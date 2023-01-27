import socket

BYTES_TO_READ = 4096

def get(host, port):
  # create our request
  request_data = b"GET / HTTP/1.1\nHost:" + host.encode('utf-8') + b'\n\n'

  # create our socket
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # we've sent some data on our socket
  s.connect((host, port))
  s.send(request_data)
  # shut down client write, server can stop waiting for more data and read 
  s.shutdown(socket.SHUT_WR)

  # listen for repsonse
  response = s.recv(BYTES_TO_READ)
  while(len(response) > 0):
    print(response)
    response = s.recv(BYTES_TO_READ)

  s.close()

get('www.google.com', 80)