#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import logging
from django.utils import simplejson as json

class MainHandler(webapp.RequestHandler):
    def post(self):
        payload_j = self.request.POST['payload']
        payload = json.dumps(payload_j)
	logging.debug("Received payload %s" % payload)

def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=False)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()