#!/usr/bin/env python

import socket
import sys

from minecraft_query import MinecraftQuery

def main():
    try:
        query = MinecraftQuery("server.url.here", 25565,
                               timeout=10,
                               retries=0)
        server_data = query.get_rules()
    except socket.error as e:
        print "socket exception caught:", e.message
        print "Server is down or unreachable."
        sys.exit(1)
    
    print(server_data['motd'])
    
    print(server_data['version'])
    		
    NumPlayers = "Players "
    NumPlayers += str(server_data['numplayers']) + "/"
    NumPlayers += str(server_data['maxplayers']) + " :"
    print(NumPlayers)
    
    Players = server_data['players']
    for player in Players:
    	print("\t"+player)
    
    sys.exit(0)


if __name__=="__main__":
    main()
