#!/usr/bin/env python
'''
The MIT License (MIT)

Copyright (c) [2015] [Tom Tang]

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
'''

import argparse
import ConfigParser
import sys
import re
import logging




AP = argparse.ArgumentParser("A tool to alter ini config files.")
AP.add_argument("ini", type=str, nargs="+")
AP.add_argument("--set", nargs="+", help='Add items, and it has to be in following format "SECTION.item_name=value"')
AP.add_argument("--del", nargs="+", help='Del section or items, has to be in following format "SECTION.item_name"')
AP.add_argument("-o", "--out", default=None)
AP.add_argument("-v", "--verbose", default=False, help="Enable logging to info level, default is warnning")

def handle_set(cfg, updates):
    pattern = re.compile("([^.]+)\.([^=]+)\=(.*)")
    for i in updates:
        m = pattern.match(i)
        if not m:
            raise Exception(
                '''item: %s does not follow format "SECTION.item_name=value"''' % i)
        if m:
            section, key, value = m.groups()
            cfg.set(section, key, value)


def handle_del(cfg, dels):
    pattern = re.compile("^([^.]+)\.([^$]*)$")
    for i in dels:
        m = pattern.match(i)
        if m:
            section, key = m.groups()
            cfg.remove_option(section, key)
        else:
            section = i
            cfg.remove_section(section)


def main(args):
    try:
        c = ConfigParser.ConfigParser()

        log_level = logging.WARNING
        if args.verbose:
            log_level = args.INFO
        logging.basicConfig(format='%(levelname)-8s:%(message)s',
            level=log_level)

        success = c.read(args.ini)

        logging.info("INI configs parsed: %s" % success)

        if len(success) != len(args.ini):
            failed_lst = [i for i in args.ini  if i not in success]
            raise Exception("Failed to read following ini files: %s" % failed_lst)

        if args.set:
            handle_set(c, args.set)

        if getattr(args, 'del'):
            handle_del(c, getattr(args, 'del'))

        if not args.out:
            c.write(sys.stdout)
            sys.stdout.flush()
        else:
            with open(args.out, "wb") as f:
                c.write(f)

    except Exception, e:
        logging.exception("Failed to process")
        sys.exit(-1)

if __name__ == '__main__':
    main(AP.parse_args())
