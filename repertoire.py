class Repertoire:
    def __init__(self, size):
        self.buckets = []
        for i in range(size):
            self.buckets.append([])

    def append(self, key, data):
        index = key % len(self.buckets)
        bucket = self.buckets[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key, data)
                return
        bucket.append((key, data))

    def get(self, key):
        index = key % len(self.buckets)
        for (k, d) in self.buckets[index]:
            if k is key:
                return d
        return None
