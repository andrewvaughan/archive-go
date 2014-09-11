import ConfigParser, os

from bottle import route, run, template


# from go import Go


# Load our useful paths
script_dir = os.path.dirname(os.path.realpath(__file__))
conf_dir = os.path.realpath(script_dir + '/../conf')


# Load in the configuration files, if set
config = ConfigParser.ConfigParser()
config.readfp(open(conf_dir + '/default.ini'))
config.read([conf_dir + '/local.ini'])


# Setup our redirect routes
@route('/<route>')
def route(route):
    return 


run(
    host = config.get('server', 'host'),
    port = config.get('server', 'port')
)