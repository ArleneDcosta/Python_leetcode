import hashlib

class BloomFilter:
    def __init__(self, size=100):
        self.size = size
        self.bit_array = [0] * size

    def _hashes(self, item):
        h1 = int(hashlib.md5(item.encode()).hexdigest(), 16) % self.size
        h2 = int(hashlib.sha1(item.encode()).hexdigest(), 16) % self.size
        return [h1, h2]

    def add(self, item):
        for h in self._hashes(item):
            self.bit_array[h] = 1

    def check(self, item):
        return all(self.bit_array[h] == 1 for h in self._hashes(item))

# Example usage
bf = BloomFilter(size=10)
bf.add("cat")

print("cat:", "Maybe" if bf.check("cat") else "Nope")
print("dog:", "Maybe" if bf.check("dog") else "Nope")
