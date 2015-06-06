=====
Luffa
=====

Project Luffa (絲瓜) aimed to provide integration between multiple Slack domains.

Installation
------------
::

 $ pip install git+https://github.com/rschiang/luffa.git


Config
-------
We using a json file for our configuration shown as following::

 {
     "example": {
         "slug": "Example",
         "token": "LoremIpsumDonorAmet",
         "publish_hook": "https://hooks.slack.com/services/LoremIpsum/DonorAmet"
     }
 }

Please create a config file and place it at one of path.

+ ``./luffa.conf``,
+ ``/usr/local/etc/luffa.json``
+ ``/etc/luffa.json``
+ ``$HOME/.luffa.json``

We will load it in this order; note that the first math win.

Run server
-----------

With bottle builtin server::

 $ luffa

License
--------

Copyright (C) Poren Chiang 2015, released under MIT License.
