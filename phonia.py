#!/usr/bin/env python3

# MIT License

# Copyright (C) 2019, Entynetproject. All Rights Reserved.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# dependencies
import sys
import signal
import os
import time
# lib
from lib.args import args,parser
from lib.banner import banner, __version__
from lib.output import *
from lib.format import *
from lib.logger import Logger
from lib.googlesearch import closeBrowser
# scanners
from scanners import numverify
from scanners import localscan
from scanners import ovh
from scanners.footprints import osintScan
from scanners import recon

def scanNumber(InputNumber):
    os.system("clear")
    os.system("cat banner/banner.txt")
    print("")
    time.sleep(3)
    title("[!] ---- Fetching informations for {} ---- [!]".format(formatNumber(InputNumber)))
    time.sleep(5)

    number = localscan.scan(InputNumber)

    if not number:
        throw(("Error: an error occured parsing {}. Skipping.".format(
            formatNumber(InputNumber))))

    numverify.scan(number['default'])
    ovh.scan(number['local'], number['countryIsoCode'])
    recon.scan(number)
    osintScan(number)

    info("Scan finished.\n")


def main():
    scanners = ['any', 'all', 'numverify', 'ovh', 'footprints']
    
    if args.update:
        os.system("cd ~ && chmod +x phonia/bin/phonia && phonia/bin/phonia -u")
        sys.exit()

    banner()

    # Ensure the usage of Python3
    if sys.version_info[0] < 3:
        print(
            "(!) Please run the tool using Python 3")
        sys.exit()

    # If any param is passed, execute help command
    if not len(sys.argv) > 1:
        parser.print_help()
        sys.exit()
    elif args.info:
        os.system("cat banner/banner1.txt")
        sys.exit()

    if args.output:
        sys.stdout = Logger()
        
    # Verify scanner option
    if not args.scanner in scanners:
        print(("Error: scanner doesn't exists."))
        sys.exit()

    if args.number:
        scanNumber(args.number)
    elif args.input:
        for line in args.input.readlines():
            scanNumber(line)
    else:
        parser.print_help()
        sys.exit()

    if args.output:
        args.output.close()

    closeBrowser()


def signal_handler(signal, frame):
    print('\n[-] You pressed Ctrl+C! Exiting...')

    closeBrowser()

    sys.exit()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()
