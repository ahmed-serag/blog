from google.appengine.ext import db


def valid_pw(name, password, h):
    salt = h.split(',')[0]
    return h == make_pw_hash(name, password, salt)

class User(db.Model):
    """
    User Entity Class
    """
    password = db.StringProperty( required = True)
    username = db.StringProperty( required= True)

    @classmethod
    def by_name(cls, username):
        u = User.all().filter('username =', username).get()
        return u

    @classmethod
    def login(cls, username, password):
        u = cls.by_name(username)
        if u and valid_pw(username, password, u.password):
            return u

    @classmethod
    def by_id(cls, uid):
        return User.get_by_id(int(uid))
