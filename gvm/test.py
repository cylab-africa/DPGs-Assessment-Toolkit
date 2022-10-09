from gvm.connections import SSHConnection
from gvm.protocols.latest import Osp

# path to unix socket
path = '/run/ospd/ospd.sock'
connection = SSHConnection(hostname='172.19.0.2', port=22, username='gmp', password='')
osp = Osp(connection=connection)

# using the with statement to automatically connect and disconnect to ospd
with osp:
    # get the response message returned as a utf-8 encoded string
    response = osp.get_version()

    # print the response message
    print(response)
