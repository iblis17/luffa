import os


CONFIG_SEARCH_PATH = (
    './luffa.conf',
    '/usr/local/etc/luffa.json',
    '/etc/luffa.json',
    os.path.join(os.environ.get('HOME'), '.luffa.json'),
)
