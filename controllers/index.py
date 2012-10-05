import os
import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import xmpp
from google.appengine.api.labs import taskqueue
from google.appengine.ext.webapp import xmpp_handlers
from models import Channel
from models import Log
from models import Person

import logging
import re
import wsgiref.handlers



class IndexController(webapp.RequestHandler):
  """Controller that handles the front page."""

  def get(self):
    path = os.path.join(os.curdir, '..', 'templates', 'index.html')
    values = {
        'app_jid': os.environ['SERVER_NAME'].replace('.', '@', 1),
    }
    self.response.out.write(template.render(path, values))


def main():
  app = webapp.WSGIApplication([
      ('/', IndexController),
      ], debug=True)
  wsgiref.handlers.CGIHandler().run(app)
  
  

if __name__ == '__main__':
  main()
