#!/bin/bash

BASE_DIR=.
VENV_DIR=/usr/local/pythonenv/ffmunge-env

echo "Creating the Python virtual environment..."
virtualenv -p /usr/bin/python3.5 --system-site-packages $VENV_DIR

echo "Entering the virtual environment..."
source $VENV_DIR/bin/activate

#echo "Installing Python dependencies..."
#pip install -r $BASE_DIR/DEPENDENCIES
