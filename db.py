import pymongo
from pymongo import MongoClient

class Ecampusdb(object):
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.ecampus

    def insert(self,data):
        self.db.faq.insert_one(data)
    
    def findAll(self,question_keyword):
        cursor = self.db.faq.find({})
        print ("cursor",cursor)
        max_hit =0
        
        for document in cursor:
            print ("document",document)
            keywords = document["keywords"]
            result = []
            hit = 0
            for que in question_keyword:
                print (que,"que")
                if que in keywords:
                    print ("yes")
                    result.append(que)
                    hit += 1

            if hit > max_hit:
                text = document["text"]
                max_hit = hit
        print ((max_hit/len(question_keyword)))


        if (max_hit/len(question_keyword))*100 >= 50.00:
            return text
        else:
            return "Sorry ! I do not understand. Please email your query at ecampus@sjsu.edu"

