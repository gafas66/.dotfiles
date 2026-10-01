#! /usr/bin/env python3
################################################################################
# Created: Wednesday, September 30 2026
# Author: , ESK

from flask import Flask
import routines

app = Flask(__name__)

@app.route('/')
def hello_world():
    return routines.main_entry()

@app.route('/files')
def show_files():
    ##return "This was supposed to be another page"
    return routines.index_entry()

app.run(debug=True)

# End of file
################################################################################
# Local Variables:
# comment-column: 60
# End:
################################################################################
