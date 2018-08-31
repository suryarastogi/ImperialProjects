class Competition < ActiveRecord::Base
  
  has_many :matches
  belongs_to :user
  belongs_to :channel
  has_many :competitors
  belongs_to :sport
  belongs_to :group
  belongs_to :winner, class_name: "Competitor"
  mount_uploader :image, ImageUploader, :mount_on => :image 
  
  accepts_nested_attributes_for :competitors
  
  def season_as_string
    if self.curr_season
      "20#{self.curr_season[0..1]}-20#{self.curr_season[2..3]}"
    end
  end
    
end
