# Task 1

Build a todo applicatin working on a single web page.
Use all the CRUD functions.
Store created tasks as a **list of objects** inside app and retrieve them on each load.

# Task 2

Add task categories as a separate **list of objects** and link tasks with the categories.
Update CRUD with adding Category and selecting tasks category.

# Task 3

Build simple Auth system of users (Register and Login)
Store users as a **list of objects** inside app.
View a user related tasks after user's login and store tasks with linking to user.

# Task 4

Create roles of Auth, manually add admin to users **list of obects**.
After admin auth show Web page with tasks, categories and users (UI is up to your creativity)
On selecting User, show that user's tasks and note task category
On selecting category, show all tasks created on that category and note User

# Task 5

Add SQL support with a simple .sqlite file. Use SQLAlchemy and Flask-sqlalchemy libraries.
Create db.Models and tables:
 + User
 + Task
 + User_role
 + Category
Build foreign keys and relationships (optional)
Retrieve all data on Views from database, and store data.