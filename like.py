from google.appengine.ext import db

class Like(db.Model):
    user = db.IntegerProperty(required = True)
    post = db.IntegerProperty( required = True)
 
    @classmethod
    def by_id(cls, uid):
        return Like.get_by_id(int(uid))
