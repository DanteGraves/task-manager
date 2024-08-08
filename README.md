Task Manager
This Python project is a task management application designed to help teams manage their tasks efficiently. It allows for user registration, task assignment, and tracking of task completion.

Features
User Registration: Register new users with a username and password.
Task Assignment: Assign tasks to registered users with details like the task description, due date, and completion status.
Task Overview: Generate a report of all users and their respective tasks, including completion rates and overdue tasks.
Files
task_manager.py: The main Python script that manages the task assignments, user registrations, and generates reports.
tasks.txt: A file storing all tasks assigned to users, including details like the task description, assigned date, due date, and completion status.
user.txt: A file storing all registered users along with their usernames and passwords.
user_overview.txt: A file containing the overview of each user’s task completion statistics.
Usage
1. Registering Users
To register new users, you can use the task_manager.py script. The users' credentials will be stored in user.txt.


Copy code
python task_manager.py --register-user
2. Assigning Tasks
Tasks can be assigned to users via the task_manager.py script. All tasks are stored in tasks.txt.


Copy code
python task_manager.py --assign-task
3. Generating Reports
Generate an overview of the tasks for each user, including the total tasks assigned, the percentage completed, and the overdue tasks. The report will be saved in user_overview.txt.


Copy code
python task_manager.py --generate-report
Data Overview
User Data
The user.txt file contains the following user information:

Username	Password
admin	adm1n
dante	d@nte
happy	mond@y
Tasks

User Overview
The user_overview.txt file provides a summary of each user’s task statistics:

Total Users: 3
Total Tasks: 4
Example for the user admin:

Total Tasks Assigned: 2
Percentage of Total Tasks Assigned: 50.00%
Percentage of Tasks Completed: 0.00%
Percentage of Tasks Incomplete: 100.00%
Percentage of Overdue Tasks: 100.00%