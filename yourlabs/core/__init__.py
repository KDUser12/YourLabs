import platform
import sys
import os
import datetime
import calendar

from __init__ import __version__
from utils.update import check_versions


class Yourlabs:
    def __init__(self, debug=False):
        self.current_version = __version__
        self.latest_version = check_versions("yourlabs", self.current_version)
        
        self.operating_system = platform.system()
        self.python_version = '.'.join(map(str, sys.version_info[:3]))
        self.current_time = datetime.datetime.now()
        
        self.clear_output()
        
        print(f"YourLabs - {self.current_version}{" [DEBUG-MODE]" if debug else ""} (main, {calendar.month_abbr[self.current_time.month]}"
              f" {self.current_time.day} {self.current_time.year}, {self.current_time.hour}:{self.current_time.minute}) [Python "
              f"{self.python_version}] on {self.operating_system}\nFor more information enter \"help\", \"license\" or \"credit\".\n")
        
        if self.latest_version:
            print("Install the latest YourLabs for new features and improvements! https://github.com/KDUser12/YourLabs/releases/latest\n")
        elif self.latest_version is None:
            print("An error has occurred, please check that you have the latest version! https://github.com/KDUser12/YourLabs/releases/latest\n")
        
        
    def clear_output(self):
        command = 'cls' if os.name == 'nt' else 'clear'
        return os.system(command)
        