from pymongo import MongoClient
from pprint import pprint
# 방법1 - URI
mongodb_URI = "mongodb://localhost:27017/"
client = MongoClient(mongodb_URI)

# 방법2 - HOST, PORT
# client = MongoClient(host='localhost', port=27017)

print(client)
# pprint(client.__dict__)
print(client.list_database_names())


#db.py

# import pymongo


# conn = pymongo.MongoClient()

# print(conn)
# print()
# db_name = 'rocketchat'
# print(conn.list_database)
# db = conn.get_database(db_name)
# # print(db)




# print(conn_defsault)
# db = conn.rocketchat
# print(db)
# print()
# coll = db.get_collection('users')
# results = coll.find()

# print(results)
# db = client.newDB 			# db 를 하나 만들고
# userCollection = db.user	# db 에서 collection 을 만든다.

# # insert_one() 으로 db 를 추가
# userCollection.insert_one({
#     'name' : 'mik_a',
#     'age'  : '100',
# })

# # find() 로 collection 에 저장된 데이터를 불러와서 출력한다
# for i in userCollection.find() :
#     print(i)

# # collection 의 데이터를 전부 삭제한다.
# userCollection.delete_many({})


# from pymongo import MongoClient, errors

# # global variables for MongoDB host (default port is 27017)
# DOMAIN = 'mongodb://localhost'
# PORT = 27017

# # use a try-except indentation to catch MongoClient() errors

# # try to instantiate a client instance
# client = MongoClient(
#     host = [ str(DOMAIN) + ":" + str(PORT) ],
#     serverSelectionTimeoutMS = 3000, # 3 second timeout,
# )

# # print the version of MongoDB server if connection successful
# print ("server version:", client.server_info()["version"])

# # get the database_names from the MongoClient()
# database_names = client.list_database