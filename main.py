# This is the template code for the CNA337 Final Project
# Zachary Rubin, zrubin@rtc.edu
# CNA 337 Fall 2020

from Server import Server

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Nikita Chagay")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    # Change IP address if needed
    object = Server("3.145.30.238")
    # TODO - Call Ping method and print the results
    print(Server.ping(object))
