class UpdatesController < ApplicationController
  
  def create
    @channel = Channel.find(params[:channel_id])
    @update = @channel.updates.create(update_params)
    
    redirect_to chat_path(@channel)
  end
 
  private
    def update_params
      params.require(:update).permit(:user_id, :body)
    end
end
