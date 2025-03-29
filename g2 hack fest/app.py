from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import firebase_admin
from firebase_admin import credentials, firestore, auth
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# Initialize Firebase with environment variables
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": os.getenv('FIREBASE_PROJECT_ID'),
    "private_key_id": os.getenv('FIREBASE_PRIVATE_KEY_ID'),
    "private_key": os.getenv('FIREBASE_PRIVATE_KEY').replace('\\n', '\n'),
    "client_email": os.getenv('FIREBASE_CLIENT_EMAIL'),
    "client_id": os.getenv('FIREBASE_CLIENT_ID'),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": os.getenv('FIREBASE_CLIENT_CERT_URL')
})

firebase_admin.initialize_app(cred)
db = firestore.client()

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, uid, email):
        self.id = uid
        self.email = email

@login_manager.user_loader
def load_user(user_id):
    user_doc = db.collection('users').document(user_id).get()
    if user_doc.exists:
        user_data = user_doc.to_dict()
        return User(user_id, user_data.get('email'))
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.get_user_by_email(email)
            user_obj = User(user.uid, user.email)
            login_user(user_obj)
            return redirect(url_for('dashboard'))
        except:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.create_user(email=email, password=password)
            db.collection('users').document(user.uid).set({
                'email': email,
                'created_at': datetime.now()
            })
            return redirect(url_for('login'))
        except:
            return render_template('register.html', error="Registration failed")
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/log-mood', methods=['POST'])
@login_required
def log_mood():
    data = request.json
    db.collection('users').document(current_user.id).collection('mood_logs').add({
        'mood': data.get('mood'),
        'triggers': data.get('triggers'),
        'cravings': data.get('cravings'),
        'timestamp': datetime.now()
    })
    return jsonify({'status': 'success'})

@app.route('/api/get-coping-strategies', methods=['GET'])
@login_required
def get_coping_strategies():
    # Mock AI analysis - in production, this would use real AI
    strategies = [
        "Take deep breaths and count to 10",
        "Call your support buddy",
        "Go for a walk",
        "Practice mindfulness meditation",
        "Write in your journal"
    ]
    return jsonify({'strategies': strategies})

@app.route('/api/get-milestones', methods=['GET'])
@login_required
def get_milestones():
    # Mock data - in production, this would come from the database
    milestones = [
        {'name': '24 Hours Sober', 'points': 100, 'completed': True},
        {'name': '1 Week Sober', 'points': 500, 'completed': False},
        {'name': '1 Month Sober', 'points': 2000, 'completed': False}
    ]
    return jsonify({'milestones': milestones})

if __name__ == '__main__':
    app.run(debug=True) 