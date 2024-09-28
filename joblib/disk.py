"""
Disk management utilities.
"""
import os
import sys
import time
import errno
import shutil
from multiprocessing import util
try:
    WindowsError
except NameError:
    WindowsError = OSError

def disk_used(path):
    """ Return the disk usage in a directory."""
    pass

def memstr_to_bytes(text):
    """ Convert a memory text to its value in bytes.
    """
    pass

def mkdirp(d):
    """Ensure directory d exists (like mkdir -p on Unix)
    No guarantee that the directory is writable.
    """
    pass
RM_SUBDIRS_RETRY_TIME = 0.1
RM_SUBDIRS_N_RETRY = 10

def rm_subdirs(path, onerror=None):
    """Remove all subdirectories in this path.

    The directory indicated by `path` is left in place, and its subdirectories
    are erased.

    If onerror is set, it is called to handle the error with arguments (func,
    path, exc_info) where func is os.listdir, os.remove, or os.rmdir;
    path is the argument to that function that caused it to fail; and
    exc_info is a tuple returned by sys.exc_info().  If onerror is None,
    an exception is raised.
    """
    pass

def delete_folder(folder_path, onerror=None, allow_non_empty=True):
    """Utility function to cleanup a temporary folder if it still exists."""
    pass