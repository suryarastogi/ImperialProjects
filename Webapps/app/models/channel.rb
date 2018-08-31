class Channel < ActiveRecord::Base
    validates :user_id, presence: true
    validates :name, presence: true, length: { within: 1..40 }
    
    has_many :updates, dependent: :destroy
    has_many :chats, :class_name => "Chat", :foreign_key => "context", dependent: :destroy
    accepts_nested_attributes_for :updates
end
