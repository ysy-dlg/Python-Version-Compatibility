import socket
import errno
import pickle

def Main():
	host = 'localhost'
	port = 12345

	all_text = ['text1', 'text2', 'text3']
	music_text = ['Konzert1', 'Konzert2', 'Konzert3']

	all_description = ['Test \n Description1\n', 'Test \n Description1\n', 'Test \n Description1\n']

	all_images = ['unlock.png', 'unlock.png', 'unlock.png']
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
	s.bind((host, port))
	s.listen(1)


	while True:

		c, addr = s.accept()
		c.setblocking(0)

		print "Connection from: " + str(addr)

		try:
			pcommand = c.recv(2048)  # here was the error
		except IOError as e:  # and here it is handeled
			if e.errno == errno.EWOULDBLOCK:
				pass

		command = pickle.loads(pcommand)

		if command[0] == 'GIVEALL':
			textstring = pickle.dumps([all_text, all_images, all_description])#verwandelt Liste in String
			c.send(textstring)

		elif command[0] == 'GIVEMUSIC':
			textstring = pickle.dumps([music_text, all_images, all_description])#verwandelt Liste in String
			c.send(textstring)

		elif command[0] == 'ADD':
			try:
				new_event = pickle.loads(command)
				print new_event
				caption = command[1]
				image = command[2]
				describtion = command[3]
				city = command[4]
				#add to SQL
			except:
				pass

		try:
			c.close()
			#s.setsockopt(socket.AF_INET, socket.SOCK_STREAM, 1)
			s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		except socket.error as e:
			if e.errno != errno.ECONNRESET:
				raise
			pass

if __name__ == '__main__':
    Main()