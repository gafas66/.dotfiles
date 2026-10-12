#! /usr/bin/env python3
################################################################################
# Created: Wednesday, September 30 2026
# Author: , ESK

import random
import string
import sys
from subprocess import Popen, run
from time import sleep

import cherrypy


class HelloWorld:
    @cherrypy.expose
    def index(self):
        return "Hello world"

    @cherrypy.expose
    def gen(self,length=8):
        return ''.join(random.sample(string.hexdigits,int(length)))

if len(sys.argv) > 1:
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 80,
    })
    try: cherrypy.quickstart(HelloWorld())
    finally: sys.exit(0) # Kill program when server stops/dies
    
if __name__ == '__main__':
    try:
        p = Popen(["python", "app.py", "--server"])
        sleep(3)
        run(["firefox", "http://localhost:80"],check=False)
    finally:
        print("Firefox is done")
        p.terminate()
        sys.exit(0)


'''
from flask import Flask
import routines

app = Flask(__name__)

@app.route('/')
def hello_world():
    return routines.main_entry()

@app.route('/handle_post',methods=['post'])
def main_post():
    return routines.main_post()

@app.route('/files')
def show_files():
    ##return "This was supposed to be another page"
    return routines.index_entry()

app.run(debug=True)
'''

# End of file
################################################################################
# Local Variables:
# comment-column: 60
# End:
################################################################################
