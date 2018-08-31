json.array!(@competitors) do |competitor|
  json.extract! competitor, :id, :name
  json.url competitor_url(competitor, format: :json)
end
