from database import project_collection


def fetch_all_projects():
    projects = []
    for project in project_collection.find():
        projects.append(project)

    return projects
