import csv
import os
import sys
import time
import datetime

from ctypes import (
    POINTER,
    c_float,
    c_uint16,
    c_uint32,
    cast,
    cdll,
    create_string_buffer,
    sizeof,
    memset,
)
from typing import List, Tuple

from keycodes import get_usb_code

class Wrapper(object):
	"""
	ctypes interface to interact with the Wooting Analog SDK
	"""
	def __init__(self):
		path = os.getcwd()
		try:
			if sys.platform.startswith('win'):
				self._lib = cdll.LoadLibrary(os.path.join(path, 'wooting_analog_wrapper.dll'))
			elif sys.platform.startswith('linux'):
				# you need udev rules for this to work on linux
				# https://help.wooting.io/article/147-configuring-device-access-for-wootility-under-linux-udev-rules
				self._lib = cdll.LoadLibrary(os.path.join(path, 'libwooting_analog_wrapper.so'))

			else:
				# mac os is not supported
				raise OSError("Unsupported platform: {}".format(sys.platform))
		except OSError as e:
			sys.exit(f'Failed to load SDK wrapper. Is Wootlitly installed?')

	def read_key(self, code: int) -> float:
		"""
		Read the analog value of a single key.
		"""
		return self._lib.wooting_analog_read_analog(code) 


if __name__ == "__main__":
	wp = Wrapper()
	while True:
		print(wp.read_key(41))
		time.sleep(0.1)