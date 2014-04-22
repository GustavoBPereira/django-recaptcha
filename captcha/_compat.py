import sys

PY2 = sys.version_info[0] == 2
if PY2:
    text_type = unicode
else:
    text_type = str


def want_bytes(s, encoding='utf-8', errors='strict'):
    if isinstance(s, text_type):
        s = s.encode(encoding, errors)
    return s