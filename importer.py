from mainGUI import *
import sys
import gc
from os.path import getsize, basename
from os import system
from playsound import playsound
from functools import partial
from _pickle import load, dump
from hurry.filesize import size as convertBytesToReadable
from hurry.filesize import alternative
from notifierP import Notification
from textwrap import wrap
from shutil import copyfile
from emoji import emojize
from time import sleep
