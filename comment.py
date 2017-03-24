from google.appengine.ext import db

class Comment(db.Model):
    '''
    this is the model class for Comments
    '''
    user = db.StringProperty(required = True)
    post = db.StringProperty( required = True)
    body = db.TextProperty( required = True)
    created = db.DateTimeProperty(auto_now_add = True)

    @classmethod
    def by_id(cls, uid):
        return Comment.get_by_id(int(uid))

    @classmethod
    def by_post(cls, post):
        u = Comment.all().filter('post =', str(post)).order('-created')
        return u