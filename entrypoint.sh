#!/bin/sh
gunicorn -w 2 -b 0.0.0.0:8082 wsgi:api