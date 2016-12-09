import webapp2
from webapp2_extras import jinja2


class BaseHandler(webapp2.RequestHandler):

    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)
        self.context = {}

    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def render(self, template):
        self.response.write(self.jinja2.render_template(template, **self.context))

    def urlFor(self, name, **kwargs):
        """
        get url by name
        :param name: name of URL
        :return: url
        """
        return webapp2.uri_for(name, self, **kwargs)
