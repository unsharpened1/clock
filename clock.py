import shutil
from datetime import datetime
from time import sleep

terminal_width, _ = shutil.get_terminal_size()

def print_in_center(width, text):
	print(f'\r{text.center(width)}', end='', flush=True)

while True:
	now = datetime.now()
	time = now.strftime('%d-%m-%Y %H:%M:%S')
	print_in_center(terminal_width, time)
	sleep(1)
