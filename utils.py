import random
import tlogger

def get_course_id(course_id):

    course_dict = {
        "course_id" : int(course_id)
    }

    course_obj = f12_course_van.find_one(course_dict)

    return course_obj

def get_last_course_id():

    last_course_id      = f12_course_van.find().sort([('course_id', -1)]).limit(1)

    try:
        last_course_id = last_course_id[0]['course_id']
    except Exception as err:
        tlogger.info("error while getting last course_id : ", err)
        last_course_id = 0

    return last_course_id

def get_last_course_subscriber_id():

    last_course_subscriber_id      = f12_course_subscribers_van.find().sort([('course_subscriber_id', -1)]).limit(1)

    try:
        last_course_subscriber_id = last_course_subscriber_id[0]['course_subscriber_id']
    except Exception as err:
        tlogger.info("error while getting last course_subscriber_id : ", err)
        last_course_subscriber_id = 0

    return last_course_subscriber_id
