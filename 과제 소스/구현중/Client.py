# telnet program example 
import socket, select, string, sys 
   
def prompt() : 
     sys.stdout.write('<You> ') 
     sys.stdout.flush() 
   
#main function 
if __name__ == "__main__": 
       
     if(len(sys.argv) < 3) : 
         print 'Usage : python chat_client.py hostname port'
         print sys.argv
         sys.exit()
       
     host = sys.argv[1] 
     port = int(sys.argv[2]) 
       
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
     s.settimeout(2) 
       
     # connect to remote host 
     try : 
         s.connect((host, port)) 
     except : 
         print 'Unable to connect'
         sys.exit() 
       
     print 'Connected to remote host. Start sending messages'
     prompt() 
       

     while 1:
	print 'ID plz'
	ID = sys.stdin.readline()
	print 'PW plz'
	PW = sys.stdin.readline()
	s.send('log' + '\\' + ID + '\\' + PW)
	sys.stdout.flush()

	if s.recv(4096) == 'ok':
		print 'log ok'
		break;
	else:
		print 'log failed'

     while 1: 
         socket_list = [sys.stdin, s] 
           
         # Get the list sockets which are readable 
         read_sockets, write_sockets, error_sockets = select.select(socket_list , [], []) 
           
         for sock in read_sockets: 
             #incoming message from remote server 
             if sock == s: 
                 data = sock.recv(4096) 
                 if not data : 
                     print '\nDisconnected from chat server'
                     sys.exit() 
                 else : 
                     #print data 
                     sys.stdout.write(data) 
                     prompt() 
             #user entered a message 
             else : 
                 msg = sys.stdin.readline() 
                 s.send(msg) 
                 prompt() 
