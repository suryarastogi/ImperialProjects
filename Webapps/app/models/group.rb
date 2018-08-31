class Group < ActiveRecord::Base
    include SessionsHelper
    validates :name, presence: true, length: { within: 1..40 }
    validates :user_id, presence: true
    
    belongs_to :user
    has_many :chats, dependent: :destroy
    has_many :user_groups, dependent: :destroy
    has_many :users, :through => :user_groups
    attr_reader :new_users
    
    def new_users=(ids)
        self.user_ids = ids.split(",").uniq
    end
    
    def name_with_length
       "#{name} (#{self.users.length})" 
    end
end