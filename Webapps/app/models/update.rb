class Update < ActiveRecord::Base
    
    validates :channel_id, presence: true
    validates :body, presence: true
    
    belongs_to :channel
    after_create :forward, :broadcast
  
  def broadcast
    
    username = "Broadcast"
    user_id = 0
    Pusher["channel#{self.channel_id}"].trigger('update', {
       :body => "#{body}",
       :user => username,
       :user_id => user_id,
       :channel_id => self.channel_id,
       :time => self.created_at
     })
  end
  
  def forward
    @channel = Channel.find(self.channel_id)
    @channel.chats.each do |chat|
      if chat
        chat.messages.create(
        :user_id => 0,
        :body => self.body,
        :chat_id => chat.id)
      end
    end
  end
end
