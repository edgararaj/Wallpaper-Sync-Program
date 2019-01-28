"""
Python 3.7.0
Client for Wallpaper Sync Program (WSP)
Written by: Edgar Araújo
Date (start): 27/01/2019
Date (end):
"""

import socket

HOST, PORT = "localhost", 5000


def receive_file(sock, file_info):
    filename = file_info.split(":")[0]      # Split file_info sent by the server into filename ...
    file_size = int(file_info.split(":")[1])    # ... And file_size
    data_received = 0       # Variable to track how many bytes has been received

    with open("wsp_" + filename, "wb") as file:     # Open file in write-bytes mode
        while True:
            data = sock.recv(1024)      # Receive 1024 bytes of data from the server
            if not data:        # Close file if there's no data
                break
            file.write(data)        # Write data to the file
            data_received += len(data)      # Add bytes that have been received to tracker variable

    if data_received == file_size:      # Check integrity of file received
        print("Download complete!")
    else:
        print("ERROR!")


def main():
    with socket.socket() as s:
        s.connect((HOST, PORT))     # Connect to socket in host and port

        file_info = s.recv(1024).decode()       # Receive filename and file size of the file to receive (file_info)
        receive_file(s, file_info)      # Receive file

    input()


if __name__ == '__main__':
    main()
