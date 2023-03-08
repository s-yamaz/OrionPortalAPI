from database import conversation_collection


def get_conversations(channel_id: str):
    filter = {"channel_id": channel_id}
    documents = conversation_collection.find(filter)
    return [conversation_serializer(document) for document in documents]


def conversation_serializer(conversation) -> dict:
    conversation["id"] = str(conversation["_id"])
    del conversation["_id"]
    return conversation
