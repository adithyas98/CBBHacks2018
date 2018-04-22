import pymysql
from flask import Flask, render_template,request

class studySession:

    users = []
    data = []
    #initializes a studySession object
    #subject: course (e.g. MA253)
    #username: host student's username
    #time: time of session
    #date: date of session
    #location: where the session is conducted
    def __init__(self, subject, username, time, date, location):
        app = Flask(__name__)
        # Make the WSGI interface available at the top level so wfastcgi can get it.
        wsgi_app = app.wsgi_app

        self.subject = subject
        self.username = username
        self.time = time
        self.date = date
        self.location = location


        #mysql
        MYSQL_DATABASE_HOST = '35.184.37.128'
        MYSQL_DATABASE_USER = 'cbbroot'
        MYSQL_DATABASE_PASSWORD = 'studyu'
        MYSQL_DATABASE_DB = 'userdb'
        conn = pymysql.connect(
            host=MYSQL_DATABASE_HOST, 
            user=MYSQL_DATABASE_USER, 
            passwd=MYSQL_DATABASE_PASSWORD, 
            db=MYSQL_DATABASE_DB)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `sessions` (`subject`, `username`, `time`, `date`, `location`) VALUES ( '%s', '%s','%s','%s','%s');" %
                        (self.subject, self.username, self.time, self.date, self.location))
        data = cursor.fetchone()
        conn.commit()
        self.users.add(self.username)
        data.add(self.subject, users, self.time, self.date, self.location)


    #string representation of the studySession object
    def toString(self):
        return self.subject + " " + self.username + " " + self.time + " " + self.date + " "+ self.location
    
    #add a new user to an existing study session
    def join(self, newUser):
        MYSQL_DATABASE_HOST = '35.184.37.128'
        MYSQL_DATABASE_USER = 'cbbroot'
        MYSQL_DATABASE_PASSWORD = 'studyu'
        MYSQL_DATABASE_DB = 'userdb'
        conn = pymysql.connect(
            host=MYSQL_DATABASE_HOST, 
            user=MYSQL_DATABASE_USER, 
            passwd=MYSQL_DATABASE_PASSWORD, 
            db=MYSQL_DATABASE_DB)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `sessions` (`subject`, `username`, `time`, `date`, `location`) VALUES ( '%s', '%s','%s','%s');" %
                        (self.subject, newUser, self.time, self.date, self.location))
        conn.commit()
        self.users.add(newUser)
        

#create a new session
#subject: course (e.g. MA253)
#username: host student's username
#time: timestamp of studySession
#date: date of session
#location: where the session is conducted
def newSession(subject, username, time, date, location):
    #mysql
    MYSQL_DATABASE_HOST = '35.184.37.128'
    MYSQL_DATABASE_USER = 'cbbroot'
    MYSQL_DATABASE_PASSWORD = 'studyu'
    MYSQL_DATABASE_DB = 'userdb'
    conn = pymysql.connect(
        host=MYSQL_DATABASE_HOST, 
        user=MYSQL_DATABASE_USER, 
        passwd=MYSQL_DATABASE_PASSWORD, 
        db=MYSQL_DATABASE_DB)

    cursor = conn.cursor()
    # check if session already exists
    cursor.execute("SELECT * FROM sessions WHERE subject = `%s` and time = `%s` and date = `%s' and location = `%s`" %
                    (subject, username, time, date, location))
    data = cursor.fetchone()
    if not data:
        session = studySession(subject, username, time, date, location)
        return session
    else:
        return False

#add a user to an existing session
def joinSession(session, username):
    # MYSQL_DATABASE_HOST = '35.184.37.128'
    # MYSQL_DATABASE_USER = 'cbbroot'
    # MYSQL_DATABASE_PASSWORD = 'studyu'
    # MYSQL_DATABASE_DB = 'userdb'
    # conn = pymysql.connect(
    #     host=MYSQL_DATABASE_HOST, 
    #     user=MYSQL_DATABASE_USER, 
    #     passwd=MYSQL_DATABASE_PASSWORD, 
    #     db=MYSQL_DATABASE_DB)

    # cursor = conn.cursor()
    # # check if sessions already exists
    # cursor.execute("SELECT * FROM sessions WHERE subject = `%s` and usernameand time = `%s` and location = `%s`" %
    #                 (session.subject, session.username, session.time, session.location))
    # data = cursor.fetchone()
    # if not data:
    #     session = studySession(subject, username, time, location)
    #     return True
    # else:
    #     return False
    if username in session.users:
        return False
    else:
        session.join(username)
        return True

#search function
def search(query):
    MYSQL_DATABASE_HOST = '35.184.37.128'
    MYSQL_DATABASE_USER = 'cbbroot'
    MYSQL_DATABASE_PASSWORD = 'studyu'
    MYSQL_DATABASE_DB = 'userdb'
    conn = pymysql.connect(
        host=MYSQL_DATABASE_HOST, 
        user=MYSQL_DATABASE_USER, 
        passwd=MYSQL_DATABASE_PASSWORD, 
        db=MYSQL_DATABASE_DB)
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sessions WHERE subject = '%s'" %
                    (query))
    data = cursor.fetchall()
    return data

#test function
def test():
    # print(addSession("MA253", "testuser1","2018-04-21 08:30:00", "Davis 217"))
    # print(addSession("MA253", "testuser2","2018-04-21 08:30:00", "Davis 217"))
    # print(addSession("MA253", "testuser3","2018-04-21 08:30:00", "Davis 217"))
    # print(addSession("MA253", "testuser4","2018-04-21 08:30:00", "Davis 217"))
    # print(addSession("CS231", "Trisha","2018-04-25 20:45:00", "Miller Street"))
    # print(addSession("CS231", "Caleb","2018-04-25 20:45:00", "Miller Street"))
    # print(addSession("CS231", "Gautam","2018-04-25 20:45:00", "Miller Street"))


    #SQL query for any individual session:
    #SELECT * FROM sessions WHERE subject = "session.subject" and time = "session.time" and location = "session.location";

    # session1 = studySession("MA253", "testuser1","2018-04-21 08:30:00", "Davis 217")
    # session1.join("testUser2")
    # session1.join("testUser3")
    # session1.join("testUser4")
    # print(session1.toString())

    print(search('MA253'))
    print(type(search('MA253')))

    # session2 = studySession("CS231", "Trisha","2018-04-25 20:45:00", "Miller Street")
    # session2.join("Caleb")
    # session2.join("Gautam")
    # print(session2.toString())


if __name__ == '__main__':
    test()