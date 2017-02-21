

import webapp2
import ceasarporweb
import cgi


rotationamount = 0

def build_page(textarea_content, rotationamount):

    header = "<h3>What would you like to encrypt?</h3>"
    text_area = "<textarea rows='4' cols='50' name='message'>" + textarea_content + "</textarea>"
    rot_amount = "<input type='text' name='rotationamount' value=''style='width: 17px; margin: 0px 4px 0px 0px'/>"
    rotation_label = "<label>Rotate message by </label>"
    submit = "<input type='submit'/>"
    form = ("<form method='post'>" +
            text_area + "<br><br>" + rotation_label
            + rot_amount + "<span>characters </span><br>"
            + submit + "</form>")
    return header + form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("","")

        self.response.write(content)

    def post(self):
        message = self.request.get("message")
        rotation = self.request.get("rotationamount")

        encrypted_message = ceasarporweb.encrypt(message, int(rotation))
        escaped_message = cgi.escape(encrypted_message)
        self.response.write(build_page(textarea_content=escaped_message, rotationamount=int(rotation)))
#"<p>hey, buddy!</p><br><strong>Your secret message is:  </strong>" + escaped_message
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
