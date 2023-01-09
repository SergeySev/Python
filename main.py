import socket
# import requests
# import math

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()


# def accept_connection(server_socket):
while True:
    print("Before .accept()")
    client_socket, addr = server_socket.accept()
    print("Connection from", addr)

    while True:
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = 'Hello world\n'.encode()
            client_socket.send(response)
    print('Outside inner while loop')
    client_socket.close()


# def privat24_ex(num):
#     API_PRIVAT = "https://api.privatbank.ua/p24api/pubinfo"
#     parametr = {"json": "", "exchange": "", "coursid": "11"}
#
#     privat_cours = requests.get(API_PRIVAT, params=parametr).json()
#     cusd = float(privat_cours[0]["buy"])
#     ceur = float(privat_cours[1]["buy"])
#     uah_usd = round((num * cusd), 2)
#     uah_eur = round((num * ceur), 2)
#     print("USD", uah_usd, "EUR", uah_eur)
#
#
# privat24_ex(50)