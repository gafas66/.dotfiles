#! /usr/bin/env python3
################################################################################
# Created: Wednesday, September 30 2026
# Author: , ESK

import os

workers = int(os.environ.get('GUNICORN_PROCESSES','2'))
threads = int(os.environ.get('GUNICORN_THREADS','4'))

bind = os.environ.get('GUNICORN_BIND','0.0.0.0:80')

forwarded_allow_ips = '*'

secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }

# End of file
################################################################################
# Local Variables:
# comment-column: 60
# End:
################################################################################
