################################################################################

import os
import re
import sys
from glob import glob

from tabulate import tabulate


################################################################################
def get_vec():
    #Popen(f"{command}",stdout=PIPE,stderr=PIPE,shell=True)
    #return f"<p>{command}</p>"
    WDIR = "/home/EPI/project/EUPILOT/VEC/signoff"

    htm = []
    for mod in ("vec","iotile","ddr","c2c","axi","pcie"):
        link = f"xterm?cmd=make+{mod}&wdir={WDIR}"
        htm.append( [f"Last {mod} innovus db",f'<a href="{link}" class="button">{mod}</a>'] )
    
    link = f"xterm?cmd=make+gds&wdir={WDIR}"
    htm.append( ["chip_vec_top.gds - RC4 (fabricated)",f'<a href="{link}" class="button">CHIP_VEC_TOP (RC4)</a>'] )

    return tabulate(htm,tablefmt="unsafehtml")

################################################################################
REENA = "/home/idsproj01/trusted/projects/TrEB/Design/Cerberus_ASIC/_cad/Digital/user/sisodiya"
def get_metis_v2():
    "Get innovus link and lvs links to Reena MV2"
    layerfile = "/home/kofoed/prj/vendor/gf/GF22INVECTAS.layerprops"
    htm = []
    keep = ["init","floorplan","place","cts","postcts","route","postroute","outputs"]
    wd = f"{REENA}/pnr_innovus"
    for d in glob(f"{wd}/chip_cerberus_22fdx_s*_pnr*"):
        base = os.path.basename(d)
        dbs = [base]
        for db in glob(f"{d}/dbs/*"):
            name = os.path.basename(db)
            if not name in keep:
                continue
            dbs.append(f'<a href="xterm?cmd=innovus+-db+{db}&title=Cerberus+project+{name}" class="button">{name}</a>')
        htm.append(dbs)
    # NOTE Latest GDS
    gds   = f"{REENA}/pnr_innovus/chip_cerberus_22fdx_s05_pnr03/my_results/chip_cerberus_22fdx.output.gds.gz"
    gds2  = f"{REENA}/phy_ver/chip_cerberus_22fdx_s05_pnr07/run_merge/chip_cerberus_22fdx_dp_merged.gds.gz"
    lvs   = f"{REENA}/phy_ver/chip_cerberus_22fdx_s05_pnr07/run_lvs/svdb"
    link  = f"xterm?cmd=calibredrv+-m+{gds}+-l+{layerfile}&title=Cerberus+GDS"
    link2 = f"xterm?cmd=calibredrv+-m+{gds2}+-l+{layerfile}&title=Cerberus+GDS"
    link3 = f"xterm?cmd=calibredrv+-m+{gds2}+-l+{layerfile}+-rve+-lvs+{lvs}&title=Cerberus+GDS"
    htm.append(["s05_pnr03 GDS",f'<a class="button" href="{link}">s05_pnr03 GDS</a>'])
    htm.append(["s05_pnr05_pnr07 GDS2",f'<a class="button" href="{link2}">dp_merged 10-nov-26</a>'])
    htm.append(["s05_pnr05_pnr07 GDS2 LVS",f'<a class="button" href="{link3}">LVS dp_merged 10-nov-26</a>'])
    return tabulate(htm,tablefmt="unsafehtml")

################################################################################
#tools = ["calibre","genus","tempus"] # genus/innovus are in same bin
tools = ["calibre","calibredrv","genus","tempus","innovus","lec"]
l     = max([len(s) for s in tools])

def check_tool_versions(tools=tools):
    '''Loop through path to check for newer versions of tools'''
    for tool in tools:
        for path in os.getenv("PATH").split(":"):
            current = path + "/" + tool
            if os.path.exists(current):
                current_date = tool_date(current)
                path = os.path.dirname(path) # less /bin/tool
                print(f"{tool:{l}s} {path}") # current, w/o bin/tool
                path = os.path.dirname(path)
                for file in glob(f"{path}/*/bin/{tool}"):
                    m = re.search(r"(.*)/bin/.*",file)
                    if os.path.islink(m.group(1)): continue
                    if int(tool_date(file)) > int(current_date):
                        print(f"  {tool_date(file)} {file} VS {current}")

def tool_date(tool):
    '''
    Translates version numbers into (string) integers.
    Exits program if version cannot be identified
    '''

    # Calibre
    m = re.search(r".*(ixl|aoi|aoj|aok|x86)_cal_(\d\d\d\d)\.(\d+)_(\d+)\.(\d+).*",tool)
    if m:
        ix = ["","x86","ixl","aoi","aoj","aok"]
        j = ix.index(m.group(1))
        val = []
        for n in range(2,6): val.append(int(m.group(n)))
        return f"{j}{val[0]:04d}_{val[1]:01d}_{val[2]:02d}_{val[3]:02d}"
    

    # genus/innovus/tempus
    m = re.search(r".*(DDI|SSV)/(\d+)\.(\d+)\.(\d+).*",tool)
    if m:
        val = []
        for n in range(2,5): val.append(int(m.group(n)))
        return f"{val[0]:02d}_{val[1]:02d}_{val[2]:03d}"

    # lec
    m = re.search(r".*/(\d+)\.(\d+)\.d?(\d+).*",tool)
    if m:
        val = []
        for n in range(1,4): val.append(int(m.group(n)))
        return f"{val[0]:02d}_{val[1]:02d}_{val[2]:03d}"


    print(f"Cant id date: {tool}")
    sys.exit(0)

################################################################################
wd = f"{REENA}/pnr_innovus"
if __name__ == "__main__":
    print("Testing glob")
    print(glob(f"{wd}/chip_cerberus_22fdx_s*_pnr*/dbs/*"))
    
# End
################################################################################
