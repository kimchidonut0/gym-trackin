#!/bin/bash
gunicorn --workers 4 --bind 127.0.0.1:5000 run:app