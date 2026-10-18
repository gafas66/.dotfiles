#! /usr/bin/env python3
################################################################################
# Created: Saturday, September 19 2026
# Author: , ESK

import re
import sys
import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(sys.argv[1])
    page.get_by_role("textbox").fill("17479608")
    page.get_by_role("button").click()
    page.get_by_role("link",name="Connected devices").click()
    time.sleep(25)
    aria = page.aria_snapshot()
    page.get_by_text("Log out").click()
    browser.close()

for line in aria.split('\n'):
    m = re.search(r"- row \"(\S+)",line)
    if m: print(m.group(1))
    
# End of file
################################################################################
# Local Variables:
# comment-column: 60
# End:
################################################################################
