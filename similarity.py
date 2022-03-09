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


import pymongo
from pymongo import MongoClient
# import pymongo.errors as pymon_err
from dotenv import load_dotenv
import os
from zipfile import ZipFile


load_dotenv()

MONGO_URI = os.environ.get('MONGO_URI')

# creating a MongoClient object  
client = MongoClient(MONGO_URI)  

# accessing the database  
DB_NAME = 'prohost'
database = client[DB_NAME]


def display_all_projects():
    
    
    list_of_projects = []

    collection = database['project_details']
    projects = collection.find({})
        

    for project in projects:
        list_of_projects.append(project)
        

    # return list_of_projects
    final_list=[]
    for dict in list_of_projects:
        for key in dict:
            if key=="project_string":
                final_list.append(dict[key])
            else:
                continue
    # print(len(final_list))
    return final_list
    # print(list_of_projects)




# def main():

#     # get_prev_id()
#     master_list=display_all_projects()
#     length=
#     print(str1)
    



master_list=display_all_projects()
length=len(master_list)

    
# if __name__ == '__main__':  
#     main()



def check_similarity(cnt_1, cnt_2):

    cnt_1 = cnt_1.lower()
    cnt_2 = cnt_2.lower()

    nlp = spacy.load('en_core_web_sm')

    search_doc = nlp(cnt_1)

    main_doc = nlp(cnt_2)

    print(main_doc.similarity(search_doc))

def test():
    
    cnt_1 = master_list[length-1]

    for i in range(0,length-1):
        cnt_2=master_list[i]
        check_similarity(cnt_1, cnt_2)
    
if __name__ == '__main__':

    test()