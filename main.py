import os
import webapp2
import jinja2

templates = os.path.join(os.path.dirname(__file__), 'templates')

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(templates),
    extensions=['jinja2.ext.autoescape'])

class BaseHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template(self.template)
        template_values = {'title': self.title} #TODO: Look at internet and see what is the trend and move this into html page
        self.response.write(template.render(template_values))
        return

class HomePage(BaseHandler):
    template = 'home.html'
    title = 'Standard Dies And Tools'

class ProductsPage(BaseHandler):
    template = 'products.html'
    title = 'Products'

class AboutPage(BaseHandler):
    template = 'aboutus.html'
    title = 'About us'

class ClientsPage(BaseHandler):
    template = 'clients.html'
    title = "Clients"

class ContactUsPage(BaseHandler):
    template = 'contactus.html'
    title = "Contact us"

class EnquiryPage(BaseHandler):
    template = 'enquiry.html'
    title = "Enquiries"

application = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/products/', ProductsPage),
    ('/contactus/', ContactUsPage),
    ('/enquiry/', EnquiryPage),
    ('/_ah/warmupenquiry/', EnquiryPage),
    ], debug=True)
