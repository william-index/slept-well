import webapp2
import handlers


app = webapp2.WSGIApplication([
    webapp2.Route('/', handler=handlers.IndexHandler, name='index'),
], debug=True)
