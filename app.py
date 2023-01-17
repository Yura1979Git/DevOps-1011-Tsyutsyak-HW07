from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    USER = os.getenv('USER')
    redis.incr('hits')
    counter = str(redis.get('hits'), 'utf-8')
    return "Hello " + USER + "\n" + "Welcome to our Flask app with Redis!, This web page was withites " + counter + " times.\n"

@app.route('/health')
def health():
    return "Health ok!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug = True)