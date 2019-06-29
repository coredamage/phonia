# Phonia Toolkit
                                                       
               _|                            _|            
     _|_|_|    _|_|_|      _|_|    _|_|_|          _|_|_|  
     _|    _|  _|    _|  _|    _|  _|    _|  _|  _|    _|  
     _|    _|  _|    _|  _|    _|  _|    _|  _|  _|    _|  
     _|_|_|    _|    _|    _|_|    _|    _|  _|    _|_|_|  
     _|                                                    
     _|  Toolkit v1.4

<p align="center">
  <a href="http://entynetproject.simplesite.com/">
    <img src="https://img.shields.io/badge/entynetproject-Ivan%20Nikolsky-blue.svg">
  </a>
  <a href="https://github.com/entynetproject/phonia/releases">
    <img src="https://img.shields.io/github/release/entynetproject/phonia.svg">
  </a>
  <a href="https://ru.m.wikipedia.org/wiki/Python">
    <img src="https://img.shields.io/badge/language-python-blue.svg">
 </a>
  <a href="https://github.com/entynetproject/phonia">
      <img src="https://img.shields.io/badge/gather-PNI-red.svg?maxAge=2592000">
 </a>
  <a href="https://github.com/entynetproject/phonia/issues?q=is%3Aissue+is%3Aclosed">
      <img src="https://img.shields.io/github/issues/entynetproject/phonia.svg">
  </a>
  <a href="https://github.com/entynetproject/phonia/wiki">
      <img src="https://img.shields.io/badge/wiki%20-phonia-lightgrey.svg">
 </a>
  <a href="https://mobile.twitter.com/entynetproject">
    <img src="https://img.shields.io/badge/twitter-entynetproject-blue.svg">
 </a>
</p>

# Phonia toolkit credits

    Name      : Phonia Toolkit
    Developer : Entynetproject
    Version   : v1.4 (phonia-v1.4-dev)
    Gather    : PNI (phone number information)
    Site      : http://entynetproject.simplesite.com/

# About phonia toolkit

    INFO: Phonia Toolkit is one of the most advanced toolkits to scan 
    phone numbers using only free resources. The goal is to first gather 
    standard information such as country, area, carrier and line type on 
    any international phone numbers with a very good accuracy.

# How to install phonia

    INFO: Phonia Toolkit will be installed into /bin and 
    /usr/local/bin as /bin/phonia and /usr/local/bin/phonia!

> cd phonia

> chmod +x install.sh

> ./install.sh

# How to uninstall phonia

> cd phonia

> chmod +x uninstall.sh

> ./uninstall.sh

# How to execute phonia

> phonia -h

    usage: phonia -n <number> [options]

    optional arguments:
      -h, --help            show this help message and exit
      -n number, --number number
                            The phone number to scan.
      -i input_file, --input input_file
                            Phone number list to scan.
      -o output_file, --output output_file
                            Output to save scan results.
      -s scanner, --scanner scanner
                            The scanner to use.
      --recon               Launch custom format reconnaissance.
      --no-ansi             Disable colored output.
      -u, --update          Update Phonia Toolkit.
      --info                Show Phonia Toolkit credits.

# Phonia toolkit examples

> If you want to start basic scan, run
    
    phonia -n +15554443333
    
> If you want to start list scan, run

    phonia -i input.txt -o output.txt
    
> If you want to get number footprints, run

    phonia -n +15554443333 -s footprints

# Terms of use

    This tool is only for educational purposes only.
    Use this tool wisely and never without permission.
    I am not responsible for anything you do with this tool.

# Phonia MIT license

    MIT License

    Copyright (C) 2019, Entynetproject. All Rights Reserved.

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

# Thats all!
