#! /usr/bin/env python3
################################################################################
# Created: Thursday, October  1 2026
# Author: , ESK

from flask import render_template
from flask_table import Table, Col
import os

class ItemTable(Table):
    name = Col('Name')
    description = Col('Description')
################################################################################

def main_entry():
    return render_template('main.html')

################################################################################
def index_entry():
    text = []
    for _,_,files in os.walk("."):
        for file in files:
            text.append( {"name": file,"description": "Just another file"} )
        break
    table = ItemTable(text)
    return render_template("files.html")

# End of file
################################################################################
# Local Variables:
# comment-column: 60
# End:
################################################################################
