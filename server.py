import socket

ob = socket.socket()
ob.bind(('localhost',2301))
ob.listen(3)
clientobject,add= ob.accept()
print("server is ready")
print('connected with this address',add)

conn=True
while conn:
    gotmsg=clientobject.recv(2012)
    gotmsg.decode('utf-8')
    print(gotmsg)
    if len(gotmsg)==0:
        conn=False
        ob.close()