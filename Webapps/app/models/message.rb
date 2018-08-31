class Message < ActiveRecord::Base
  validates :chat_id, presence: true
  validates :user_id, presence: true
  validates :body, presence: true
  
  belongs_to :user, :class_name => 'User'
  belongs_to :chat, :class_name => 'Chat'
  
  after_create :broadcast
  
  def broadcast
    user = User.find_by(id: self.user_id)
    if user
      username = user.username
      user_id = user.id
    else
      username = "Broadcast"
      user_id = 0
    end
    Pusher["chat#{self.chat_id}"].trigger('update', {
       :body => "#{body}",
       :user => username,
       :user_id => user_id,
       :chat_id => self.chat_id,
       :time => self.created_at
     })
  end 
end
