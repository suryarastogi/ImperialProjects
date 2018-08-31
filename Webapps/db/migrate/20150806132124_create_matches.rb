class CreateMatches < ActiveRecord::Migration
  def change
    create_table :matches do |t|
      t.integer :competition_id
      t.integer :channel_id
      t.integer :competitor1_id
      t.integer :competitor2_id
      t.integer :winner_id
      t.integer :winner_match_id
      t.integer :winner_match_pos
      t.boolean :match_finished
      t.integer :round
      t.integer :competitor1_score, default: 0
      t.integer :competitor2_score, default: 0
      t.integer :foreign_id
      ##
      t.string :time
      t.string :home_goalkeeper
      t.string :home_defense
      t.string :home_midfield
      t.string :home_forward
      t.string :home_subs
      t.string :home_formation
      t.string :home_yellows
      t.string :away_goalkeeper
      t.string :away_defense
      t.string :away_midfield
      t.string :away_forward
      t.string :away_subs
      t.string :away_formation
      t.string :away_yellows
      t.string :location
      t.string :stadium
      t.boolean :archived, default: false
      t.datetime :date
      t.string :season
      ##
      t.timestamps null: false
    end
  end
end
