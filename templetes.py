"""
this module is responsibe for handling the app and request
"""

import webapp2
from mainpage import MainPage
from blog import Blog
from writepost import WritePost
from viewpost import ViewPost
from logout import LogOut
from like import LikeHandler

"""
app object 
"""
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/logout',LogOut),
    ('/like/([0-9,]+)',LikeHandler),
    ('/blog',Blog),
    ('/writePost',WritePost),
    ('/post/([0-9]+)',ViewPost),
     ('/post',ViewPost),
      ('/*', MainPage)
], debug=True)


 