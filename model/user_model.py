import mysql.connector
import json
from flask import make_response, jsonify

class user_model():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost",user="root",password="",database="irisdata")
            self.con.autocommit=True
            self.cur = self.con.cursor(dictionary=True)
            
            print("Connection Sucessful")
        except:
            print("Error")

    def user_getall_model(self):
        #Business logic
        self.cur.execute("Select * from iris")
        result = self.cur.fetchall()
        if len(result)>0 :
            res = make_response({"payload":result},200)
            res.headers['Access-Control-Allow-Origin']="*"
            return res
        else:
            return  make_response({"message":"No Data Found"},201)


    def user_addone_model(self,data):
        self.cur.execute(f"INSERT INTO iris(sepal_length, sepal_width, petal_length, petal_width, species) VALUES('{data['sepal_length']}', '{data['sepal_width']}', '{data['petal_length']}', '{data['petal_width']}', '{data['species']}')")
        return make_response({"message":"CREATED_SUCCESSFULLY"},201)

    def add_multiple_users_model(self, dataa):
        # Generating query for multiple inserts
        qry = "INSERT INTO iris(sepal_length, sepal_width, petal_length, petal_width, species) VALUES "
        for data in dataa:
            qry += f" {data['sepal_length']}', '{data['sepal_width']}', '{data['petal_length']}', '{data['petal_width']}', '{data['species']}'),"
        finalqry = qry.rstrip(",")
        self.cur.execute(finalqry)
        return make_response({"message":"CREATED_SUCCESSFULLY"},201)