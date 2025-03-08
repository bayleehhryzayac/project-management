import os
from datetime import datetime as dt

def get_projects():
    projects = []
    # Add your project names here
    projects += ["Project 1", "Project 2", "Project 3"]
    return projects

def get_tasks(project):
    tasks = []
    # Add your task names and due dates for the corresponding project
    if project == "Project 1":
        tasks += [("Task 1", dt.strptime("2022-03-01", "%Y-%m-%d")), ("Task 2", dt.strptime("2022-03-15", "%Y-%m-%d"))]
    elif project == "Project 2":
        tasks += [("Task 1", dt.strptime("2022-04-01", "%Y-%m-%d")), ("Task 2", dt.strptime("2022-05-15", "%Y-%m-%d"))]
    elif project == "Project 3":
        tasks += [("Task 1", dt.strptime("2022-06-01", "%Y-%m-%d")), ("Task 2", dt.strptime("2022-07-15", "%Y-%m-%d"))]
    return tasks

def get_progress(project, task):
    progress = "In Progress"
    if project == "Project 1" and task == "Task 1":
        progress = "Completed"
    elif project == "Project 2" and task == "Task 2":
        progress = "Completed"
    return progress

def main():
    projects = get_projects()
    for project in projects:
        tasks = get_tasks(project)
        for task, due_date in tasks:
            print(f"Project: {project}, Task: {task}, Due Date: {due_date}, Progress: {get_progress(project, task)}")

if __name__ == "__main__":
    main()