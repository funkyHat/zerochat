import select
import sys
import networkzero as nw0


try:
    input = raw_input
except NameError:
    pass


def main():

    username = input("Please enter your username: ")

    address = nw0.advertise("zerochat_" + username)

    oldchats = {}
    while True:

        chats = {name:address for name, address in nw0.discover_all() if name.startswith("zerochat_")}
        if chats.keys() != oldchats.keys():
            print("New users:")
            print(chats)

        rlist, wlist, elist = select.select([sys.stdin], [], [], 0.1)
        if rlist:
            recipient = sys.stdin.readline()
            msg = input("Message:")
            print("\x1b[31;m[%s] %s\x1b[0m" % (recipient, msg))

            recipient_service = nw0.discover("zerochat_" + recipient)
            nw0.send_message_to(recipient_service, msg)


        received_msg = nw0.wait_for_message_from(address, wait_for_s=0, autoreply=True)
        if received_msg is not None:
            print("Got message: %s" % received_msg)

        oldchats = chats



if __name__ == '__main__':
    main()
