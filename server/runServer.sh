#! /bin/bash

python3 zeroconf_server_2.py &

python3 APIserver.py &

python3 create_playlist.py &
