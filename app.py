from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Please subscribe and like, comment on this video!'
