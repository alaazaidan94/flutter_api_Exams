from typing import Union
from fastapi import FastAPI
import mysql.connector
mydb = mysql.connector.connect(host="bmj7gpyrnnvddlwsuzmm-mysql.services.clever-cloud.com",
                                     user="uey0hhoxexn16bqq",
                                     password="NCPJvn5Y3ibyB6KWEHXR",
                                     database= "bmj7gpyrnnvddlwsuzmm")

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']    
)
 

@app.post("/users/addUsers")
def add_users(userName,passWord,firstName,lastName,email):
    cur = mydb.cursor()
    cur.execute(f"select username from users where username = '{userName}'")
    c = cur.fetchall()
    lst = []
    for i in c:
        lst.append(i)
    x = 0    
    if (not lst):
        x = 1
        mydb.execute(f"insert into users(username,password,firstname,lastname,email) values ('{userName}','{passWord}','{firstName}','{lastName}','{email}')")
        mydb.commit()
        mydb.close()
    else:
        x = 0
        
    return x



@app.post("/users/delUser")
def get_user(id):
    cur = mydb.cursor()
    cur.execute(f"delete from users where id = {id}")  
    mydb.commit()
    mydb.close()
    return 1

@app.get("/users")  
def getAllUser():
    cur = mydb.cursor()
    cur.execute("SELECT * from Users")
    c = cur.fetchall()
    lst_json=[]
    for i in c:
        item={}
        item["id"] = i[0]
        item["username"] = i[1]
        item["password"] = i[2]
        item["firstname"] = i[3]
        item["lastname"] = i[4]
        item["email"] = i[5]
        lst_json.append(item)
    return lst_json   


@app.get("/management")
def getManagements():
    cur = mydb.cursor()
    cur.execute("SELECT * from management")
    c = cur.fetchall()
    lst_json=[]
    for i in c:
        item={}
        item["id"] = i[0]
        item["username"] = i[1]
        item["password"] = i[2]
        lst_json.append(item)
    return lst_json  

@app.post("/management/addManagement")
def addManagement(userName,passWord):
    mydb.execute(f"INSERT INTO management(username,password) VALUES ('{userName}','{passWord}')")
    mydb.commit()
    mydb.close()
    return 1

@app.post("/management/removeManagement")
def removeManagement(id):
    cur = mydb.cursor()
    cur.execute(f"delete from management where id = {id}")  
    mydb.commit()
    mydb.close()
    return 1
    
@app.get("/questions")
def getQuestions():
    cur = mydb.cursor()
    cur.execute("SELECT * from questions")
    c = cur.fetchall()
    lst_json=[]
    for i in c:
        item={}
        item["id"] = i[0]
        item["question"] = i[1]
        item["choice1"] = i[2]
        item["choice2"] = i[3]
        item["choice3"] = i[4]
        item["choice4"] = i[5]
        item["grouperadio"] = i[6]
        lst_json.append(item)
    return lst_json  

@app.post("/questions/addQuestion")
def addQuestion(question,choice1,choice2,choice3,choice4):
    mydb.execute(f"INSERT INTO questions(question,choice1,choice2,choice3,choice4) VALUES ('{question}','{choice1}','{choice2}','{choice3}','{choice4}')")
    mydb.commit()
    mydb.close()
    return 1

@app.post("/questions/removeQuestions")
def removeQuestion(id):
    cur = mydb.cursor()
    cur.execute(f"delete from questions where id = {id}")  
    mydb.commit()
    mydb.close()
    return 1    

@app.post("/questions/updateQuestion")
def updateQuestion(id,question,choice1,choice2,choice3,choice4):
    mydb.execute(f"update questions set question = '{question}',choice1 = '{choice1}',choice2 = '{choice2}',choice3 = '{choice3}',choice4 = '{choice4}' where id = {id}")
    mydb.commit()
    mydb.close()
    return 1    
    
@app.get("/verification/manger")
def verificationManger(username,password):
    cur = mydb.cursor()
    cur.execute(f"SELECT username,password from management where username = '{username}'and password = '{password}'")
    c = cur.fetchall()
    lst_json=[]
    for i in c:
        lst_json.append(i)
    x = 0
    if (not lst_json):
        x = 0
    else:
        x = 1

    return x    

@app.get("/verification/user")
def verificationUser(username,password):
    cur = mydb.cursor()
    cur.execute(f"SELECT username,password from users where username = '{username}'and password = '{password}'")
    c = cur.fetchall()
    lst_json=[]
    for i in c:
        lst_json.append(i)
    x = 0
    if (not lst_json):
        x = 0
    else:
        x = 1

    return x  


mydb.close()

    
              
    
    
    
    
    
    
    
    
    
    
