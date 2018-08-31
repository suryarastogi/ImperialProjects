json.array!(@matches) do |match|
  json.extract! match, :id, :p1score, :p2score
  json.url match_url(match, format: :json)
end
