from database import node_log_collection


def get_all_logs_by_node(node_id: str):
    node_logs = []
    filter = {"project_id": node_id}
    documents = node_log_collection.find(filter)
    for document in documents:
        node_logs.append(document)

    return node_logs
