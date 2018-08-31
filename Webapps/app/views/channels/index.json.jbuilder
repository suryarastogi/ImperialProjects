json.array!(@channels) do |channel|
  json.extract! channel, :id, :user_id, :name
  json.url channel_url(channel, format: :json)
end
