# This is the template code for the CNA337 Final Project
# Zachary Rubin, zrubin@rtc.edu
# CNA 337 Fall 2020

from Server import Server

def print_program_info():
    print("Server Automator v0.1 by Nikita Chagay")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # Change IP address if needed
    object = Server("13.58.74.211")
    # Call Ping and paramiko methods and print the results
    print(Server.ping(object))
    Server.paramiko(object)


