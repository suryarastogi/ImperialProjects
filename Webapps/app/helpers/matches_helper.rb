module MatchesHelper
    
  def user_has_competed_in?(match)
    competitor1 = match.competitor1
    competitor2 = match.competitor2
    if competitor1.nil? && competitor2.nil?
      false
    elsif competitor1.nil?
      user_is_competitor?(competitor2) 
    elsif competitor2.nil?
      user_is_competitor?(competitor1)
    else
      user_is_competitor?(competitor1) || user_is_competitor?(competitor2) 
    end
  end
  
  def user_is_competitor?(competitor)
    user = current_user
    user == competitor.user
  end
  
  def round_name(round_number, competition)
    rounds = Math.log2(competition.competitors.length).ceil
    if rounds == 1
      "Final"  
    elsif rounds == 2
      if round_number == 1
        "Semi-Final"
      else
        "Final"
      end
    elsif rounds == 3
      if round_number == 1
        "Quarter-Final"  
      elsif round_number == 2
        "Semi-Final"
      else
        "Final"
      end
    else
      if rounds == round_number
        "Final"
      elsif rounds - 1 == round_number
        "Semi-Final"
      elsif rounds - 2 == round_number
        "Quarter-Final"
      else
        "Round #{round_number}"
      end
    end
  end
  
end
