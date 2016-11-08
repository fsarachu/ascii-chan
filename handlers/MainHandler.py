from google.appengine.ext import db
from Handler import Handler


class MainHandler(Handler):
    def get(self):
        arts = db.GqlQuery("SELECT * FROM Art "
                           "ORDER BY created DESC")
        self.render('index.html', arts=arts)
