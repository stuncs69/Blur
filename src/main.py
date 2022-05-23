import threading, sockets
import threading as thr

mem = []

async def get_setting(setting):
	with open('./settings.blr.config') as set_file:
		for x in set_file.read().split('\n'):
			if x.startswith(f'{setting}='):
				return x.rstrip(f"{setting}=")
		return 0

