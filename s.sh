#!/bin/bash

ip='10.10.14.239'
port='8080'
dir='srv/'

mkdir -p $dir
python3 -m http.server $port --bind $ip --directory $dir
