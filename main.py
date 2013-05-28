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
        template_values = {
                'title': self.pageTitle,
                'active_pageID': self.pageID,
                'navigation_bar': navBar
                }
        self.response.write(template.render(template_values))
        return


class HomePage(BaseHandler):
    template = 'home.html'
    pageTitle = 'Standard Dies And Tools'
    pageID = 'home'
    hRef = '/'
    navDisplay = 'Home'


class ProductsPage(BaseHandler):
    template = 'products.html'
    pageTitle = 'Products'
    pageID = 'Products'
    hRef = '/products/'
    navDisplay = 'Products'


class ContactUsPage(BaseHandler):
    template = 'contactus.html'
    pageTitle = "Contact"
    pageID = "Contact"
    hRef = '/contactus/'
    navDisplay = 'Contact'

class EnquiryPage(BaseHandler):
    template = 'enquiry.html'
    pageTitle = "Enquiry"
    pageID = "Enquiry"
    hRef = '/enquiry/'
    navDisplay = 'Enquiry'

class WarmupQueryHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("")
        return
    hRef = '/_ah/warmup/'


routes = [('/_ah/warmup', WarmupQueryHandler)]
navBar = []

for cls in [HomePage, ProductsPage, ContactUsPage, EnquiryPage]:
    routes.append((cls.hRef, cls))
    navBar.append((cls.hRef, cls.pageID, cls.navDisplay))

application = webapp2.WSGIApplication(routes, debug=True)
