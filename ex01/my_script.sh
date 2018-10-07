#!/bin/sh

pip -V

mkdir local_lib
echo > ./local_lib/__init__.py
script ./local_lib/path_install.log -c "curl -L https://raw.githubusercontent.com/jaraco/path.py/master/path.py > ./local_lib/path.py"

python3 my_program.py
