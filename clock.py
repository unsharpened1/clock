import shutil
import sys
from datetime import datetime
from time import sleep

enable_seconds = True if '-s' in sys.argv else False

terminal_width, _ = shutil.get_terminal_size()

def print_in_center(width, text):
	print(f'\r{text.center(width)}', end='', flush=True)

while True:
	try:
		now = datetime.now()
		
		if enable_seconds:
			time = now.strftime('%d-%m-%Y %H:%M:%S')
		else:
			time = now.strftime('%d-%m-%Y %H:%M')
			
		print_in_center(terminal_width, time)
		sleep(1)
	except KeyboardInterrupt:
		exit()
