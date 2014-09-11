import redis
import base64
import md5


class Go:
    def __init__(self, config = []):
        self.config = config
        self.redis = redis.StrictRedis(
            host = config.get('redis', 'host'),
            port = config.get('redis', 'port'),
            db = config.get('redis', 'db')
        )
        
    
    def hash(self, url):
        """
        Hashing method that returns a stored/generated hash created from the
        Base64 encoded MD5 hash of the URL.
        """
        return base64.b64encode(
            md5.new(url).digest().replace('=', '').replace('/', '_')[-6:]
        )
        
        
    def register(self, url, vanity = None):
        """
        Registration method that will hash and return a shortcode for a given
        URL.  Will attempt to use a vanity URL if one is provided, and it has
        not already been used.  If the vanity URL has been used, a random hash
        will be returned.
        
        On the rare collision, a previous hash will be evicted.
        
        On error, this method returns None.
        """
        prefix = self.config.get('redis', 'prefix')
        
        if (vanity and vanity != ''):
            test = self.redis.get(prefix + vanity)
            
            if test == url:
                return vanity
            
            if not test:
                self.redis.set(prefix + vanity, url)
                return vanity
        
        # No vanity, or vanity failed, let's hash
        hash = self.hash(url)
        
        try:
            self.redis.set(prefix + hash, url)
            return hash
            
        except:
            return None
    
    
    def fetch(self, hash):
        """
        Returns a URL for a given hash, or None if the hash does not exist.
        """
        try:
            return self.redis.get(
                self.config.get('redis', 'prefix') + hash
            )
            
        except:
            return None
