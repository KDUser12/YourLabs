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
import logging.handlers
import os

from utils._os import check_os_compatibility
from utils.env import check_python_version

# Configure logging
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()

logging.basicConfig(
    level=LOG_LEVEL,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('logs.log', mode='a')
    ]
)

if __name__ == '__main__':
    required_versions = ['3.6', '3.7', '3.8']
    logging.debug(f"Required versions : {required_versions}")
    
    try:
        check_os_compatibility()
        check_python_version(required_versions)
    except EnvironmentError as error:
        logging.error(f"Error: {error}")
        exit(1)
        