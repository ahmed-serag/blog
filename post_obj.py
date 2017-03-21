
class Post_obj:

    def __init__(self, user, title, body, likes, dislikes):
        self.user = user
        self.title = title
        self.body = body
        self.comments = []
        self.likes = likes
        self.dislikes = dislikes

    def add_comments(self, comments):
        self.comments.extend(comments)


