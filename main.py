import webapp2

from handlers import *

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/new-art', NewArtHandler)
], debug=True)
