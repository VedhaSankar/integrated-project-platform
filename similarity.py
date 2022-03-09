import spacy
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# Run:
# python -m spacy download en_core_web_sm
# the first time you run this file

# db = get_db()
# data = db.author.find_one({'email' : email, 'password' : password})
# print(data)

MONGO_URI =  os.environ.get('MONGO_URI')

#  collection_name = 'project_details'

client = MongoClient(MONGO_URI)  
DB_NAME = 'prohost'
database = client[DB_NAME]


collection_name = 'project_details'

new_collection = database[collection_name]


# # db = MongoClient.prohost()

# col = db.project_details

# details = []
# for doc in col.find():
# # append each document's ID to the list
#     details += [doc["project_string"]]

# # print out the IDs
# print ("project_string:", project_string)
# print ("total docs:", len(ids))



def check_similarity(cnt_1, cnt_2):

    cnt_1 = cnt_1.lower()
    cnt_2 = cnt_2.lower()

    nlp = spacy.load('en_core_web_sm')

    search_doc = nlp(cnt_1)

    main_doc = nlp(cnt_2)

    print(main_doc.similarity(search_doc))

def test():

    cnt_1 = '''
    Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure, resizable compute capacity in the cloud.
    '''

    cnt_2 = '''
    Amazon Elastic Compute Cloud (Amazon EC2) provides scalable computing capacity in the Amazon Web Services (AWS) Cloud. Using Amazon EC2 eliminates your need to invest in hardware up front, so you can develop and deploy applications faster.
    '''
    
    check_similarity(cnt_1, cnt_2)
    
if __name__ == '__main__':

    test()