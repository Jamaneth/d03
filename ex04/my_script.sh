#mkdir django_venv

#python3 -m venv --without-pip django_venv
conda create -n django_venv python=3.5.2 anaconda

source activate django_venv
#  pip3 install -r requirement.txt
  conda install -n django_venv django=2.1.0
  conda install -n django_venv psycopg2-binary==2.7.0
