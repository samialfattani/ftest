# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Flask project


import sys
import os

# add your project directory to the sys.path
project_home = '/home/samialfattani/ftest'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# MUST BE BEFORE CREATING `app`
# from dotenv import load_dotenv
# load_dotenv( os.path.join (project_home, '.env') )

# need to be "application" for WSGI to work
# from app import app as application

import app as application