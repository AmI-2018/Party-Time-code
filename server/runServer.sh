#! /bin/bash

python3 zeroconf_server_2.py &
wait 5
python3 APIserver.py &
wait 5
python3 create_playlist.py &
