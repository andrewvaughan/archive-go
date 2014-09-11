import ConfigParser, os

from bottle import route, error, static_file, request, response, redirect, run
from go import Go


# Load our useful paths
script_dir = os.path.dirname(os.path.realpath(__file__))
conf_dir = os.path.realpath(script_dir + '/../conf')


# Load in the configuration files, if set
config = ConfigParser.ConfigParser()
config.readfp(open(conf_dir + '/default.ini'))
config.read([conf_dir + '/local.ini'])


# Initialize GO
go = Go(config = config)


# 404 Error
@error(404)
def error404(error):
    return static_file('404.html', root = script_dir + '/templates')


# Registration
@route('/')
def register():
    return static_file('index.html', root = script_dir + '/templates')


# Register call
@route('/', method = "POST")
def register_do():
    url = request.forms.get('url')
    vanity = request.forms.get('vanity')
    
    return go.register(url, vanity)


# Redirections
@route('/<route>')
def route(route):
    url = go.fetch(route)
    
    if not url:
        response.status = "404 Not Found"
        return static_file('404.html', root = script_dir + '/templates')
    
    return redirect(url)


run(
    host = config.get('server', 'host'),
    port = config.get('server', 'port')
)