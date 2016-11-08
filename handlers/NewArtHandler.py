from Handler import Handler


class NewArtHandler(Handler):
    def get(self):
        self.render('new_art.html')

    def post(self):
        title = self.request.get('title')
        art = self.request.get('art')

        if title and art:
            self.write("Thanks!")
        else:
            error = 'We need both a title and art!'
            self.render('new_art.html', error=error)
