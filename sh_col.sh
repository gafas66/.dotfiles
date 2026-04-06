#! /bin/sh
################################################################################
# Created: Monday, April  6 2026
# Time-stamp: <2026-04-06 12:01:52 erik>
# Author: , ESK

# Description:
# 

# red    31 / 41
# green  32 / 42
# yellow 33 / 43
# blue   34 / 44

# '&' represents matched pattern
# '\x1b[' + color-number + 'm' is selected color
# \x1b[0m' means reset colors to default

s/.*ERROR.*/\x1b[31m\x1b[43m&\x1b[0m/
s/.*WARNING.*/\x1b[31m&\x1b[0m/

# End of file
################################################################################
# Local Variables:
# comment-column: 60
# End:
################################################################################
