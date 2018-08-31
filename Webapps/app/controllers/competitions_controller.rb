class CompetitionsController < ApplicationController
  helper CompetitionsHelper
  before_action :set_competition, only: [:show, :edit, :update, :destroy]
  after_action :update_competitor_names, only: [:create]

  # GET /competitions
  # GET /competitions.json
  def index
    @competitions = Competition.all
  end

  # GET /competitions/1
  # GET /competitions/1.json
  def show
    @rounds = set_rounds
    @matches = @competition.matches.select { |match| match.season == @competition.curr_season }
    @matches = @matches.sort_by{ |m| m.round }
  end

  # GET /competitions/new
  def new
    @sport = Sport.find(params[:sport_id])
    @competition = Competition.new
    @groups = Group.all.select { |group| includes_curr_user?(group) }
  end

  # GET /competitions/1/edit
  def edit
  end

  # POST /competitions
  # POST /competitions.json
  def create
    @competition = Competition.new(competition_params)
    add_group_users_to_competition # if exists
    create_channel
    respond_to do |format|
      if @competition.save
        generate_fixtures
        format.html { redirect_to @competition, notice: "Competition #{@competition.competition_type} was successfully created." }
        format.json { render :show, status: :created, location: @competition }
      else
        format.html { render :new }
        format.json { render json: @competition.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /competitions/1
  # PATCH/PUT /competitions/1.json
  def update
    respond_to do |format|
      if @competition.update(competition_params)
        format.html { redirect_to @competition, notice: 'Competition was successfully updated.' }
        format.json { render :show, status: :ok, location: @competition }
      else
        format.html { render :edit }
        format.json { render json: @competition.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /competitions/1
  # DELETE /competitions/1.json
  def destroy
    @competition.destroy
    respond_to do |format|
      format.html { redirect_to competitions_url, notice: 'Competition was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_competition
      @competition = Competition.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def competition_params
      params.require(:competition).permit(:name, :sport_id, :user_id, :competition_type, :image, :group_id, :curr_season, competitors_attributes: [:id, :name, :_destroy, :user_id, :user])
    end
    
    def create_channel
      ch = Channel.create(:name => @competition.name, :user_id => @competition.user_id)
      @competition.channel_id = ch.id
    end
   
    def generate_fixtures
      update_competitor_names
      case @competition.competition_type
        when 1 # Single Round Robin
          generate_single_rr
        when 2 # Double Round Robin
          generate_double_rr
        when 3 # Tournament
          generate_tournament
      end
    end
    
  def generate_single_rr
    @fixtures = @competition.competitors.to_a.combination(2).to_a
    @fixtures.each do |fixture|
      match = @competition.matches.build()
      match.competitor1 = fixture[0]
      match.competitor2 = fixture[1]
      match.create_channel(user_id: current_user.id, name: "#{match.competitor1.name} vs #{match.competitor2.name}")
      match.save
    end
  end
  
  def generate_double_rr
    2.times { generate_single_rr }
  end
  
  def generate_tournament
    num_competitors = @competition.competitors.length
    @curr_round = Array.new(Math.log2(num_competitors)+1)
    @fixtures = @competition.competitors.to_a
    next_round = build_first_two_rounds
    if num_competitors > 3
      build_playoffs next_round
    end
  end
  
  def build_first_two_rounds
    num_competitors = @competition.competitors.length
    if Math.log2(num_competitors) % 1 == 0 # if regular bracket size (base 2)
      i = 0
      while i < num_competitors/2 do
        match = @competition.matches.build()
        match.competitor1 = @fixtures[(2*i)]
        match.competitor2 = @fixtures[(2*i)+1]
        match.round = 1
        match.create_channel(user_id: current_user.id, name: "#{match.competitor1.name} vs #{match.competitor2.name}")
        match.save
        @curr_round[i] = match
        i = i + 1
      end 
      return 2
    else # irregular bracket size
      i = 0
      rounds = Math.log2(num_competitors).to_i
      num_first_round = num_competitors - 2**(rounds - 1)
      # creating second round of matches
      puts rounds
      while i < 2**(rounds-1) do
        match = @competition.matches.build()
        match.competitor1 = @fixtures[(2*i)]
        match.competitor2 = @fixtures[(2*i)+1]
        match.round = 2
        match.create_channel(user_id: current_user.id, name: "#{match.competitor1.name} vs #{match.competitor2.name}")
        match.save
        puts match.channel.name
        @curr_round[i] = match
        i = i + 1
      end 
      i = i*2
      m = 0
      # storing extra competitors
      @spares = Array.new(num_first_round)
      while i < num_competitors do
        @spares[m] = @fixtures[i]
        puts "#{i}:#{@fixtures[i].name}"
        i = i + 1
        m = m + 1
      end
      i = 0
      # populate first round with extra competitors
      while i < m do
        match = @competition.matches.build()
        match.create_channel(user_id: current_user.id, name: match)
        if i % 2 == 0
          comp = @curr_round[i/2].competitor1
          @curr_round[i/2].competitor1 = nil
          match.competitor1 = comp
          match.competitor2 = @spares[i]
          match.winner_match_pos = 1
        else
          comp = @curr_round[i/2].competitor2
          @curr_round[i/2].competitor2 = nil
          match.competitor2 = comp
          match.competitor1 = @spares[i]
          match.winner_match_pos = 2
        end
          match.channel.name = "#{match.competitor1.name} vs #{match.competitor2.name}"
          match.channel.save
          match.winner_match = @curr_round[i/2]
          match.winner_match.save
          match.round = 1
          match.save
          i = i + 1
      end
      3
    end
  end

  def build_playoffs(round)
    while @curr_round.length > 1
      num_matches = @curr_round.length/2
      @next_round = Array.new(num_matches)
      i = 0
      num_matches.times {
        puts "looping in playoffs"
        match = @competition.matches.create()
        match.round = round
        match.create_channel(user_id: current_user.id, name: "v")
        @next_round[i] = match
        set_next_match(@curr_round[(2*i)],match,i,1)
        set_next_match(@curr_round[(2*i)+1],match,i,2)
        i += 1
      }
      @curr_round.each do |m|
        m.save unless m.nil?
      end
      @curr_round = @next_round
      round += 1
    end
    @curr_round[0].round = round - 1
    @curr_round[0].save
  end
  
  def set_next_match(comp, match, i, pos)
    puts "settingnextmatch"
    if comp.is_a? Competitor
      puts comp.name
      if pos == 1
        match.competitor1 = comp
      else
        match.competitor2 = comp
      end
    elsif comp.is_a? Match
      @curr_round[(2*i)+(pos-1)].winner_match = match
      @curr_round[(2*i)+(pos-1)].winner_match_pos = pos
    end
  end

  def set_rounds
    num_rounds = Math.log2(@competition.competitors.length) + 1
    rounds = Array.new(num_rounds)
    final = @competition.matches.where(round: num_rounds).to_a
    rounds.unshift(final)
    bracket = @competition.matches.where(round: num_rounds-1).to_a
    i=0
    (rounds.length - 1).times do 
      rounds.unshift(bracket)
      bracket = @competition.matches.where(round: (num_rounds-2-i)).to_a
      i+=1
    end
    rounds = rounds.reject {|r| r == [] || r.nil?}
    return rounds
  end
  
  def set_rounds1
    rounds = Array.new(Math.log2(@competition.competitors.length) + 1)
    final = @competition.matches.where(winner_match: nil).to_a
    rounds.unshift(final)
    bracket = @competition.matches.where(winner_match: final).to_a
    (rounds.length - 1).times do 
      rounds.unshift(bracket)
      bracket = @competition.matches.where(winner_match: bracket).to_a
    end
    rounds = rounds.reject {|r| r == [] || r.nil?}
    puts "##### #{rounds} #####"
    puts "##### #{@competition.matches.where(winner_match: !nil).to_a} ########"
    return rounds
  end
    
  def update_competitor_names
    @competition.competitors.each do |competitor|
      if competitor.name == ""
        competitor.name = competitor.user.username
        competitor.save
      end
    end
  end
  
  def add_group_users_to_competition
    if !@competition.group.nil?
      @competition.group.users.each do |g|
        if !g.nil?
          c = Competitor.create(user: g, name: g.username, competition_id: @competition.id)
          @competition.competitors << c
          c.save
        end
      end
      @competition.save
    end
  end
    
end
