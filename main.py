from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/av"
mongo = PyMongo(app)
api = Api(app)


class Register(Resource):
     def post(self):

         # user = mongo.db.user_details

         name = request.json['name']
         email = request.json['email']
         password = request.json['password']
         id = mongo.db.user_details.insert({"name": name, "email": email, "password": password})

         # is_exist = user.find_one({'email': email}, {'_id': 0, 'email': 1})
         # is_exist = is_exist.get('email')
         # print(is_exist)=i
         if id is None:
             return jsonify({'msg': 'user is not inserted'})
         else:
             # if email == mongo.db.user_details.get('email'):
             #     return jsonify({'msg': 'Email already registered. Please register using another email.'})
             # else:
             return jsonify({'msg': 'user inserted successfully'})

         # id = user.insert({"email": email, "password": password})
            # # print(id)
            # if id is None:




         # else:
             # return jsonify({'msg': 'user already exists'})

class Display_users(Resource):
    def get(self):
        # user = mongo.db.user_details
        output = []
        for all_data in mongo.db.user_details.find():
            # print(all_data)

            output.append({"Name": all_data['name'], "Email": all_data["email"]})   #all_data is acting as a i in for loop
        return jsonify({"result": output})

class Login_user(Resource):
    def post(self):
        # user = mongo.db.user_details
        email = request.json['email']
        password = request.json['password']
        login_user = mongo.db.user_details.find_one({"email": email}, {'_id': 0, 'email': 1, 'password': 1})
        # print(login_user)
        if login_user is None:
            return jsonify({'msg': 'user does not exist'})
        else:
            if password == login_user.get('password'):
                # print(password)
                return jsonify({'msg': 'user login successful'})
            else:
                return jsonify({'msg': 'Invalid Password '})
class Reset_pass(Resource):
    def post(self):
        email = request.json['email']
        current_password = request.json['current_password']
        # print(current_password)
        new_password = request.json['new_password']
        # print(new_password)

        find_user = mongo.db.user_details.find_one({"email": email}, {'_id': 0, 'email': 1, 'password': 1})
        if find_user is None:
            return jsonify({'msg': 'User does not exist'})
        else:
            if find_user['password'] == current_password:
                # is_updated =

                mongo.db.user_details.update({'password': current_password}, {'$set': {'password': new_password}})

                # print(is_updated)

                return jsonify({'msg': 'password is updated successfully'})
            else:
                return jsonify({'msg': 'password is not updated'})


api.add_resource(Register, "/register")
api.add_resource(Display_users, "/display")
api.add_resource(Login_user, "/login")
api.add_resource(Reset_pass, '/resetpass')

if __name__ == '__main__':   #from here the atual program starts
    app.run(host='0.0.0.0', debug=True, port=8100)