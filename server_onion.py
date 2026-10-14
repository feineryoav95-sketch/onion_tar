import socket
#create the server
server_soc = socket.socket()
server_soc.bind(("0.0.0.0",1450))
server_soc.listen(3)

def remLayer1(msg):
    """

    :param msg:
    :return: the string without layer1
    """
    return msg[0:-1*(10*len("layer1")):1]
def remLayer2(msg):
    """

    :param msg:
    :return: the string without layer2
    """
    return msg[0:-1*(10*len("_____")):1]
def remLayer3(msg):
    """

    :param msg:
    :return: the string without layer3
    """
    return msg[0:-1*(10*len("1111111")):1]
def remLayer4(msg):
    """

    :param msg:
    :return: the string without layer4
    """
    return msg[0:-1*(10*len("HaHa")):1]
def remLayer5(msg):
    """

    :param msg:
    :return: the string without layer5
    """
    return msg[0:-1 * (10 * len("last")):1]
while True:
    client_soc, addr = server_soc.accept()
    print(f"{addr[0]} - connected")
    while True:
        try:
            data = client_soc.recv(1024).decode()
            if data == "exit":
                break
            else:
                if data.lower() == "exit":
                    break
                data = remLayer5(data)  #remove layer1
                data = remLayer4(data)  #remove layer2
                data = remLayer3(data)  #remove layer3
                data = remLayer2(data)  #remove layer4
                data = remLayer1(data)  #remove layer5
                print(data)



        except Exception as e:
            print(f"error in recv/send {str(e)}")
            break
    print(f"{addr[0]} - disconnected")
    client_soc.close()