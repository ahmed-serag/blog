from handler import Handler
from post import Post
from like import Like
from comment import Comment
from user import User
class Blog(Handler):
    def get(self):
        if self.read_secure_cookie('user_id'):
            posts = Post.all()
            user = User.by_id(self.read_secure_cookie('user_id'))
            self.render('home.html',posts = posts, user = user)
        else:
            self.redirect('/')
        
