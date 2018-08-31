module ApplicationHelper
  def link_to_remove_fields(name, f)
    f.hidden_field(:_destroy) + link_to(name, '#', onclick: "remove_fields(this)", class: "btn btn-default", tabindex: "-1")
  end
  
  def link_to_add_fields(name, f, association)
    new_object = f.object.class.reflect_on_association(association).klass.new
    fields = f.fields_for(association, new_object, :child_index => "new_#{association}") do |builder|
      render(association.to_s.singularize + "_fields", :f => builder)
    end
    
    tag "input", { "type" => "button", "value" => name, 
                   "onclick" => "add_fields('competitor_fields', \"#{association}\", \"#{escape_javascript(fields)}\")",
                   "class" => "btn btn-info btn-sm", role: "button"}
  end
  
  def user_is_signed_in
    unless signed_in?
      flash[:notice] = "Please sign in."
      redirect_to login_path
    end
  end
  
  def signed_in?
    !current_user.nil?
  end
  
  def includes_user?(group,user)
      group.users.include? user
  end
  
  def includes_curr_user?(group)
      group.users.include? current_user
  end
  
  def setup_tournaments
    xmlsoccer_client = Xmlsoccer::Client.new(api_key: 'LVMPVMNCFHPWKNDZQUZSVNZJTQBYBMTOSZVFINPEUSYLWVHIIY', api_type: 'Full')
    
    response = xmlsoccer_client.get_all_leagues
    
    # GetAllLeagues() can only be called once every hour
    # If we have called it recently instead
    if response.is_a? String
      response = ["English Premier League", "English League Championship", "Scottish Premier League",
      "Bundesliga", "Serie A", "Serie B", "Ligue 1", "La Liga", "Superleague Greece",
      "Eredivisie", "Jupiler League", "Süper Lig", "Superliga", "Champions League",
      "Europe League", "Primeira Liga", "Scottish First Division", "Major League Soccer",
      "Allsvenskan", "FA Cup", "League Cup", "Mexican Primera League", "Brasileirao",
      "English League 1", "English League 2", "Ukrainian Premier League", "Russian Football Premier League",
      "Australian A-League", "Tippeligaen", "Chinese Super League", "Lega Pro", "2. Bundesliga",
      "Adelante", "Ligue 2", "Superettan", "Brasileirão Série B", "Norwegian 1. Divisjon", "Ekstraklasa"]
      response.each do |league|
        competition = Competition.create(name: league, sport_id: "1", user_id: "1", competition_type: "0", curr_season: "1516")
        competition.create_channel(user_id: "1", name: league)
        competition.save
      end
    else
      response.each do |league|
        competition = Competition.create(name: league[:name], sport_id: "1", user_id: "1", competition_type: "0", curr_season: "1516")
        competition.create_channel(user_id: "1", name: league[:name])
        competition.save
      end
    end
  end
    
  def setup_matches
    xmlsoccer_client = Xmlsoccer::Client.new(api_key: 'LVMPVMNCFHPWKNDZQUZSVNZJTQBYBMTOSZVFINPEUSYLWVHIIY', api_type: 'Full')
    
    competitions = Competition.all
    
    competitions.each do |competition|
      puts "--- #{competition.name} ---"
      response = xmlsoccer_client.get_fixtures_by_league_and_season(season_date_string: "1516", league: competition.name)
    
      if !response.is_a? String
        response.each do |match|
          season = '1516' #get_season_by_date match[:date]
          archived = match[:time] == "Finished"
          competitor1 = Competitor.find_by(foreign_id: match[:home_team_id])
          competitor2 = Competitor.find_by(foreign_id: match[:away_team_id])
          if competitor1.nil?
            competitor1 = Competitor.create(name: match[:home_team], foreign_id: match[:home_team_id], competition_id: competition.id)
          end
          if competitor2.nil?
            competitor2 = Competitor.create(name: match[:away_team], foreign_id: match[:away_team_id], competition_id: competition.id)
          end
          if match[:home_goals].nil?
            new_match = Match.create(competition_id: competition.id, competitor1_id: competitor1.id, competitor2_id: competitor2.id,
              foreign_id: match[:id],
              time: match[:time], home_goalkeeper: match[:home_lineup_goalkeeper], home_defense: match[:home_lineup_defense],
              home_midfield: match[:home_lineup_midfield], home_forward: match[:home_lineup_forward], home_subs: match[:home_lineup_substitutes],
              home_formation: match[:home_team_formation], home_yellows: match[:home_team_yellow_card_details],
              away_goalkeeper: match[:away_lineup_goalkeeper], away_defense: match[:away_lineup_defense],
              away_midfield: match[:away_lineup_midfield], away_forward: match[:away_lineup_forward], away_subs: match[:away_lineup_substitutes],
              away_formation: match[:away_team_formation], away_yellows: match[:away_team_yellow_card_details], 
              location: match[:location], date: match[:date], archived: archived, round: match[:round], season: season
              )
          else
            new_match = Match.create(competition_id: competition.id, competitor1_id: competitor1.id,
              competitor2_id: competitor2.id, competitor1_score: match[:home_goals], 
              competitor2_score: match[:away_goals], match_finished: true, foreign_id: match[:id],
              time: match[:time], home_goalkeeper: match[:home_lineup_goalkeeper], home_defense: match[:home_lineup_defense],
              home_midfield: match[:home_lineup_midfield], home_forward: match[:home_lineup_forward], home_subs: match[:home_lineup_substitutes],
              home_formation: match[:home_team_formation], home_yellows: match[:home_team_yellow_card_details],
              away_goalkeeper: match[:away_lineup_goalkeeper], away_defense: match[:away_lineup_defense],
              away_midfield: match[:away_lineup_midfield], away_forward: match[:away_lineup_forward], away_subs: match[:away_lineup_substitutes],
              away_formation: match[:away_team_formation], away_yellows: match[:away_team_yellow_card_details], 
              location: match[:location], date: match[:date], archived: archived, round: match[:round], season: season
              )
          end
          new_match.create_channel(user_id: "1", name: "#{match[:home_team]} vs #{match[:away_team]}")
          new_match.save
          puts new_match.channel.name
        end
      end
    end
  end
  
  def get_season_by_date (date)
    #puts date
    date = date.to_s
    #puts date
    year = date.split('-')[0][2..3]
    #puts year
    month = date.split('-')[1]
    #puts month
    if month.to_i > 6
      "#{year}#{year.to_i+1}"
    else
      "#{year.to_i-1}#{year}"
    end
  end
  
end