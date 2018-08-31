class Chat < ActiveRecord::Base
  validates :name, presence: true, length: { within: 1..40 }
  validates :channel, presence: true
  validates :group, presence: true
  
  has_many :messages, dependent: :destroy
  belongs_to :group
  belongs_to :channel, :class_name => "Channel", :foreign_key => 'context'
  
  accepts_nested_attributes_for :messages
end
