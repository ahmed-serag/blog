"""
this module is responsibe for handling the app and request
"""

import webapp2
from mainpage import MainPage
from blog import Blog
from writepost import WritePost
"""
app object 
"""
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/blog',Blog),
    ('/writePost',WritePost)
], debug=True)


 