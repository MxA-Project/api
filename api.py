from flask import Flask
import redis
app = Flask(__name__)

# Connect to RedisDB
redis_db = redis.StrictRedis(host='localhost', port=6379, db=0)


def get_followers_count(token):
    """ Get followers count via user's token """
    # Get the username corresponding to the token
    username = redis_db.get(token)
    if(username):
        # Get the followers count corresponding to the username
        followers_count = redis_db.hget(username, "followcount")
        if(followers_count):
            return followers_count
        return "failed to get your followers count"
    return "wrong token"


@app.route('/<token>')
def follow_count(token):
    return get_followers_count(token)
