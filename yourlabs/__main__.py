#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
YourLabs

A program to facilitate developers on the management of their personal
projects in python.

~~~~~~~~~~~~~~~~~~~~~
Source: https://github.com/KDUser12/YourLabs
(c) 2024 KDUser12
Released under the MIT License
"""

import logging
import argparse

from utils._os import check_os_compatibility
from utils.env import check_python_version
from utils.packages import check_and_install_dependencies


def setup_logging(debug=False):
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('logs.log', mode='a')
        ]
    )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A program to facilitate developers on the management of their personal projects in python.")
    parser.add_argument('--debug', action='store_true', help='enable debug mode')
    
    args = parser.parse_args()
    
    setup_logging(args.debug)
    
    required_versions = ['3.6', '3.7', '3.8']
    logging.debug(f"Required versions : {required_versions}")
    
    try:
        check_os_compatibility()
        check_python_version(required_versions)
    except EnvironmentError as error:
        logging.error(f"Error: {error}")
        exit(1)
        
    check_and_install_dependencies(['requirements.txt'])
    
    