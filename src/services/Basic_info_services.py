import pathlib,sys

root_path = pathlib.Path(__file__).parent.resolve().parent.resolve()
sys.path.append(str(root_path))

from flask import Flask,request
import json
import yaml 
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dao import basic
import re
import threading,time

app = Flask('__name__')

def get_db_connection():
    
    Session = sessionmaker(bind=db_engine) #Session ->var
    return Session() 

@app.route('/student',methods = ['GET'])
def get_details():

    res = {
        'status' : 'success',
        'message' : None,
        'data' : None
    }

    try:
        connection = get_db_connection()
        student = basic.get_student_info(connection)
        res['data'] = student
    
    except Exception as e:
        res['status'] = 'failure'
        res['message'] = 'process failed'
    
    return json.dumps(res)
def a(n=0):
    while True:
        n=n+1
        print(n)
        time.sleep(1)
#insert
@app.route('/student/new' , methods = ['POST'])
def student_new():

    res = {
        'status' : 'sucess',
        'message' : None,
        'data' : None
    }
    try:
        input = request.get_json(force=True)
        if 'id' not in input:
            res['status'] : 'failure'
            res['message'] : 'No student id given'
        elif 'name' not in  input:
            res['status'] = 'failure'
            res['message'] = 'No student name given'
        elif not re.match('^\d{1,3}$',str(input['course_id'])):
            res['status'] = 'failuer'
            res['message'] = 'Invalid subject_id given'
        else :
            connection = get_db_connection()
            res['data'] = basic.student(
                id = int(input['id']),
                name = input['name'],
                course_id = int(input['course_id']),
                connection = connection
            )
    except Exception as e:
        print(str(e))
        res['status'] = 'failuer'
        res['message'] = 'unable to get the student detail'

    return json.dumps(res)
    
def dec():
    for i in range(10):
        print(i)
        time.sleep(1)


conf = yaml.load(open(os.path.join(root_path,"..","config" , "conf.yml")))
                                     #src ..->befor file 
db_engine = create_engine(conf['db_connection_string'],pool_size=50,isolation_level="READ COMMITTED",echo=True)

t = threading.Thread(target=a,args=(100,))
t.daemon=True
t.start()
dec()

#app.run('localhost' , 5000)