class MessagesController < ApplicationController
    def create
        @chat = Chat.find(params[:chat_id])
        @message = @chat.messages.create(message_params)
        
        redirect_to chat_path(@chat)
    end
    
  
    private
        def message_params
            params.require(:message).permit(:user_id, :body)
        end
        
end
