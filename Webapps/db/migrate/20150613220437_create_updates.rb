class CreateUpdates < ActiveRecord::Migration
  def change
    create_table :updates do |t|
      t.integer :user_id
      t.integer :channel_id
      t.text :body

      t.timestamps null: false
    end
  end
end
