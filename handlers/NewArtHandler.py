from Handler import Handler


class NewArtHandler(Handler):
    def get(self):
        self.render('new_art.html')

    def post(self):
        pass
