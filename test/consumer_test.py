import unittest
import json
import sys
sys.path.append('src/Consumer/')
import pika
from consumer import Consumer
'''
Note - unittest module expects that method names start with test_
ex: test_return_formatted_url
'''

class Consumer_Pipeline(unittest.TestCase):
	""" test suit class """

	def test_rabbitmq_init(self):
		print("Sahil1")
		self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
		self.channel = self.connection.channel()
		self.channel.queue_declare(queue= 'test_queue')


	def test_length_of_content(self):
		message = Consumer("bus", "localhost")
		print("Sahil")
		string = message.pull_message()
		assert len(string) > 0
	

		
if __name__ == '__main__':
	unittest.main()