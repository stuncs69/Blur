import threading, socket
import threading as thr

mem = []

class Buffer:

    def __init__(self,sock):
        self.sock = sock
        self.buffer = b''

    def get_line(self):
        while b'\r\n' not in self.buffer:
            data = self.sock.recv(1024)
            if not data: # socket closed
                return None
            self.buffer += data
        line,sep,self.buffer = self.buffer.partition(b'\r\n')
        return line.decode()

async def get_setting(setting):
	setting = setting.upper()
	with open('./settings.blr.config') as set_file:
		for x in set_file.read().split('\n'):
			if x.startswith(f'{setting}='):
				return x.lstrip(f"{setting}=")
		return 0

def runtime(command):
	y = command.split('--').strip(' ')



def main():
	while True:
		s  = socket.socket().setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADRR).bind(('0.0.0.0',get_setting('port'))).listen(5)
		y, adrr = s.accept()
		print(f'{addr} CONNECT')
		with y:
			z = Buffer(y)
			while True:
				line = b.get_line()
				if line == None:
					break
				runtime(line)
		print(f'{adrr} DISCONNECT')



if __name__ == "__main__":
	main()