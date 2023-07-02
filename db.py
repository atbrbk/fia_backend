import mysql.connector as mysql

class DB:
    def __init__(self):
        self.db = mysql.connect(
            host='db4free.net',
            user='fia_admin',
            password='f4ef91557b471aa8dd4eb32e772a9873b49be455',
            database='fia_data',
            port='3306',
            # connect_timeout=180,
        )
        self.cursor = self.db.cursor()

    def create_user(self, login, password, role, name, birth_date, school, degree):
        if self.cursor:
            password = generate_password_hash(password)
            self.cursor.execute(f'INSERT INTO users (`login`, `password`, `role`, `name`, `school`, `degree`) VALUES ("{login}", "{password}", "{role}", "{name}", "{school}", "{degree}")')
            self.db.commit()
            return self.cursor.rowcount
        return

    def check_password(self, login, password, role):
        if self.cursor:
            self.cursor.execute(f'SELECT id, password FROM users WHERE login="{login}" AND role="{role}"')
            data = self.cursor.fetchall()
            if len(data) > 0:
                u_pass = data[0][1]
                if check_password_hash(u_pass, password):
                    return data[0][0]
        return False

    def create_school(self, user_id, name, description, address1, address2, city, state, country):
        if self.cursor:
            self.cursor.execute(f"INSERT INTO schools (user_id, name, description, address1, address2, city, state, country) VALUES ('{user_id}', '{name}', '{description}', '{address1}', '{address2}', '{city}', '{state}', '{country}')")
            data = self.cursor.fetchall()
            print(data)
        return

    def create_event(self, user_id, school_id, name, desc, subject, start_date, start_time, end_date, end_time, address1, address2, city, state, country):
        if self.cursor:
            self.cursor.execute(f"INSERT INTO events (user_id, school_id, name, desc, subject, start_date, start_time, end_date, end_time, address1, address2, city, state, country) VALUES ('{user_id}', '{school_id}', '{name}', '{desc}', '{subject}', '{start_date}', '{start_time}', '{end_date}', '{end_time}', '{address1}', '{address2}', '{city}', '{state}', '{country}')")
            data = self.cursor.fetchall()
            print(data)
        return result

    def get_events(self, school_id):
        result = []
        if self.cursor:
            self.cursor.execute(f'SELECT * FROM events WHERE school_id="{school_id}"')
            data = self.cursor.fetchall()
            for item in data:
                item_data = {
                    'name':item[0], 
                    'desc':item[1], 
                    'subject':item[2], 
                    'start_date':item[3], 
                    'start_time':item[4], 
                    'end_date':item[5], 
                    'end_time':item[6], 
                    'address1':item[7], 
                    'address2':item[8], 
                    'city':item[9], 
                    'state':item[10], 
                    'country':item[11],#.decode('utf-8'),
                }
                result.append(item_data)
        return False
