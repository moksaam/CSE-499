from pymongo import MongoClient

client = MongoClient("mongodb+srv://test_user:testasNM0103!@cluster0.kkkfb.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

char_collection.insert_one({
    
})


try:
 
    print("MongoDB version is %s" %
 
            client.server_info()['version'])
 
except pymongo.errors.OperationFailure as error:
 
    print(error)
 
    quit(1)