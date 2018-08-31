json.array!(@chats) do |chat|
  json.extract! chat, :id, :group_id, :context, :name
  json.url chat_url(chat, format: :json)
end
