from bottle import response, get, run
from pymongo import MongoClient
cluster = MongoClient("MONGODB HIRE")
db = cluster.posts
col = db["prod"]

@get('/api/get')
def index():
    response.set_header ("Access-Control-Allow-Origin", "*")
    o = []
    for posst in col.find():
        posst["_id"]=str(posst["_id"])
        o.append(posst)
    return {"data":o,"v":"0.1 BETA"}

run(host='0.0.0.0', port=81)
