import socket
def layer1(msg1):
    """
    :param: msg1
    :return: a string with msg1 at the start and layer1 10 times after it without any spaces
    """
    return msg1 + "layer1"*10
def layer2(msg2):
    """
    :param msg2:
    :return: : a string with msg2 at the start and _____ 10 times after it without any spaces
    """
    return msg2 + "_____"*10

def layer3(msg3):
    """
    :param msg3:
    :return: : a string with msg3 at the start and 1111111 10 times after it without any spaces
    """
    return msg3 + "1111111"*10

def layer4(msg4):
    """
    :param msg4:
    :return: : a string with msg4 at the start and HaHa 10 times after it without any spaces
    """
    return msg4 + "HaHa"*10

def layer5(msg5):
    """
    :param msg5:
    :return: : a string with msg5 at the start and Last 10 times after it without any spaces
    """
    return msg5 + "Last"*10
my_sock = socket.socket()

#connect to server
try:
    my_sock.connect(("127.0.0.1",1450))
except Exception as e:
    my_sock.close()
    exit(f"server is down - try again {str(e)}")

while True:
    msg = input("enter a message or exit to exit ")
    if msg == "exit":
        my_sock.send(msg.encode())
        break
    msg = layer1(msg)   #create layer1
    msg = layer2(msg)   #create layer2
    msg = layer3(msg)   #create layer3
    msg = layer4(msg)   #create layer4
    msg = layer5(msg)   #create layer5


    try:
        my_sock.send(msg.encode())

    except Exception as e:
        print(f"error in receive or sending data {str(e)}")
        break
my_sock.close()
print("Bye Bye, have a great day!")