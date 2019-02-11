import re


def get_ws_config(filename):
    config = []
    with open(filename) as f:
        for line in f.readlines():
            m = re.match(r'^\s*var\s*(\S+)\s*=\s*"(.*)";$', line.strip())
            if m:
                config.append(m.groups())
    return dict(config)
