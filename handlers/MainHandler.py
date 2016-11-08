from Handler import Handler


class MainHandler(Handler):
    def get(self):
        self.render('base.html', x=1, y=2)
