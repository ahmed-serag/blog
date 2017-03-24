from google.appengine.ext import db
from handler import Handler
from user import User
from comment import Comment
from like import Like
class Post(db.Model):
    '''
    thi is the post model
    '''
    user = db.StringProperty(required = True)
    title = db.StringProperty( required = True)
    body = db.TextProperty( required = True)
    created = db.DateTimeProperty(auto_now_add = True)

    @classmethod
    def by_id(cls, uid):
        return Post.get_by_id(int(uid))

class postDeleteHandler(Handler):
    '''
    this handler is  for handel delete post requests and it's likes and comments from the datastore 
    '''
    def get(self,post_id):
        if self.read_secure_cookie('user_id'):
            post = Post.by_id(post_id)
            if post:
                if post.user == User.by_id(self.read_secure_cookie('user_id')).username:
                    post.delete()
                    if Comment.by_post(post_id).get():
                        for comment in Comment.by_post(post_id):
                            comment.delete()
                    if Like.by_post(post_id).get():
                        for like in Like.by_post(post_id):
                            like.delete()                    
            self.redirect('/blog')
            
        else:
            self.redirect('/')
