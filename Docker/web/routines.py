#! /usr/bin/env python3
################################################################################
# Created: Thursday, October  1 2026
# Author: , ESK

from flask import render_template
import os
from tabulate import tabulate

def main_entry():
    return render_template('main.html')

def main_post():
    return "This is the current result"

################################################################################
def index_entry():
    table = []
    for _,_,files in os.walk("."):
        for file in files:
            table.append( [file,"Just another file"] )
    table = tabulate(table,tablefmt="html")
    return render_template("files.html",table=table)

    
# End of file
################################################################################
# Local Variables:
# comment-column: 60
# End:
################################################################################
