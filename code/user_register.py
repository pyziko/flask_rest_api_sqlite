import sqlite3

from flask_restful import Resource, reqparse

from user import User


class UserRegister(Resource):  # todo INFO: remember to add it as a resource
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="This field cannot be left blank")
    parser.add_argument("password", type=str, required=True, help="This field cannot be left blank")

    def post(self) -> tuple[dict[str, str], int]:

        data = UserRegister.parser.parse_args()

        if User.find_by_username(data["username"]):
            return {"message": "User with username '{}' already exists".format(data["username"])}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users Values(NULL, ?, ?)"  # id is automatically generated
        cursor.execute(query, (data["username"], data["password"]))  # remember it must be a tuple

        connection.commit()
        connection.close()

        return {"message": "User created successfully"}, 201
