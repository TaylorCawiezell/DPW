import webapp2
from pages import Page #from ofile import class

class MainHandler(webapp2.RequestHandler):
    def get(self):
       p = Page()
       p.title = 'My Page!'
       p.css = 'css/main.css'
       p.body = "Miss Piggy is aweful!"
       p.update()
       self.response.write(p.whole_page)
        

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
