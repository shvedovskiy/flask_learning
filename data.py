DATA_ENCODING = 'utf-8'
_data_filename = None
_entries = None


def _load_entries():
    with open(_data_filename, 'r', encoding=DATA_ENCODING) as data_file:
        return eval(data_file.read())


def _save_entries():
    with open(_data_filename, 'w', encoding=DATA_ENCODING) as data_file:
        print(repr(_entries), file=data_file)

def init_with_file(filename):
    global _data_filename, _entries
    _data_filename = filename
    _entries = _load_entries()


def get_entries():
    return _entries


def add_entry(entry):
    _entries.append(entry)
    _save_entries()
