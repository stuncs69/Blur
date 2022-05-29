import threading, socket
import threading as thr

mem = []

from cryptography.fernet import Fernet

class Encr:
	def __init__(self,key):
		self.key = key
	
	def encrypt(self,data):
		f = Fernet(self.key)
		return f.encrypt(data)
	
	def decrypt(self,data):
		f = Fernet(self.key)
		return f.decrypt(data)


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

def get_setting(setting):
	setting = setting.upper()
	with open('./settings.blr.config') as set_file:
		for x in set_file.read().split('\n'):
			if x.startswith(f'{setting}='):
				return x.lstrip(f"{setting}=")
		return 0

def runtime(command):
	y = command.split('--').strip(' ')
	main_cmd = command.split(' ')[0]
	valid_commands = ['chvar','advar','dlvar','rnvar']
	z = [] # assigned for data and options
	if main_cmd in valid_commands:
		for x in y:
			b = x.split('=')
			x = x.lstrip(f"{b[0]}=").strip('"')
			z.append({f'{b[0]}':x})
		if main_cmd.startswith('chvar'):
			
		
	else:
		return 0



def main():
	while True:
		s  = socket.socket().setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADRR).bind(('0.0.0.0',get_setting('port'))).listen(5)
		y, adrr = s.accept()
		print(f'{adrr} CONNECT')
		with y:
			z = Buffer(y)
			while True:
				line = z.get_line()
				if line == None:
					break
				thr.Thread(target=runtime,args=(line)).start()
				runtime(line)
		print(f'{adrr} DISCONNECT')



if __name__ == "__main__":
	main()