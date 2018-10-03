#! /usr/bin/env python3

# Echo client program
import socket, sys, re, os

sys.path.append("../lib")       # for params
import params

from framedSock import framedSend, framedReceive


switchesVarDefaults = (
    (('-s', '--server'), 'server', "127.0.0.1:50000"),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    (('-p', '--put'), 'file', " ")
    )

progname = "framedClient"
paramMap = params.parseParams(switchesVarDefaults)

server, usage, debug, file  = paramMap["server"], paramMap["usage"], paramMap["debug"], paramMap["file"]

if usage:
    params.usage()

try:
    serverHost, serverPort = re.split(":", server)
    serverPort = int(serverPort)
except:
    print("Can't parse server:port from '%s'" % server)
    sys.exit(1)

s = None
for res in socket.getaddrinfo(serverHost, serverPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        print("creating sock: af=%d, type=%d, proto=%d" % (af, socktype, proto))
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        print(" error: %s" % msg)
        s = None
        continue
    try:
        print(" attempting to connect to %s" % repr(sa))
        s.connect(sa)
    except socket.error as msg:
        print(" error: %s" % msg)
        s.close()
        s = None
        continue
    break

if s is None:
    print('could not open socket')
    sys.exit(1)

if os.path.exists(file) and file!=" ":
    inFile = file
    f = open(inFile, "r")
    outMessage = f.read();
    outMessage = outMessage.replace("\n", "\\n")
else:
    outMessage = "File not found"
outMessageB = bytes(outMessage, encoding= 'utf-8')

print("sending " + outMessage)
framedSend(s, outMessageB, debug)
inMessage = bytes(framedReceive(s, debug).decode("utf-8").replace("\\n", "\n"), encoding= 'utf-8')
print("received:", inMessage)
