from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), unique=True, nullable=False)
    content_status = db.Column(db.String(20), nullable=False)

# Database model for logging user actions
class UserLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    action = db.Column(db.String(100), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Routes
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        user = User.query.filter_by(user_id=user_id).first()
        if user:
            log = UserLog(user_id=user_id, action='login')
            db.session.add(log)
            db.session.commit()
            session['user_id'] = user_id
            return redirect(url_for('content'))
        else:
            flash('User ID not found. Please register first.', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = request.form['user_id']
        existing_user = User.query.filter_by(user_id=user_id).first()
        if existing_user:
            flash('User ID already exists. Please choose a different one.', 'danger')
        else:
            new_user = User(user_id=user_id, content_status='processing')
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/content')
def content():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter_by(user_id=user_id).first()
        if user:
            log = UserLog(user_id=user_id, action='view_content')
            db.session.add(log)
            db.session.commit()
            content = {
                'status': user.content_status,
                'videos': ['video1.mp4', 'video2.mp4'] if user.content_status == 'completed' else [],
                'images': ['image1.jpg', 'image2.jpg'] if user.content_status == 'completed' else []
            }
            return render_template('content.html', content=content)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

