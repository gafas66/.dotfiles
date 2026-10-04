#! /usr/bin/env python3
################################################################################
# Created: Saturday, October  3 2026
# Author: , ESK

import os,subprocess,shlex,re, platform
from tabulate import tabulate

info = []

def get_output(cmd):
    args   = shlex.split(cmd)
    p      = subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return str(p.communicate()[0]).strip()
    
def get_pi_version():
    result = get_output('cat /proc/device-tree/model')
    m      = re.search(r"'(.*)\\x",result)
    result = m.group(1) if m else None
    return result

try:
    pi_version = get_pi_version()
except:
    pi_version = None

info.append(["Pi Version",pi_version])
################################################################################
def get_kernel_version():
    res = get_output("uname -r")
    m = re.search(r"'(.*)\\n",res)
    info.append(["Kernel",m.group(1)])
def get_opsys_version():
    res = get_output("grep DEBIAN_VER /etc/os-release")
    m = re.search(r"'(.*)\\n",res)
    info.append(["OS",m.group(1)])
    
get_kernel_version()
get_opsys_version()
info.append([ "Python",platform.python_version() ])
#info.append([ "System",platform.system() ])
#info.append([ "Release",platform.uname()[0]["machine"] ])
outer = [["System information","Other information"]]

format = "outline"

outer.append([tabulate(info,tablefmt=format),"NA"])
#print(tabulate(outer,tablefmt=outline))
print(tabulate(info,tablefmt=format))

# End of file
################################################################################
# Local Variables:
# comment-column: 60
# End:
################################################################################
