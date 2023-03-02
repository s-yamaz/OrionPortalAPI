from motor import motor_asyncio

MONGO_CONNECTIONS = "mongodb://root:password@oicosf-test.cc.kitami-it.ac.jp:27017"

client = motor_asyncio.AsyncIOMotorClient(MONGO_CONNECTIONS)

database = client.orion

project_collection = database.get_collection("projects")
foreign_service_project_collection = database.get_collection("foreign_service_projects")
node_log_collection = database.get_collection("node_logs")
conversation_collection = database.get_collection("conversations")
slack_user_collection = database.get_collection("slack_users")


async def fetch_all_projects():
    projects = []
    async for project in project_collection.find():
        projects.append(project)

    return projects
