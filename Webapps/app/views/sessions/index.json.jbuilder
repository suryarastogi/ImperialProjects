json.array!(@sessions) do |session|
  json.extract! session, :id, :username, :password
  json.url session_url(session, format: :json)
end
