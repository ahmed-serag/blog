from like import Like
from handler import Handler
from post import Post
class LikeHandler(Handler):
    '''
    this class handel the requests for likes and dislikes
    '''
    def get(self,value=None):

        if self.read_secure_cookie('user_id'):
            if value:
                tag = value.split(',')
                if(tag[1]):
                    post = tag[0]
                    value = tag[1]
                    user = self.read_secure_cookie('user_id')
                    if int(post) and Post.by_id(post):
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