class Sport < ActiveRecord::Base
  
  validates :name, presence: true, length: {  within: 1..50 }
    
  has_many :competitions
    
  def live_score_pull
    xmlsoccer_client = Xmlsoccer::Client.new(api_key: 'LVMPVMNCFHPWKNDZQUZSVNZJTQBYBMTOSZVFINPEUSYLWVHIIY', api_type: 'Full')
    
    response = xmlsoccer_client.get_live_score
    
    if !response.is_a? String
      response.each do |match|
          puts "--> Updating Match #{match[:id]}"
          m = Match.find_by(foreign_id: match[:id])
          check_for_changes(m, match)
          m.update( 
              time: match[:time], home_goalkeeper: match[:home_lineup_goalkeeper], home_defense: match[:home_lineup_defense],
              home_midfield: match[:home_lineup_midfield], home_forward: match[:home_lineup_forward], home_subs: match[:home_lineup_substitutes],
              home_formation: match[:home_team_formation], home_yellows: match[:home_team_yellow_card_details],
              competitor1_score: match[:home_goals], competitor2_score: match[:away_goals],
              away_goalkeeper: match[:away_lineup_goalkeeper], away_defense: match[:away_lineup_defense],
              away_midfield: match[:away_lineup_midfield], away_forward: match[:away_lineup_forward], away_subs: match[:away_lineup_substitutes],
              away_formation: match[:away_team_formation], away_yellows: match[:away_team_yellow_card_details], 
              location: match[:location], date: match[:date], archived: false
              )
      end
    else
      puts response
    end
  end
  
  def check_for_changes(match, updated_match)
    if updated_match[:time] == "Finished" && match[:time] != "Finished"
      broadcast_match_result(match.channel, updated_match)
      broadcast_match_result(match.competition.channel, updated_match)
    else
      broadcast_match_update(updated_match[:home_goals], updated_match[:away_goals], match)
    end
  end
  
  def broadcast_match_result(channel, match)
    if match[:home_goals] == match[:away_goals]
      channel.updates.create(body: "#{match[:home_team]} vs #{match[:away_team]} has ended in a draw, #{match[:home_goals]} - #{match[:away_goals]}", user_id: channel.user_id)
    elsif match[:home_goals] > match[:away_goals]
      channel.updates.create(body: "#{match[:home_team]} has won #{match[:home_goals]} - #{match[:away_goals]} against #{match[:away_team]}", user_id: channel.user_id)
    else
      channel.updates.create(body: "#{match[:away_team]} has won #{match[:away_goals]} - #{match[:home_goals]} against #{match[:home_team]}", user_id: channel.user_id)
    end
  end
  
  def broadcast_match_update(com1_new_score, com2_new_score, match)
      if com1_new_score.to_i != match.competitor1_score
        match.channel.updates.create(body: "#{match.competitor1.name} has scored a goal against #{match.competitor2.name}, #{com1_new_score} - #{com2_new_score}", user_id: match.channel.user_id)
      elsif com2_new_score.to_i != match.competitor2_score
        match.channel.updates.create(body: "#{match.competitor2.name} has scored a goal against #{match.competitor1.name}, #{com2_new_score} - #{com1_new_score}", user_id: match.channel.user_id)
      end
  end
end
