class CreateCompetitors < ActiveRecord::Migration
  def change
    create_table :competitors do |t|
      t.string :name
      t.integer :competition_id
      t.integer :user_id
      t.integer :foreign_id
      t.timestamps null: false
    end
  end
end
