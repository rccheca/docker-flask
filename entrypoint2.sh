#!/bin/bash
gunicorn -w 4 -b 0:$PORT app:app --reload