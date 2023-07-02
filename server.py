import db
from flask import Flask, Response
import json

app = Flask(__name__)

DB = db.DB()

@app.route('/')
def index():
    c_list = DB.get_events()
    return return_json_response(c_list)


@app.route('/login')
def login():
    try:
        json_data = request.get_json()

        if json_data == None:
            raise Exception('Data is empty!')

        login = json_data.get("login")
        password = json_data.get("password")
        role = json_data.get("role")

        uid = DB.check_password(login, password, role)
        assert type(id) == str or type(id) == int, 'Invalid email or password.'

        resp = {
            "uid": uid,
        }

        return return_json_response(resp)

    except Exception as ex:
        return return_failed_response(ex)


@app.route('/register')
def register():
    try:
        json_data = request.get_json()

        if json_data == None:
            raise Exception('Data is empty!')

        login = json_data.get("login")
        password = json_data.get("password")
        role = json_data.get("role")
        name = json_data.get("name")
        birth_date = json_data.get("birth_date")
        school = json_data.get("school")
        degree = json_data.get("degree")

        flag = DB.create_user(login, password, role, name, birth_date, school, degree)
        assert flag, 'Invalid data.'

        resp = {
            "msg": 'registered',
        }

        return return_json_response(resp)

    except Exception as ex:
        return return_failed_response(ex)


@app.route('/create_school_data')
def create_school_data():
    try:
        json_data = request.get_json()

        if json_data == None:
            raise Exception('Data is empty!')

        user_id = json_data.get("user_id")
        name = json_data.get("name")
        description = json_data.get("description")
        address1 = json_data.get("address1")
        address2 = json_data.get("address2")
        city = json_data.get("city")
        state = json_data.get("state")
        country = json_data.get("country")

        flag = DB.create_school(user_id, name, description, address1, address2, city, state, country)
        assert flag, 'Invalid data.'

        resp = {
            "msg": 'created',
        }

        return return_json_response(resp)

    except Exception as ex:
        return return_failed_response(ex)


@app.route('/create_event')
def create_event():
    try:
        json_data = request.get_json()

        if json_data == None:
            raise Exception('Data is empty!')

        user_id = json_data.get("user_id")
        school_id = json_data.get("school_id")
        name = json_data.get("name")
        description = json_data.get("description")
        subject = json_data.get("subject")
        start_date = json_data.get("start_date")
        start_time = json_data.get("start_time")
        end_date = json_data.get("end_date")
        end_time = json_data.get("end_time")
        address2 = json_data.get("address2")
        city = json_data.get("city")
        state = json_data.get("state")
        country = json_data.get("country")

        flag = DB.create_event(user_id, school_id, name, description, subject, start_date, start_time, end_date, end_time, address1, address2, city, state, country)
        assert flag, 'Invalid data.'

        resp = {
            "msg": 'created',
        }

        return return_json_response(resp)

    except Exception as ex:
        return return_failed_response(ex)


@app.route('/get_events')
def get_events():
    try:
        json_data = request.get_json()

        if json_data == None:
            raise Exception('Data is empty!')

        school_id = json_data.get("school_id")

        resp = DB.get_events(school_id)

        return return_json_response(resp)

    except Exception as ex:
        return return_failed_response(ex)


def dump_json(passed_json):
    return json.dumps(passed_json, indent=4, sort_keys=True, default=str)

def return_json_response(json):
    return Response(dump_json(json),
        status=200, mimetype='application/json')

def return_failed_response(ex):
    return Response(dump_json({"error": ex}),
        status=500, mimetype='application/json')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
