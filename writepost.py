from handler import Handler
from user import  User
from post import Post
class WritePost(Handler):
    def post(self):
        if self.read_secure_cookie('user_id'):

            user = self.request.get('user')
            title = self.request.get('title')
            body = self.request.get('body')
            post = Post(title = title, body = body, user=user)
            post.put()
            self.redirect('/blog')
            
        else:
            self.redirect('/')
        

    def get(self):
        if self.read_secure_cookie('user_id'):

            user = User.by_id(self.read_secure_cookie('user_id'))
            self.render('write_post.html', user = user)
        else:
            self.redirect('/')
        
