#! /usr/bin/env python3
import sys, os
sys.path.append("../lib")       # for params
import re, socket, params

switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50001),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )

progname = "echoserver"
paramMap = params.parseParams(switchesVarDefaults)

debug, listenPort = paramMap['debug'], paramMap['listenPort']

if paramMap['usage']:
    params.usage()

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # listener socket
if not isinstance(listenPort, int):
    listenPort = int(listenPort)
bindAddr = ("127.0.0.1", listenPort)
lsock.bind(bindAddr)
lsock.listen(5)
print("listening on:", bindAddr)

sock, addr = lsock.accept()

print("connection rec'd from", addr)


from framedSock import framedSend, framedReceive

while True:
    payload = framedReceive(sock, debug)

    if payload:
        if "::" in payload.decode("utf-8"):
            decodedPayload = payload.decode("utf-8")
            fileName = decodedPayload.split('::')[0]
            contents = decodedPayload.split('::')[1]
            file = os.getcwd() + "/serverFolder/" + fileName
            f = open(file, "w")
            f.write(contents)

    if debug: print("rec'd: ", payload)
    if not payload:
        break
    payload += b"!"             # make emphatic!
    framedSend(sock, payload, debug)