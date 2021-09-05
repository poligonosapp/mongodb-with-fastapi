# https://api.mongodb.com/python/3.0/examples/authentication.html#default-authentication-mechanism

from pymongo import MongoClient

client = MongoClient('example.com')

client.the_database.authenticate('user',
                                  'password',
                                  source='source_database')
True

uri = "mongodb://user:password@example.com/?authSource=source_database"
client = MongoClient(uri)