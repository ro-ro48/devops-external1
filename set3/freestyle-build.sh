#!/bin/bash

set -e

echo "Starting Jenkins Freestyle Job"

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

echo "Running Python Tests"

pytest -v

echo "Jenkins Freestyle Job Completed Successfully"
