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
	def __init__(self, key1, key2):
		# key 1 and key 2 are the keys that will be read
		# they should be the USB HID codes of the keys to be read
		self.key1 = key1
		self.key2 = key2

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

		result = self._lib.wooting_analog_initialise()
		if result < 0:
			sys.exit(f'Failed to initialise Wooting Analog SDK')

		self.buffer_size = 105
        # create ctypes buffers for calling read_full_buffer
		self.code_buffer = cast(create_string_buffer(self.buffer_size * sizeof(c_uint16)), POINTER(c_uint16))
		self.analog_buffer = cast(create_string_buffer(self.buffer_size * sizeof(c_float)), POINTER(c_float))
	
	def read_full_buffer(self):
		"""
		Read the analog values of all keys.

		Returns tuple of two floats, the analog values of the two keys

		"""
		memset(self.code_buffer, 0, self.buffer_size * sizeof(c_uint16))
		memset(self.analog_buffer, 0, self.buffer_size * sizeof(c_float))
		result = self._lib.wooting_analog_read_full_buffer(self.code_buffer, self.analog_buffer, c_uint32(self.buffer_size))

		output = [0,0]
		if result < 0:
			print(f'Failed to read full buffer with error {result}')
			return output
		else:
			# if there is not error, result is the amout buffer areas populated
			for i in range(result):
				if (self.code_buffer[i] == self.key1):
					output[0] = self.analog_buffer[i]
				elif (self.code_buffer[i] == self.key2):
					output[1] = self.analog_buffer[i]

			return output


if __name__ == "__main__":
	# for testing
	wp = Wrapper(get_usb_code('x'), get_usb_code('c'))
	while True:
		print(wp.read_full_buffer())
		time.sleep(0.1)