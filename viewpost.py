from handler import Handler
from user import  User
from post import Post
from comment import Comment
from like import Like
class ViewPost(Handler):
    '''
    this class handle requests to view the post and it's comments and likes
    '''
    def post(self, post_param=None):
        if self.read_secure_cookie('user_id'):
            user = self.request.get('user')
            post = self.request.get('post')
            body = self.request.get('body')
            if Post.by_id(int(post)) and User.by_name(user):
                comment = Comment(user = user, body = body, post=post)
                comment.put()
                self.redirect('/post/%s'%post)
        else:
            self.redirect('/')

    def get(self, post_id=None):
        if self.read_secure_cookie('user_id'):
            if post_id and Post.by_id(int(post_id)):
                post = Post.by_id(int(post_id))
                comments = Comment.by_post(post_id)
                likes = Like.by_post(post_id)
                likes_num = 0
                dislikes_num = 0
                if Like.by_post(post_id).count():
                    for like in Like.by_post(post_id):
                        if like.value > 0:
                            likes_num +=1
                        else:
                            dislikes_num +=1
                user = User.by_id(self.read_secure_cookie('user_id'))
                self.render('post.html', post = post, comments = comments, likes = likes_num, dislikes = dislikes_num, user = user, post_id=post_id)
            else:
                self.redirect('/')
        else:
            self.redirect('/')
