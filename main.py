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
import webapp2
import ceasarporweb

def build_page(textarea_content):
    header = "<h3>What would you like to encrypt?</h3>"
    text_area = "<textarea rows='4' cols='50' name='message'>" + textarea_content + "</textarea>"
    rot_amount = "<input type='text' name='rotationamount' style='width: 17px; margin: 0px 4px 0px 0px'/>"
    rotation_label = "<label>Rotate message by </label>"
    submit = "<input type='submit'/>"
    form = ("<form method='post'>" +
            text_area + "<br><br>" + rotation_label
            + rot_amount + "<span>characters </span><br>"
            + submit + "</form>")
    return header + form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")

        self.response.write(content)

    def post(self):
        message = self.request.get("message")
        rotation = self.request.get("rotationamount")

        encrypted_message = ceasarporweb.encrypt(message, int(rotation))
        self.response.write("<p>thanks, buddy</p><br><img src='http://www.reocities.com/Hollywood/Land/4801/main/terrance11.gif'/><br><br><strong>Your secret message is:</strong>" + encrypted_message)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
