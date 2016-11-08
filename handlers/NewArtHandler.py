from Handler import Handler
from entities import *


class NewArtHandler(Handler):
    def get(self):
        self.render('new_art.html')

    def post(self):
        title = self.request.get('title')
        art = self.request.get('art')

        if title and art:
            new_art = Art(title=title, art=art)
            new_art.put()
            self.redirect('/')
        else:
            error = 'We need both a title and art!'
            self.render('new_art.html', error=error, title=title, art=art)
