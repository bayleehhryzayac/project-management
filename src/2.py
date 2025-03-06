import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask and SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project-management.db"
db = SQLAlchemy(app)

# Define Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    
    # Define Task model
    class Task(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        project_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)
        title = db.Column(db.String(100), nullable=False)
        description = db.Column(db.Text, nullable=False)
        due_date = db.Column(db.DateTime, nullable=False)
        completed = db.Column(db.Boolean, default=False)
        
    # Define User model
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(100), nullable=False)
        email = db.Column(db.String(100), unique=True, nullable=False)
        password = db.Column(db.String(100), nullable=False)
        
    # Define Project-User relationship model
    class UserProject(db.Model):
        user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
        project_id = db.Column(db.Integer, db.ForeignKey("project.id"), primary_key=True)
        role = db.Column(db.String(100), default="developer")
        
    # Define Task-User relationship model
    class UserTask(db.Model):
        user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
        task_id = db.Column(db.Integer, db.ForeignKey("task.id"), primary_key=True)
        
    # Define the __repr__ method to display Projects and Tasks as strings
    def __repr__(self):
        return f"Project('{self.title}', '{self.description}', '{self.created_date}')"
    
    def __repr__(self):
        return f"Task('{self.title}', '{self.description}', '{self.due_date}', '{self.completed}')"
    
# Define routes and forms for the application
@app.route("/")
def index():
    projects = Project.query.all()
    return render_template("index.html", projects=projects)

@app.route("/project/<int:project_id>")
def project(project_id):
    project = Project.query.get(project_id)
    tasks = Task.query.filter_by(project_id=project_id).all()
    return render_template("project.html", project=project, tasks=tasks)

@app.route("/create-project", methods=["GET", "POST"])
def create_project():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        
        # Create new project and save to database
        project = Project(title=title, description=description)
        db.session.add(project)
        db.session.commit()
        
        return redirect(url_for("index"))
    
    return render_template("create-project.html")

@app.route("/create-task", methods=["GET", "POST"])
def create_task():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        due_date = request.form["due_date"]
        
        # Create new task and save to database
        task = Task(title=title, description=description, due_date=due_date)
        db.session.add(task)
        db.session.commit()
        
        return redirect(url_for("project", project_id=task.project_id))
    
    return render_template("create-task.html")

if __name__ == "__main__":
    app.run(debug=True)