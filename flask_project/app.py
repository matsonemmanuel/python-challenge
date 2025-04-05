from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)

# MongoDB URI
app.config["MONGO_URI"] = "mongodb://localhost:27017/myAppDB"  # Change 'your_database_name' to your DB name

mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/add_user', methods=['POST'])
def add_user():
    # Get data from form
    name = request.form['name']
    email = request.form['email']

    # Insert data into MongoDB
    users_collection = mongo.db.users  # Access the "users" collection
    users_collection.insert_one({"name": name, "email": email})

    return "User added successfully!"

@app.route('/users')
def show_users():
    users_collection = mongo.db.users
    users = users_collection.find()  # Retrieve all users

    return render_template('users.html', users=users)