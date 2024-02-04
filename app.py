from flask import Flask, render_template, request, redirect, url_for,session

app = Flask(__name__)
app.secret_key='your_secret_key'

# In-memory data storage (replace this with a database in a real application)
users = {'user1': {'username': 'user1', 'password': 'pass1'},
         'user2': {'username': 'user2', 'password': 'pass2'}}

@app.route('/')
def home():
    return 'Welcome to the Home Page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)

        if user and user['password'] == password:
            return f'Welcome, {username}!'
        else:
            return 'Invalid username or password. Please try again.'

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            return 'Username already exists. Please choose a different one.'
        else:
            users[username] = {'username': username, 'password': password}
            return 'Registration successful. You can now login.'

    return render_template('register.html')

@app.route('/logout')
def logout():
    
    return render_template('logout.html')


if __name__ == '__main__':
    app.run(debug=True)
