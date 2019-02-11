class DB:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        try:
            with open(self.filename) as f:
                return f.readline().strip()
        except FileNotFoundError:
            return '0'

    def write(self, data):
        with open(self.filename, 'w') as f:
            f.write(data)
