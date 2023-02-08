class dblStack:
    def __init__(self):
        self.names = []
        self.entries = []
        self.size = 0

    def __repr__(self):
        _temp = ""
        for i in range(self.size):
            _temp += self.names[i] + ", " + self.entries[i] + "\n"
        return _temp

    def push(self, name: str, entry: str):
        self.names.append(name)
        self.entries.append(entry)
        self.size += 1

    def pop(self):
        _name = None
        _entry = None
        if len(self.names) > 0 and len(self.entries) > 0:
            _name = self.names[-1]
            _entry = self.entries[-1]
            del (self.names[-1])
            del (self.entries[-1])
            self.size -= 1
        return _name, _entry


def is_tag(_str: str) -> bool:
    if _str[0] == "<":
        return True
    return False


class MLParser:
    def __init__(self, filename: str):
        self.filename = filename
        self.stack = dblStack()

    def load_raw_data(self) -> list:
        _data = ""
        with open(self.filename, 'r') as f:
            _data = f.read()

        return [line for line in _data.split()]

    def format_data(self, rdata: list) -> list:
        _s = dblStack()
        _names = []
        _options = []

        running = True

        for index, line in enumerate(rdata):
            if is_tag(line):
                _names.append(line)
            if not is_tag(line):
                _options.append(line)

        print(f"Names: {_names}\nOptions: {_options}")

    def check_tags(self) -> bool:
        pass


parser = MLParser("image01.svg")
a = parser.load_raw_data()
parser.format_data(a)
