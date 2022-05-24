import threading, socket
import threading as thr

mem = []

async def get_setting(setting):
	setting = setting.upper()
	with open('./settings.blr.config') as set_file:
		for x in set_file.read().split('\n'):
			if x.startswith(f'{setting}='):
				return x.lstrip(f"{setting}=")
		return 0

def main():
	while True:
		s = socket.socket().setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADRR).bind(('0.0.0.0',7060)).listen(5)
		


if __name__ == "__main__":
	main()