################################################################################
# Created: Thursday, October  1 2026
# Author: , ESK

import os
import subprocess

from flask import render_template
from tabulate import tabulate


def main_entry():
    return render_template('main.html')

def main_post():
    subprocess.run("touch done_this",shell=True,check=False)
    return "This is the current result - second try"

################################################################################
def index_entry():
    table = []
    for _,_,files in os.walk("."):
        for file in files:
            table.append( [file,"Just another file"] )
    table = tabulate(table,tablefmt="html")
    return render_template("files.html",table=table)

def test():
    pass


    
# End of file
################################################################################
# Local Variables:
# comment-column: 60
# End:
################################################################################
