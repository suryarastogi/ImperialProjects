# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)
include ApplicationHelper

User.create(username: "admin", email: "admin@site.com", password: "password")
Sport.create(name: "Football")
User.create(username: "test", email: "test@site.com", password: "password")
User.create(username: "john", email: "john@site.com", password: "password")
User.create(username: "sophie", email: "sophie@site.com", password: "password")
User.create(username: "sean", email: "sean@site.com", password: "password")
User.create(username: "fido", email: "fido@site.com", password: "password")
User.create(username: "charles", email: "charles@site.com", password: "password")
User.create(username: "alice", email: "alice@site.com", password: "password")

group = Group.create(user_id: "1", name: "The Crew")
group.users << User.find(1)
group.users << User.find(2)
group.users << User.find(3)
group.users << User.find(4)
group.users << User.find(5)
group.users << User.find(6)
group.users << User.find(7)
group.users << User.find(8)

group2 = Group.create(user_id: "2", name: "Arsenal Mates")
group2.users << User.find(1)
group2.users << User.find(2)
group2.users << User.find(7)
group2.users << User.find(8)

group3 = Group.create(user_id: "1", name: "Fantasy League (Work)")
group3.users << User.find(1)
group3.users << User.find(2)
group3.users << User.find(3)
group3.users << User.find(4)
group3.users << User.find(5)
group3.users << User.find(6)
group3.users << User.find(7)

group4 = Group.create(user_id: "1", name: "Flatmates")
group4.users << User.find(1)
group4.users << User.find(4)
group4.users << User.find(5)

group5 = Group.create(user_id: "1", name: "English Premier")
group5.users << User.find(1)
group5.users << User.find(2)
group5.users << User.find(3)
group5.users << User.find(4)
group5.users << User.find(5)
group5.users << User.find(6)

group6 = Group.create(user_id: "1", name: "French")
group6.users << User.find(1)
group6.users << User.find(2)
group6.users << User.find(8)
group6.users << User.find(4)
group6.users << User.find(6)

setup_tournaments

setup_matches