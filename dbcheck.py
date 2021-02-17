from passlib.hash import pbkdf2_sha256
from mysql import connector

    
    

def insert(d): 
    conn = connector.connect(host="localhost",user="root" ,password="Rupam2000$",database="taskdb")
    insert_query = "INSERT INTO user(username,Name,password ,email) VALUES(%s , %s , %s , %s);"
    d["password"] = pbkdf2_sha256.hash(d["password"])
    val = (d["user"] , d["name"] ,d["password"] , d["email"])
    mycursor = conn.cursor()
    mycursor.execute(insert_query , val) 
    conn.commit()
    conn.close()
    
    
    
    
def check(user):
    
    d = {}
    conn = connector.connect(host="localhost",user="root" ,password="Rupam2000$",database="taskdb")
    select_userquery = "SELECT * FROM user WHERE username = %s OR email = %s ;"
    select_activity  = "SELECT * FROM activity WHERE user = %s ;"
    val1 = (user , user) 
    val2 = (user ,)
    mycursor = conn.cursor()
    
    mycursor.execute(select_userquery , val1)
    ls = []
    for x in mycursor:
        ls.append(x)
        
    mycursor.execute(select_activity , val2)
    ls1 = []
    for x in mycursor:
        ls1.append(x)
        
    if len(ls) > 0:
        d["name"] =  ls[0][1]
         
        d["user"] = ls[0][0]
        d["password"] = ls[0][2]
        d["email"] = ls[0][3]
        d["activity"]= ls1
        return d
        
    else:
        return -1
    conn.close()
        
        
def update_activity(username , activity):
    
    conn = connector.connect(host="localhost",user="root" ,password="Rupam2000$",database="taskdb")
    insert_query = "INSERT INTO activity(Taskname , Urgency ,Deadline ,user) VALUES(%s , %s , %s , %s);"
    
    val = (activity["task"] , activity["urgency"] ,activity["deadline"] ,username)
    mycursor = conn.cursor()
    mycursor.execute(insert_query , val) 
    conn.commit()
    conn.close()
    
    
def delete_activity(username , index):
    conn = connector.connect(host="localhost",user="root" ,password="Rupam2000$",database="taskdb")
    delete_query = "DELETE FROM activity WHERE user=%s AND id = %s;"
    
    
    val = (username , index)
    mycursor = conn.cursor()
    mycursor.execute(delete_query , val) 
    conn.commit()
    conn.close()
    
def update_password(user , password):
    conn = connector.connect(host="localhost",user="root" ,password="Rupam2000$",database="taskdb")
    password = pbkdf2_sha256.hash(password)
    update_query = "UPDATE user SET password = %s WHERE  username = %s;"
    
    val = (password , user)
    mycursor = conn.cursor()
    mycursor.execute(update_query , val) 
    conn.commit()
    conn.close()
    
def pushotp(user , otp):
    conn = connector.connect(host="localhost",user="root" ,password="Rupam2000$",database="taskdb")
    push = "INSERT INTO userotp(user , otp) VALUES(%s , %s);" 
    val = (user , otp)
    mycursor = conn.cursor()
    mycursor.execute(push , val) 
    conn.commit()
    conn.close()
    
def getotp(user):
    conn = connector.connect(host="localhost",user="root" ,password="Rupam2000$",database="taskdb")
    select = "SELECT otp FROM userotp WHERE user = %s ;" 
    val = (user , )
    mycursor = conn.cursor()
    mycursor.execute(select , val)
    ls = []
    for x in mycursor:
        ls.append(x)
        
    if(len(ls) == 0):
        conn.close()
        return None
    else:
        otp = ls[0][0]
        conn.close()
        return otp  
    
def popotp(user):
    conn = connector.connect(host="localhost",user="root" ,password="Rupam2000$",database="taskdb")
    delete = "DELETE FROM userotp WHERE user = %s ;" 
    val = (user , )
    mycursor = conn.cursor()
    mycursor.execute(delete , val) 
    conn.commit()
    conn.close()
    
    
    

    
    
    
    
    
if __name__ == '__main__': 
    print(check('prasad'))