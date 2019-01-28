"""
Python 3.7.0
Server for Wallpaper Sync Program (WSP)
Written by: Edgar Araújo
Date (start): 27/01/2019
Date (end):
"""

import socket
import os

HOST, PORT = "localhost", 5000


def send_file_info(filename, connection):
    file_size = os.path.getsize(filename)       # Get file size of (filename) in Bytes
    connection.send((filename + ":" + str(file_size)).encode())     # Send to client (filename):(file_size)


def send_file(filename, connection):
    file_size = os.path.getsize(filename)       # Get file size of (filename) in Bytes
    data_sent = 0       # Variable to track how many bytes have been sent

    with open(filename, "rb") as file:      # Open file in read-bytes mode
        while True:
            data = file.read(1024)      # Read 1024 Bytes of the file
            if not data:        # Close file if there's no data
                break
            connection.send(data)       # Send to client data
            data_sent += len(data)      # Add bytes that have been sent to the tracker variable

    if data_sent == file_size:      # Check integrity of the file sent
        print("File sent successfully.")
    else:
        print("ERROR!")


def main():
    with socket.socket() as s:
        s.bind((HOST, PORT))        # Bind socket to host and port
        s.listen(1)     # Listen for 1 connection

        conn, addr = s.accept()     # Accept connection
        with conn:
            print("Connected to:", addr)

            filename = str(input(">>> ")).strip()       # Get filename to send
            if os.path.isfile(filename):        # If filename exists on the directory
                print(f"File ({filename}) exists.")
                send_file_info(filename, conn)      # Send filename and file size of the file to send (file_info)
                send_file(filename, conn)       # Send file
            else:       # If filename does not exist on the directory
                print(f"File ({filename}) does not exist!")

    input()


if __name__ == '__main__':
    main()
