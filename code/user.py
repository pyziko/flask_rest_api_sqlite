import sqlite3


class User:
    def __init__(self, _id, username, password):  # we are using _id because id is a python keyword
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * from users WHERE username=?"
        result = cursor.execute(query, (username,))  # todo INFO: parameters have to be in form a tuple
        row = result.fetchone()
        user = cls(*row) if row else None  # *row ==>> row[0], row[1], row[2]

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * from users WHERE id=?"
        result = cursor.execute(query, (_id,))  # todo INFO: parameters have to be in form a tuple
        row = result.fetchone()
        user = cls(*row) if row else None  # *row ==>> row[0], row[1], row[2]

        connection.close()
        return user
