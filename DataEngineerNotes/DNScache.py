import socket
import time

class DNSResolver:
    def __init__(self, ttl=60):
        self.cache = {}
        self.ttl = ttl

    def resolve(self, domain):
        if domain in self.cache:
            ip, expiration = self.cache[domain]
            if expiration > time.time():
                return ip

        ips = socket.getaddrinfo(domain, None)
        #[(<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_DGRAM: 2>, 17, '', ('93.184.216.34', 80)),
        if not ips:
            return None

        ip = ips[0][4][0]
        self.cache[domain] = (ip, time.time() + self.ttl)
        return ip

    def clear_cache(self):
        self.cache.clear()