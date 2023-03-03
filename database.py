from pymongo import MongoClient

MONGO_CONNECTIONS = "mongodb://root:password@oicosf-test.cc.kitami-it.ac.jp:27017"

client = MongoClient(MONGO_CONNECTIONS)
collections = client.get_database("orion")

database = client.orion

project_collection = database.get_collection("projects")
foreign_service_project_collection = database.get_collection("foreign_service_projects")
node_log_collection = database.get_collection("node_logs")
conversation_collection = database.get_collection("conversations")
slack_user_collection = database.get_collection("slack_users")
