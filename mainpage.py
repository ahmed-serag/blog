from google.appengine.ext import db
from handler import Handler
from user import User
import hashlib
import random
from string import letters


def make_salt(length = 5):
    return ''.join(random.choice(letters) for x in xrange(length))

def make_hash(name, pw, salt = None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (salt, h)

class MainPage(Handler):
    """
    handels some project main functionalities(signin, signup)
    """
    def post(self):
        if self.read_secure_cookie('user_id'):
            username= self.request.get('username')
            password= self.request.get('password')
            if(self.request.get('login')):
                if(User.by_name(username)):
                    user = User.by_name(username)
                    salt = user.password.split(',')[0]
                    if(user.password == make_hash(username, password, salt)):
                        self.login(user)
                        self.redirect('/blog')
                    else:
                        self.render("signin.html", error="wrong password")   
                else:
                    self.render("signin.html", error="User doesn't exist")
            else:
                if(User.by_name(username)):
                    self.render("signin.html", error="User already exist")
                else:
                    password = make_hash(username, password)
                    user = User(password=password, username=username)
                    user.put()
                    self.login(user)
                    self.redirect('/blog')
        else:
             self.redirect('/')

    def get(self):
        if self.read_secure_cookie('user_id'):
            self.redirect('/blog')
        else:
            self.render('signin.html')
        