#! /usr/bin/env python3
################################################################################
# Created: Thursday, October  1 2026
# Author: , ESK

import os
from tabulate import tabulate
    
text = []
for _,_,files in os.walk("."):
    for file in files:
	text.append( [file,"Just another file"] )
	
#print(text)
#print(tabulate(text,tablefmt='html'))
#print(tabulate(text,tablefmt='rounded_outline'))
print(tabulate(text,tablefmt='latex'))
#print(tabulate(text))

if os.
# End of file
################################################################################
# Local Variables:
# comment-column: 60
# End:
################################################################################
