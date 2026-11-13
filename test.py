#! /usr/bin/env python3
################################################################################
# Created: Friday, November 13 2026
# Author: , ESK

import os
import sys
import termios
import tty

if os.path.exists("/home/demo_10g"):
    wdir = [
        ["code",    "/home/demo_10g/Metis_Bringup/metis-bringup-scripts/code"],
        ["Old code","/home/demo_10g/Metis_Bringup/metis-bringup-scripts_cc"],
    ]
elif os.path.exists("/home/idsproj01/trusted/projects/TrEB"):
    wdir = [
        ["cerberus07",    "/home/idsproj01/trusted/projects/TrEB/Design/Cerberus_ASIC/_cad/Digital/user/uenal/syn/chip_cerberus_22fdx_r07"],
        ["cerbKOF",       "/home/idsproj01/trusted/projects/TrEB/Design/Cerberus_ASIC/_cad/Digital/user/kofoed/TReB"],
        ["pattern_an",    "/home/icdaproj01/bcdc_wcc/Design/APEC_01/_cad/backend/pattern_analyzer/2_pnr"],
        ["pattern_gen",   "/home/icdaproj01/bcdc_wcc/Design/APEC_01/_cad/backend/pattern_gen/2_pnr"],
        ["git",           "/home/icdaproj01/bcdc_wcc/Design/APEC_01/_cad/backend/pattern_gen/apecs_wcc_design_36"],
        ["RC7",           "/home/EPI/project/EUPILOT/VEC/usr/esk/pnr_innovus/pcie_r08_v4/INNOVUS/WORK004_vec_top/3_calibre"],
        ["from_WCC",      "/home/icdaproj01/bcdc_wcc/Design/APEC_01/_cad/backend/from_wcc"],
        ["ocean12",       "/home/ocean12/Design/OCEAN_22FDX_02/_cad/digital/atz/pnr_innovus/ocean12_22fdx_02_v18_2eco"],
        ["RC6",           "/home/EPI/project/EUPILOT/VEC/usr/esk/pnr_innovus/pcie_r08_v4/INNOVUS/WORK004_vec_top/calibre_RC6"],
  ]
else:
    raise SystemError("Unknown filesystem")

l0 = max([len(arr[0]) for arr in wdir])

################################################################################
def main():
    if len(sys.argv) > 1:
        print("Select:")
        for i,d in enumerate(wdir):
            print(f"[{i}] {d[0]:{l0}s} {d[1]}")
    else:
        try:
            cmd = int(getch())
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
