from flask import Flask, request, jsonify

app = Flask(__name__)
users=[]


@app.route('/user', methods=['POST'])
def register_users():
    user = {
        "username": request.json['username'],

        "password": request.json['password']
    }
    users.append(user)
    return jsonify ({"users":users}), 201


@app.route('/login', methods=['POST'])
def login():
    user={
        "username": request.json['username'],

        "password": request.json['password']
    }


if __name__ == '__main__':
    app.run(debug=True)
