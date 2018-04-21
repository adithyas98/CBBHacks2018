"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
import pymysql
from flask import Flask, render_template,request
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/hello')
def hello():
    return "Hello World!"
@app.route("/")
def index():
    return render_template("login.html")


@app.route('/login',methods=["GET","POST"])
def login():
    #Initialize the Error variable
    error=None
    #This method will allow the user to sign up and sign in to a web page
    #if the method of request is post, we will display the user page, else we will display the login page
    if request.method=='POST':
        # we want to run the check method
        if(loginCheck(request.form['username'],request.form['password'])):
            #if the user has passed in the correct credentials
            raise Exception('I know Python!')
            return url_for('index')
        else:
            error="Sorry the password or username entered was incorrect"
    return render_template("login.html",error=error)

def loginCheck(username,password):
    #We are simply going to check to see if the password and the username are the same
    return username==password




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
    
    # passhash = generate_password_hash(password)
    # cursor = conn.cursor()
    # if check_password_hash(passhash,password)

    #     cursor.execute("SELECT * from usertable where username='%s' and pass_hash='%s'" %
    #                     (username, passhash))
    #     data = cursor.fetchone()
    #     if data:
    #         return True
    #     else:
    #         return False
    cursor = conn.cursor()
    cursor.execute("SELECT pass_hash from usertable where username='%s'" % (username))
    passhash = cursor.fetchone()[0]

    return check_password_hash(passhash, password)

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

def testregistertestlogin():
    # print(valid_login('testuser', 'password')," true if testuser exists")
    print(register_user('test4', 'password'),"True if new user added, False if user exists")
    print(valid_login('test4', 'password'))






























if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
