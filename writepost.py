from handler import Handler
from user import  User
from post import Post
class WritePost(Handler):
    '''
    this class is responsible for handling requests for new posts
    '''
    def post(self, post_id=None):
        if self.read_secure_cookie('user_id'):
            if self.request.get('edit_id'):
                post = Post.by_id(self.request.get('edit_id'))
                if post:
                    post.title = self.request.get('title')
                    post.body = self.request.get('body')
                else:
                    user = User.by_id(self.read_secure_cookie('user_id')).username
                    title = self.request.get('title')
                    body = self.request.get('body')
                    post = Post(title = title, body = body, user=user)
            else:
                user = User.by_id(self.read_secure_cookie('user_id')).username
                title = self.request.get('title')
                body = self.request.get('body')
                post = Post(title = title, body = body, user=user)
            post.put()
            self.redirect('/blog')
        else:
            self.redirect('/')

    def get(self, post_id=None):
        if self.read_secure_cookie('user_id'):
            if post_id:
                post = Post.by_id(post_id)
            else:
                post = None
            user = User.by_id(self.read_secure_cookie('user_id'))
            self.render('write_post.html', user = user, post=post, post_id=post_id)
        else:
            self.redirect('/')
