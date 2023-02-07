#!/bin/bash

pip --version
mkdir -p local_lib
pip install git+https://github.com/jaraco/path.git --upgrade -t local_lib > path.log
python3 my_program.py