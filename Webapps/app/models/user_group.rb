# Declare a Model based on the many-to-many linking table.
class UserGroup < ActiveRecord::Base
  validates :user, presence: true
  validates :group, presence: true
  
  belongs_to :user
  belongs_to :group
end