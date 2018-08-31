class CreateCompetitions < ActiveRecord::Migration
  def change
    create_table :competitions do |t|
      t.string :name
      t.integer :sport_id
      t.integer :channel_id
      t.integer :user_id
      t.integer :competition_type
      t.integer :group_id
      t.integer :winner_id
      t.string :curr_season
      t.string :image
      t.timestamps null: false
    end
  end
end
