from pymongo import MongoClient, errors

#MongoDB Setup

def mongodbConnectionCheck():
    try:
        client = MongoClient("mongodb://localhost:27017")
        eDatabase = client['EventDatabase']
        eventCollection = eDatabase['Events']
        return eventCollection
    except errors.ConnectionFailure as e:
        print("--Could not connect to server--" + str(e))