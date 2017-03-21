from google.appengine.ext import db

class Comment(db.Model):
    user = db.IntegerProperty(required = True)
    post = db.IntegerProperty( required = True)
    body = db.TextProperty( required = True)

    @classmethod
    def by_id(cls, uid):
        return Comment.get_by_id(int(uid))
