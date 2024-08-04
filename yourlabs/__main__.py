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

# Configure logging
LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG').upper()

logging.basicConfig(
    level=LOG_LEVEL,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('logs/os_compatibility.log', mode='a')
    ]
)

if __name__ == '__main__':
    try:
        check_os_compatibility()
    except EnvironmentError as error:
        logging.error(f"Error: {error}")
        exit(1)
        