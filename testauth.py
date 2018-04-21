"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template,request
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app





def valid_login(username, password):
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
    
    passhash = generate_password_hash(password)
    cursor = conn.cursor()
    if check_password_hash(passhash,password)

        cursor.execute("SELECT * from usertable where username='%s' and pass_hash='%s'" %
                        (username, passhash))
        data = cursor.fetchone()
        if data:
            return True
        else:
            return False

def register_user(username, password):
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
    # check if username alr exists
    cursor.execute("SELECT * from usertable where username='%s'" %
                    (username))
    data = cursor.fetchone()
    if not data:
        cursor.execute("INSERT INTO `usertable` (`username`,`password`, `pass_hash`) VALUES ('%s', '%s', '%s');" %
                    (username, password, generate_password_hash(password)))
        conn.commit()
        return True
    else:
        return False

    # cursor.execute("INSERT INTO `usertable` (`username`,`password`) VALUES ('%s', '%s');" %
    #                 (username, password))
    # conn.commit()

def test():
    # print(valid_login('testuser', 'password')," true if testuser exists")
    print(register_user('test4', 'password'),"True if new user added, False if user exists")
    print(valid_login('test4', 'password'))




if __name__ == '__main__':
    test()