from google.appengine.ext import db
from handler import Handler
class Like(db.Model):
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



class LikeHandler(Handler):
    def get(self,value=None):

        if self.read_secure_cookie('user_id'):
            if value:
                tag = value.split(',')
                if(tag[1]):
                    post = tag[0]
                    value = tag[1]
                    user = self.read_secure_cookie('user_id')
                    if Like.by_post_user(post,user).count() < 1:
                        like = Like(post=post, value=int(value), user = user)
                        like.put()
                    else:
                         like = Like.by_post_user(post,user).get()
                         like.value = int(value)
                         like.put()
                        
                else:
                    self.redirect('/')
            else:       
                self.redirect('/')
            self.redirect('/post/%s'%post)
        else:
            self.redirect('/')