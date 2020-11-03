from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

class FileHandler(FileSystemEventHandler):
    def file_event(self, event):
        for filename in os.listdir('C:\Users\mathe\Downloads'):
            src = 'C:\Users\mathe\Downloads' + '/' + filename
            