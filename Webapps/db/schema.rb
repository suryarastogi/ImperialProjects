# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20150806132200) do

  create_table "channels", force: :cascade do |t|
    t.integer  "user_id"
    t.string   "name"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "chats", force: :cascade do |t|
    t.integer  "group_id"
    t.integer  "context"
    t.string   "name"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "competitions", force: :cascade do |t|
    t.string   "name"
    t.integer  "sport_id"
    t.integer  "channel_id"
    t.integer  "user_id"
    t.integer  "competition_type"
    t.integer  "group_id"
    t.integer  "winner_id"
    t.string   "curr_season"
    t.string   "image"
    t.datetime "created_at",       null: false
    t.datetime "updated_at",       null: false
  end

  create_table "competitors", force: :cascade do |t|
    t.string   "name"
    t.integer  "competition_id"
    t.integer  "user_id"
    t.integer  "foreign_id"
    t.datetime "created_at",     null: false
    t.datetime "updated_at",     null: false
  end

  create_table "groups", force: :cascade do |t|
    t.integer  "user_id"
    t.string   "name"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "matches", force: :cascade do |t|
    t.integer  "competition_id"
    t.integer  "channel_id"
    t.integer  "competitor1_id"
    t.integer  "competitor2_id"
    t.integer  "winner_id"
    t.integer  "winner_match_id"
    t.integer  "winner_match_pos"
    t.boolean  "match_finished"
    t.integer  "round"
    t.integer  "competitor1_score", default: 0
    t.integer  "competitor2_score", default: 0
    t.integer  "foreign_id"
    t.string   "time"
    t.string   "home_goalkeeper"
    t.string   "home_defense"
    t.string   "home_midfield"
    t.string   "home_forward"
    t.string   "home_subs"
    t.string   "home_formation"
    t.string   "home_yellows"
    t.string   "away_goalkeeper"
    t.string   "away_defense"
    t.string   "away_midfield"
    t.string   "away_forward"
    t.string   "away_subs"
    t.string   "away_formation"
    t.string   "away_yellows"
    t.string   "location"
    t.string   "stadium"
    t.boolean  "archived",          default: false
    t.datetime "date"
    t.string   "season"
    t.datetime "created_at",                        null: false
    t.datetime "updated_at",                        null: false
  end

  create_table "messages", force: :cascade do |t|
    t.integer  "user_id"
    t.integer  "chat_id"
    t.text     "body"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "sports", force: :cascade do |t|
    t.string   "name"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "updates", force: :cascade do |t|
    t.integer  "user_id"
    t.integer  "channel_id"
    t.text     "body"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "user_groups", force: :cascade do |t|
    t.integer "user_id",  null: false
    t.integer "group_id", null: false
  end

  create_table "users", force: :cascade do |t|
    t.string   "username"
    t.string   "email"
    t.string   "password_digest"
    t.string   "image"
    t.integer  "group_id"
    t.datetime "created_at",      null: false
    t.datetime "updated_at",      null: false
  end

end
