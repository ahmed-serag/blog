from google.appengine.ext import db

class Post(db.Model):
    user = db.StringProperty(required = True)
    title = db.StringProperty( required = True)
    body = db.StringProperty( required = True)
    created = db.DateTimeProperty(auto_now_add = True)


    @classmethod
    def by_id(cls, uid):
        return Post.get_by_id(int(uid))
