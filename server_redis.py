#!/usr/bin/env python
# Solution for Q2 "Jane Smith Doe"

# Using Flask for Web App
# The root endpoint "/" is for display the full name
# Three RESTful endpoint has been implemented:
# /getAFirstName
# /getAMiddleName
# /getALastName

# All the requests are finally redirected to Redis queries
# The Redis Get a Hash Table "TheName"
# and Three Hash item
# "FirstName" : "Jane"
# "MiddleName": "Smith"
# "LastName"  : "Doe"

import redis
from flask import Flask
from flask_restful import Api, Resource, reqparse

myredis = redis.Redis()

app = Flask(__name__)
api = Api(app)

# Three Resources
class FirstName(Resource):
	def get(self):
		return myredis.hget("TheName", "FirstName"), 200

	def post(self):
		return "Error", 404

	def put(self):
		return "Error", 404

	def delete(self):
		return "Error", 404

class MiddleName(Resource):
	def get(self):
		return myredis.hget("TheName", "MiddleName"), 200

	def post(self):
		return "Error", 404

	def put(self):
		return "Error", 404

	def delete(self):
		return "Error", 404

class LastName(Resource):
	def get(self):
		return myredis.hget("TheName", "LastName"), 200

	def post(self):
		return "Error", 404

	def put(self):
		return "Error", 404

	def delete(self):
		return "Error", 404

# Link to Three Endpoints
api.add_resource(FirstName, "/getAFirstName")
api.add_resource(MiddleName, "/getAMiddleName")
api.add_resource(LastName, "/getALastName")

# Root for the Web App
@app.route("/")
def getName():
	FN = myredis.hget("TheName", "FirstName")
	MN = myredis.hget("TheName", "MiddleName")
	LN = myredis.hget("TheName", "LastName")
	return "%s %s %s" % (FN, MN, LN)

# Allow All
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
