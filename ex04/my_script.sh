#!/bin/sh

mkdir django_venv

python -m venv django_venv
conda create -n django_venv python=3.5.2 anaconda

source django_venv/bin/activate
  pip3 install -r requirement.txt
