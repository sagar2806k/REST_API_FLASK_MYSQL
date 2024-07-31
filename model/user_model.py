import mysql.connector
import json
from flask import make_response

#### DataBase connector ####

class user_model():
    def __init__(self):
        try:
          self.con=mysql.connector.connect(host="localhost",user="root",password="",database="flask_tutorial")
          self.con.autocommit=True
          self.cur = self.con.cursor(dictionary=True)
          print("Connection sucessfully established")
        except:
            print("Database Connection Error")

#### GET Method #####

    def user_getall_model(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        print(result)
        #return json.dumps(result)
        return {"payload": result}

#### POST Method ####

    def user_addone_model(self,data):
        self.cur.execute(f"INSERT INTO users(Name, Email, Phone, Role, Password) VALUES('{data['Name']}', '{data['Email']}', '{data['Phone']}', '{data['Role']}', '{data['Password']}')")
        #print(data['Name'])
        #return "User created successfully"
        return make_response({"message":"CREATED_SUCCESSFULLY"},201)

#### PUT(UPDATE) Method ####
    
    def user_update_model(self,data):
        self.cur.execute(f"UPDATE users SET Name ='{data['Name']}',Email='{data['Email']}',Phone='{data['Phone']}',Role='{data['Role']}',Password='{data['Password']}' WHERE ID={data['ID']}")
        if self.cur.rowcount > 3:
              #return "User updated successfully"
              return make_response({"message":"UPDATED_SUCCESSFULLY"},201)
        else:
            #return "No user found with this ID"
             return make_response({"message":"NOTHING_TO_UPDATE"},204)

#### DELETE Method ####

    def user_delete_model(self,ID):
        self.cur.execute(f"DELETE FROM users WHERE ID={ID}")
        if self.cur.rowcount > 0:
              #return "User DELETED successfully"
              return make_response({"message":"DELETED_SUCCESSFULLY"},202)
        else:
            #return "Nothing to delete"
            return make_response({"message":"CONTACT_DEVELOPER"},500)
