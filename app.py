from flask import Flask, render_template
from redis import Redis
import os
import socket
import datetime

app = Flask(__name__)
redis = Redis(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'))

@app.route('/')
def hello():
    USER = os.getenv('USER')
    redis.incr('hits')
    counter = str(redis.get('hits'), 'utf-8')
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    utc_dt=datetime.datetime.utcnow()
    # return "Hello " + USER + "\n" + "Welcome to our Flask app with Redis!, This web page was withites " + counter + " times.\n On host " + hostname + " with ip: " + ip_addr + "\n"
    return render_template('index.html', utc_dt = utc_dt, counter = counter, hostname = hostname, ip_addr = ip_addr)

@app.route('/health')
def health():
    return "Health ok!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug = True)