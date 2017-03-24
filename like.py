from google.appengine.ext import db
from handler import Handler

class Like(db.Model):
    '''
    this is the model class for likes
    '''
    user = db.StringProperty(required = True)
    post = db.StringProperty( required = True)
    value = db.IntegerProperty( required = True)
    @classmethod
    def by_id(cls, uid):
        return Like.get_by_id(int(uid))

    @classmethod
    def by_post(cls, post):
        u = Like.all().filter('post =', post)
        return u
    @classmethod
    def by_post_user(cls, post, user):
        u = Like.all().filter('post =', str(post))
        q = u.filter('user =', str(user))
        return q



