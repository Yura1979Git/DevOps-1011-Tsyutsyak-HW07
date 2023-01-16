from flask import Flask
from redis import Redis

app = Flask(__name__)
#redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    #redis.incr('hits')
    #counter = str(redis.get('hits'), 'utf-8')
    counter = "1"
    return "Welcome to our Flask app with Redis!, This web page was withites " + counter + " times"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug = True)