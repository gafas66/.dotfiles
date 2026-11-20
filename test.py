#! /usr/bin/env python3
################################################################################
# Created: Friday, November 13 2026
# Author: , ESK

import os
import sys
import termios
import tty
from routines import check_tool_versions

if os.path.exists("/home/demo_10g"):
    wdir = [
        ["code",    "/home/demo_10g/Metis_Bringup/metis-bringup-scripts/code"],
        ["Old code","/home/demo_10g/Metis_Bringup/metis-bringup-scripts_cc"],
    ]
elif os.path.exists("/home/idsproj01/trusted/projects/TrEB"):
    wdir = [
        ["Pattern analyzer Synth",      "/home/icdaproj01/bcdc_wcc/Design/APEC_01/_cad/backend2/pattern_analyzer/1_syn/"],
        ["Pattern analyzer PnR",        "/home/icdaproj01/bcdc_wcc/Design/APEC_01/_cad/backend2/pattern_analyzer/2_pnr/"],
        ["Pattern_generator (APECS 1)", "/home/icdaproj01/bcdc_wcc/Design/APEC_01/_cad/backend/pattern_gen/2_pnr\n"],
        
        ["cerberus07",                  "/home/idsproj01/trusted/projects/TrEB/Design/Cerberus_ASIC/_cad/Digital/user/uenal/syn/chip_cerberus_22fdx_r07"],
        ["cerbKOF",                     "/home/idsproj01/trusted/projects/TrEB/Design/Cerberus_ASIC/_cad/Digital/user/kofoed/TReB"],
        ["from_WCC",                    "/home/icdaproj01/bcdc_wcc/Design/APEC_01/_cad/backend/from_wcc"],
        ["ocean12",                     "/home/ocean12/Design/OCEAN_22FDX_02/_cad/digital/atz/pnr_innovus/ocean12_22fdx_02_v18_2eco"],
  ]
#        ["RC7",           "/home/EPI/project/EUPILOT/VEC/usr/esk/pnr_innovus/pcie_r08_v4/INNOVUS/WORK004_vec_top/3_calibre"],
#        ["RC6",           "/home/EPI/project/EUPILOT/VEC/usr/esk/pnr_innovus/pcie_r08_v4/INNOVUS/WORK004_vec_top/calibre_RC6"],
#        ["pattern_gen",   "/home/icdaproj01/bcdc_wcc/Design/APEC_01/_cad/backend/pattern_gen/2_pnr"],
else:
    print("Unknown filesystem - works only at FhG")

l0 = max([len(arr[0]) for arr in wdir])

################################################################################
def main():
    if len(sys.argv) == 1:
        print(f'''
        Usage: {sys.argv[0]} [d1] [d2]
        ''')
        sys.exit(0)
    if sys.argv[1] == "d1":    show_dirs()
    if sys.argv[1] == "d2":    select_dir()
    if sys.argv[1] == "tools": check_tool_versions()
    
def show_dirs():
    print("Select:")
    for i,d in enumerate(wdir):
        print(f"[{i+1}] {d[0]:{l0}s} {d[1]}")

def select_dir():
    try:
        cmd = int(getch())-1
    except ValueError:
        print("echo No number was entered")
        sys.exit(0)
    if cmd < 0 or cmd > (len(wdir)-1):
        print("echo Number out of range")
        sys.exit(0)
    print(f"cd {wdir[cmd][1]}")

################################################################################
def getch():
    fd = sys.stdin.fileno()
    orig = termios.tcgetattr(fd)

    try:
        tty.setcbreak(fd)  # or tty.setraw(fd) if you prefer raw mode's behavior.
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, orig)

# End of file
if __name__=="__main__": main()
################################################################################
