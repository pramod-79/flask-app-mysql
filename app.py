from flask import Flask
from datetime import datetime  # Ensure this import is present
app = Flask(__name__)

@app.route('/')
def hello_world():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return f'Hello! The current date and time is: {current_time}'
@app.route('/health')
def health():
    return 'Server is up and running'
