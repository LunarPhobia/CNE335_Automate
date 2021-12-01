import os
import paramiko

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        self.server_ip = server_ip

    def ping(self):
        # Use os module to ping the server
        return os.system("ping " + self.server_ip)

    def paramiko(self):
        # creating SSH instance
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.server_ip, 22, 'ec2-user')
        # running commands
        stdin, stdout, stderr = ssh.exec_command('sudo yum update')
        for line in stdout.read().splitlines():
            print(line)
        stdin, stdout, stderr = ssh.exec_command('sudo yum upgrade')
        for line in stdout.read().splitlines():
            print(line)
        # close SSH
        ssh.close();
