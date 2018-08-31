class Match < ActiveRecord::Base
    
  belongs_to :competition
  belongs_to :competitor1, class_name: "Competitor"
  belongs_to :competitor2, class_name: "Competitor"
  belongs_to :winner, class_name: "Competitor"
  belongs_to :winner_match, class_name: "Match"
  belongs_to :channel
  
  def start_time
    self.date.to_s.split(' ')[1]
  end
  
  def formatted_date
    date = self.date.to_s.split('-')
    "#{date[2].split(' ')[0]}-#{date[1]}-#{date[0]}" 
  end
  
end
