
import networkzero as nw0


def main():
    
    username = raw_input("Please enter your username: ")
    
    address = nw0.advertise("zerochat_" + username)
    
    oldchats = {}
    while True:
        
        chats = {name:address for name, address in nw0.discover_all() if name.startswith("zerochat_")}
        if chats.keys() != oldchats.keys():
            print "New users:"
            print chats
        
        
        oldchats = chats
        


if __name__ == '__main__':
    main()