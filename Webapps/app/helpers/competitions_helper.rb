module CompetitionsHelper
  def render_score(m, id)
    if id == 1
      if m.competitor1_score > m.competitor2_score
        render html: "<div class='match_winner'>#{m.competitor1_score}</div>".html_safe
      else
        render html: "<div>#{m.competitor1_score}</div>".html_safe
      end
    else
      if m.competitor2_score > m.competitor1_score
        render html: "<div class='match_winner'>#{m.competitor2_score}</div>".html_safe
      else
        render html: "<div>#{m.competitor2_score}</div>".html_safe
      end
    end
  end
  
  def count_wins(c)
    count = 0
    matches = @matches.select{|match| match.competitor1 == c or match.competitor2 == c}
    matches.each do |match|
      if match.match_finished
        if match.competitor1_score > match.competitor2_score
          if match.competitor1 == c
            count += 1
          end
        elsif match.competitor2_score > match.competitor1_score
          if match.competitor2 == c
            count += 1
          end
        end
      end
    end
    count
  end  

  def count_loses(c)  
    count = 0
    matches = @matches.select{|match| match.competitor1 == c or match.competitor2 == c}
    matches.each do |match|
      if match.match_finished
        if match.competitor1_score < match.competitor2_score
          if match.competitor1 == c
            count += 1
          end
        elsif match.competitor2_score > match.competitor1_score
          if match.competitor2 == c
            count += 1
          end
        end
      end
    end
    count
  end
  
  def count_draws(c)
    count = 0
    matches = @matches.select{|match| match.competitor1 == c or match.competitor2 == c}
    matches.each do |match|
      if match.competitor1_score == match.competitor2_score && match.match_finished
        count = count + 1
      end
    end
    count
  end
  
  def get_table_details(c)
    returnHash = { :wins => 0, :loses => 0, :draws => 0, :points => 0, :for => 0, :against => 0, :season => 0 }
    matches = @matches.select{|match| match.competitor1 == c or match.competitor2 == c}
    matches.each do |match|
      returnHash[:season] = match[:season]
      if match.match_finished
        returnHash[:for] = returnHash[:for] + match.competitor1_score
        returnHash[:against] = returnHash[:against] + match.competitor2_score
        if match.competitor1_score == match.competitor2_score
          returnHash[:draws] = returnHash[:draws] + 1
          returnHash[:points] = returnHash[:points] + 1
        elsif match.competitor1_score > match.competitor2_score
          if match.competitor1 == c
            returnHash[:wins] = returnHash[:wins] + 1
            returnHash[:points] = returnHash[:points] + 3            
          else
            returnHash[:loses] = returnHash[:loses] + 1
          end
        else
          if match.competitor1 == c
            returnHash[:loses] = returnHash[:loses] + 1
          else 
            returnHash[:wins] = returnHash[:wins] + 1
            returnHash[:points] = returnHash[:points] + 3 
          end
        end
      end
    end
    returnHash
  end
  
end
