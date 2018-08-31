class CreateChats < ActiveRecord::Migration
  def change
    create_table :chats do |t|
      t.integer :group_id
      t.integer :context
      t.string :name

      t.timestamps null: false
    end
  end
end
