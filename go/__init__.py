import ConfigParser, os

from bottle import route, error, static_file, response, run


# from go import Go


# Load our useful paths
script_dir = os.path.dirname(os.path.realpath(__file__))
conf_dir = os.path.realpath(script_dir + '/../conf')


# Load in the configuration files, if set
config = ConfigParser.ConfigParser()
config.readfp(open(conf_dir + '/default.ini'))
config.read([conf_dir + '/local.ini'])


# 404 Error
@error(404)
def error404(error):
    return "Redirect not found."


# Registration
@route('/')
def register():
    return static_file('index.html', root = script_dir + '/templates')

@route('/', method = 'POST')
def register_do():
    url = request.forms.get('url')
    return "TBD"


# Redirections
@route('/<route>')
def route(route):
    response.status = "404 Not Found"
    return "Redirect not found"


run(
    host = config.get('server', 'host'),
    port = config.get('server', 'port')
)