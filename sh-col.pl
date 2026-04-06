#! perl
################################################################################
# Created: Monday, April  6 2026
# Time-stamp: <2026-04-06 14:26:15 erik>
# Author: , ESK

# Description:
# 
use strict;

my $red    = "\x1b[31m";my $bred    = "\x1b[41m";
my $green  = "\x1b[32m";my $bgreen  = "\x1b[42m";
my $yellow = "\x1b[33m";my $byellow = "\x1b[43m";
my $blue   = "\x1b[34m";my $bblue   = "\x1b[44m";
my $off    = "\x1b[0m";
# '&' represents matched pattern
# '\x1b[' + color-number + 'm' is selected color
# \x1b[0m' means reset colors to default

s/.*ERROR.*/$red$byellow$&$off/;
s/.*WARNING.*/$blue$&$off/;

print;

# End of file
################################################################################
# Local Variables:
# comment-column: 60
# End:
################################################################################
