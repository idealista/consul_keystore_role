#!/bin/bash
set -e

cd `dirname "$0"`/../..
rm -rf venv
virtualenv venv
source venv/bin/activate
pip install molecule==1.25.0
pip install ansible==2.4.3.0
pip install python-vagrant
pip install python-consul
molecule converge
deactivate
rm -rf venv
