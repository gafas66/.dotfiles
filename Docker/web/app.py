#! /usr/bin/env python3
################################################################################
# Created: Wednesday, September 30 2026
# Author: , ESK



from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():

    return "Hello world!"

    
# End of file
################################################################################
# Local Variables:
# comment-column: 60
# End:
################################################################################
