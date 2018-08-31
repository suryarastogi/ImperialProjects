class MatchesController < ApplicationController
  before_action :set_match, only: [:show, :edit, :update, :destroy, :goal, :game_over]

  # GET /matches
  # GET /matches.json
  def index
    @matches = Match.all
  end

  # GET /matches/1
  # GET /matches/1.json
  def show
    @competition = @match.competition
    update_channel_name(@match)
  end

  # GET /matches/new
  def new
    @match = Match.new
  end

  # GET /matches/1/edit
  def edit
  end

  # PATCH /matches/1/goal
  def goal
    scorer = params.require(:match).permit(:scorer)[:scorer]
    competitor_scored scorer
    redirect_to @match
  end
  
  def game_over
    @match.match_finished = true
    @match.save
    update_tournament
    redirect_to @match
  end

  # POST /matches
  # POST /matches.json
  def create
    @match = Match.new(match_params)
    respond_to do |format|
      if @match.save
        format.html { redirect_to $redirect, notice: 'Match was successfully created.' }
        format.json { render :show, status: :created, location: @match }
      else
        format.html { render :new }
        format.json { render json: @match.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /matches/1
  # PATCH/PUT /matches/1.json
  def update
    @com1_old_score = @match.competitor1_score
    @com2_old_score = @match.competitor2_score
    respond_to do |format|
      if @match.update(match_params)
        update_tournament
        puts "Updating"
        update_channel_name(@match)
        update_channel_name(@match.winner_match) unless @match.winner_match.nil?
        format.html { redirect_to @match, notice: 'Match was successfully updated.' }
        format.json { render :show, status: :ok, location: @match }
      else
        format.html { render :edit }
        format.json { render json: @match.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /matches/1
  # DELETE /matches/1.json
  def destroy
    @match.destroy
    respond_to do |format|
      format.html { redirect_to matches_url, notice: 'Match was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_match
      @match = Match.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def match_params
      params.require(:match).permit(:competition_id, :channel_id, :winner, :competitor1_score, :competitor2_score, :winner_match_pos, :match_finished)
    end
    
    def update_tournament
      if @match.match_finished
        set_winner_competitor
        broadcast_match_result(@match.channel)
        broadcast_match_result(@match.competition.channel)
        check_tournament_winner
      else
        broadcast_match_update
      end
    end
    
    def broadcast_match_result(channel)
      if @match.competitor1_score == @match.competitor2_score
        channel.updates.create(body: "#{@match.competitor1.name} vs #{@match.competitor2.name} has ended in a draw, #{@match.competitor1_score} - #{@match.competitor2_score}", user_id: channel.user_id)
      elsif winner_of_match == @match.competitor1
        channel.updates.create(body: "#{@match.competitor1.name} has won #{@match.competitor1_score} - #{@match.competitor2_score} against #{@match.competitor2.name}", user_id: channel.user_id)
      else
        channel.updates.create(body: "#{@match.competitor2.name} has won #{@match.competitor2_score} - #{@match.competitor1_score} against #{@match.competitor1.name}", user_id: channel.user_id)
      end
    end
    
    def broadcast_match_update
        if @com1_old_score != @match.competitor1_score
          @match.channel.updates.create(body: "#{@match.competitor1.name} has scored a goal against #{@match.competitor2.name}, #{@match.competitor1_score} - #{@match.competitor2_score}", user_id: @match.channel.user_id)
        elsif @com2_old_score != @match.competitor2_score
          @match.channel.updates.create(body: "#{@match.competitor2.name} has scored a goal against #{@match.competitor1.name}, #{@match.competitor2_score} - #{@match.competitor1_score}", user_id: @match.channel.user_id)
        else
          @match.channel.updates.create(body: "Nothing happened", user_id: @match.channel.user_id)
        end
    end
    
    def winner_of_match
      if @match.competitor1_score > @match.competitor2_score
        @match.competitor1
      else
        @match.competitor2
      end
    end
    
    def loser_of_match
      if @match.competitor1_score > @match.competitor2_score
        @match.competitor2
      else
        @match.competitor1
      end
    end
    
    def update_channel_name(match)
      if match.channel.nil?
        match.create_channel(user_id: current_user.id, name: "v")
        match.save
      end
      if match.channel.name == "v"
        if !match.competitor1.nil? and !match.competitor2.nil?
          match.channel.name = "#{match.competitor1.name} v #{match.competitor2.name}"
          match.channel.save
        end
      end
    end
    
    def set_winner_competitor
      if @match.winner_match
        winner = winner_of_match
        @match.winner = winner
        if @match.winner_match_pos == 1
          @match.winner_match.competitor1 = winner
        elsif @match.winner_match_pos == 2
          @match.winner_match.competitor2 = winner
        end
        @match.winner_match.save
      end
    end
    
    def competitor_scored(c)
      if c.to_i == 1
        @match.competitor1_score = @match.competitor1_score + 1
        @match.channel.updates.create(body: "#{@match.competitor1.name} has scored a goal against #{@match.competitor2.name}, #{@match.competitor1_score} - #{@match.competitor2_score}", user_id: @match.channel.user_id)
      else
        @match.competitor2_score = @match.competitor2_score + 1
        @match.channel.updates.create(body: "#{@match.competitor2.name} has scored a goal against #{@match.competitor1.name}, #{@match.competitor2_score} - #{@match.competitor1_score}", user_id: @match.channel.user_id)
      end
      @match.save
    end
    
    def check_tournament_winner
      if @match.round ==  Math.log2(@match.competition.competitors.length).to_i + 1 && @match.match_finished
        winner = winner_of_match
        @match.competition.winner = winner
        @match.competition.channel.updates.create(body: "#{winner.name} has won the tournament", user_id: 0)
        @match.competition.save
      end
    end
    
end
