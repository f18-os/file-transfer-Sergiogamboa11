# File Transfer Lab
## How to use
To use this program, you must first launch the server, and then the client, which are both defaulted to port 50001
## To use Server
  * To change listenport type -l <port> or --listenport <port> as a parameter in the script
  Example: python fileServer.py -l 50000
  * To use debug mode type -d or --debug as a parameter in the script
  * To use check usage type -? or --usage as a parameter in the script
## To use Client
  * To choose server type -s <port> or --server <port> as a parameter in the script
  Example: python fileClient.py -s 127.0.0.1:50001
  * To use debug mode type -d or --debug as a parameter in the script
  * To use check usage type -? or --usage as a parameter in the script
  * To try to put a file into the server type -p <filename> or --put <filename >as a parameter in the script
  Example: python fileClient.py -p myFile.txt 
The client and server must be using the same port for them to connect, unless you are using the proxy.
Files are read, encoded, and sent to the server, where they are written to a new file in a subdirectory. If the
original file does not exist, has a size of 0, or already exists in the server it is not put into the server.

## Final Note
Everything that I had done so far worked perfectly until I implemented forking into my server. After I added
forking, the server started to act inconsistently and failed to return any data to the client at times. I
have been unable to figure out what the problem is, but it seems to work whenever it feels like it.
