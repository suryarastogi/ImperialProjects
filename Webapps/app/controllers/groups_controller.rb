class GroupsController < ApplicationController
  before_action :set_group, only: [:show, :edit, :update, :destroy]
  before_filter :user_is_signed_in

  # GET /groups
  # GET /groups.json
  def index
    @groups = Group.all
  end

  # GET /groups/1
  # GET /groups/1.json
  def show
  end

  # GET /groups/new
  def new
    @group = Group.new
  end

  # GET /groups/1/edit
  def edit
  end
  
  def fedit
  end

  # POST /groups
  # POST /groups.json
  def create
    @group = Group.new(group_params)
    #register owner as member
    @group.users << @group.user 
    
    respond_to do |format|
      if @group.save
        format.html { redirect_to @group, notice: 'Group was successfully created.' }
        format.json { render :show, status: :created, location: @group }
      else
        format.html { render :new }
        format.json { render json: @group.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /groups/1
  # PATCH/PUT /groups/1.json
  def update
    respond_to do |format|
      if @group.update(group_params)
        if @group.id == current_user.group_id
          @redirect = friends_path
        else
          @redirect = @group
          @group.users << @group.user
          @group.save
        end
        format.html { redirect_to @redirect, notice: 'Group was successfully updated.' }
        format.json { render :show, status: :ok, location: @group }
      else
        format.html { render :edit }
        format.json { render json: @group.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /groups/1
  # DELETE /groups/1.json
  def destroy
    @group.destroy
    respond_to do |format|
      format.html { redirect_to groups_url, notice: 'Group was successfully destroyed.' }
      format.json { head :no_content }
    end
  end
  
  def addnew
    user = current_user
    @group = Group.find(params[:group_id])
    @group.users << user
    @group.save
    redirect_to @group
  end
  
  def removeself
    user = current_user
    @group = Group.find(params[:group_id])
    @group.users.delete(user)
    redirect_to @group
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_group
      @group = Group.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def group_params
      params.require(:group).permit(:user_id, :name, :new_users)
    end
end
