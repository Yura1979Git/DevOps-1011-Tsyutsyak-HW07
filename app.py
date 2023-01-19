from flask import Flask
from redis import Redis
import os
import socket

app = Flask(__name__)
redis = Redis(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'))

@app.route('/')
def hello():
    USER = os.getenv('USER')
    redis.incr('hits')
    counter = str(redis.get('hits'), 'utf-8')
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    return "Hello " + USER + "\n" + "Welcome to our Flask app with Redis!, This web page was withites " + counter + " times.\n On host " + hostname + "with ip: " + ip_addr + "\n"

@app.route('/health')
def health():
    return "Health ok!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug = True)