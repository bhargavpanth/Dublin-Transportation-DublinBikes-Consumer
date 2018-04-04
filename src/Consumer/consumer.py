
import pika
import json
import datetime
import time
import numpy as np
import os
import ast
from pymongo import MongoClient
import time
import datetime, json

class Consumer:

	def __init__(self, flag, host):
		self.flag = flag
		self.host = host

	def pull_message(self):
		connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
		channel = connection.channel()
		channel.queue_declare(queue=str(self.flag))
		# channel.basic_consume(self.callback, queue=str(self.flag), no_ack=True)
		channel.basic_consume(self.callback, queue=str(self.flag), no_ack=True)
		message = channel.start_consuming()
		return message

	def callback(self, ch, method, properties, body):
		values = json.loads(body)
		del values["status"]
		del values["contract_name"]
		del values["bonus"]
		del values["banking"]
		del values["address"]
		print values
		self.pushToMongo(values)	
		#print essential_data
		
		#return essential_data
			# pass
			# print(" [x] Received %r" % body)
	def pushToMongo(self, dataToBePushed):
		type(dataToBePushed)
		client = MongoClient('localhost', 27017)
		db = client['bikes']
		posts = db.bikes_primary
		posts2 = db.bikes_update
		post = dataToBePushed
		# print "----------------"
		print type(post)
		post_id = posts.insert_one(post).inserted_id
		post_id2 = posts2.find_one_and_update({'number': dataToBePushed['number']}, {'$set': {'name':dataToBePushed['name'],'bike_stands':dataToBePushed['bike_stands'],'last_update':dataToBePushed['last_update'], 'available_bike_stands':dataToBePushed['available_bike_stands'], 'available_bikes':dataToBePushed['available_bikes'],'position':dataToBePushed['position']}}, upsert = True)
		print post_id
		print '----'
		print post_id2




	def terminate_connection(self):
		self.connection.close()

