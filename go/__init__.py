import ConfigParser, os

# from go import Go


# Load our useful paths
script_dir = os.path.dirname(os.path.realpath(__file__))
conf_dir = os.path.realpath(script_dir + '/../conf')


# Load in the configuration files, if set
config = ConfigParser.ConfigParser()
config.readfp(open(conf_dir + '/default.ini'))
config.read([conf_dir + '/local.ini'])


# go = Go()