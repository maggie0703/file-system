'''
THIS MODULE INTERACTS WITH THE MEMORY
'''
import time
import xmlrpclib
import pickle
import config
#HANDLE FOR MEMORY OPERATIONS
client=[]
class server0():
    def __init__(self, number):
        self.client=[]
        self.startpoint = number
        self.client0 = xmlrpclib.ServerProxy("http://localhost:"+str(self.startpoint)+"/")
        client.append(self.client0)
    def Initialize_My_FileSystem(self):
        time.sleep(1)
        try:
            state = self.client0.Initialize()
            print("Server0 has been connected")
            print("File System Initializing......")
            print ("File System Initialized!")
            print("\n")
        except:
            print ("Server Is Done!")
            exit (0)



class server1():
    def __init__(self, number):
        self.client=[]
        self.startpoint = number
        self.client1 = xmlrpclib.ServerProxy("http://localhost:"+str(self.startpoint+1)+"/")
        client.append(self.client1)

    def Initialize_My_FileSystem(self):
        time.sleep(1)
        try:
            state = self.client1.Initialize()
            print("Server1 has been connected")
            print("File System Initializing......")
            print ("File System Initialized!")
            print("\n")
        except:
            print ("Server Is Done!")
            exit (0)



class server2():
    def __init__(self, number):
        self.client=[]
        self.startpoint = number
        self.client2 = xmlrpclib.ServerProxy("http://localhost:"+str(self.startpoint+2)+"/")
        client.append(self.client2)

    def Initialize_My_FileSystem(self):
        time.sleep(1)
        try:
            state = self.client2.Initialize()
            print("Server2 has been connected")
            print("File System Initializing......")
            print ("File System Initialized!")
            print("\n")
        except:
            print ("Server Is Done!")
            exit (0)



class server3():
    def __init__(self, number):
        self.client=[]
        self.startpoint = number
        self.client3 = xmlrpclib.ServerProxy("http://localhost:"+str(self.startpoint+3)+"/")
        client.append(self.client3)

    def Initialize_My_FileSystem(self):
        time.sleep(1)
        try:
            state = self.client3.Initialize()
            print("Server3 has been connected")
            print("File System Initializing......")
            print ("File System Initialized!")
            print("\n")
        except:
            print ("Server Is Done!")
            exit (0)


class fcn():
    def inode_number_to_inode0(self,inode_number):
        a1=pickle.dumps(inode_number)
        a2=client[0].inode_number_to_inode(a1)
        return pickle.loads(a2)

    def get_data_block0(self,block_number):
        a1=pickle.dumps(block_number)
        a2=pickle.loads(client[0].get_data_block(a1))
        return ''.join(a2)

    def get_valid_data_block0(self):
        a1=pickle.loads(client[0].get_valid_data_block())
        return a1

    def free_data_block0(self,block_number):
        a1=pickle.dumps(block_number)
        client[0].free_data_block((a1))

    def update_data_block0(self,block_number, block_data):
        a1=pickle.dumps(block_number)
        a2=pickle.dumps(block_data)
        client[0].update_data_block(a1, a2)

    def status0(self):
        print("This is server0")
        a1=pickle.loads(client[0].status())
        return a1

    def update_inode_table0(self,inode, inode_number):
        a1=pickle.dumps(inode)
        a2=pickle.dumps(inode_number)
        client[0].update_inode_table(a1, a2)

    def inode_number_to_inode1(self,inode_number):
        a1=pickle.dumps(inode_number)
        a2=client[1].inode_number_to_inode(a1)
        return pickle.loads(a2)

    def get_data_block1(self,block_number):
        a1=pickle.dumps(block_number)
        a2=pickle.loads(client[1].get_data_block(a1))
        return ''.join(a2)

    def get_valid_data_block1(self):
        a1=pickle.loads(client[1].get_valid_data_block())
        return a1

    def free_data_block1(self,block_number):
        a1=pickle.dumps(block_number)
        client[1].free_data_block((a1))

    def update_data_block1(self,block_number, block_data):
        a1=pickle.dumps(block_number)
        a2=pickle.dumps(block_data)
        client[1].update_data_block(a1, a2)

    def status1(self):
        print("This is server1")
        a1=pickle.loads(client[1].status())
        return a1

    def update_inode_table1(self,inode, inode_number):
        a1=pickle.dumps(inode)
        a2=pickle.dumps(inode_number)
        client[1].update_inode_table(a1, a2)

    def inode_number_to_inode2(self,inode_number):
        a1=pickle.dumps(inode_number)
        a2=client[2].inode_number_to_inode(a1)
        return pickle.loads(a2)

    def get_data_block2(self,block_number):
        a1=pickle.dumps(block_number)
        a2=pickle.loads(client[2].get_data_block(a1))
        return ''.join(a2)

    def get_valid_data_block2(self):
        a1=pickle.loads(client[2].get_valid_data_block())
        return a1

    def free_data_block2(self,block_number):
        a1=pickle.dumps(block_number)
        client[2].free_data_block((a1))

    def update_data_block2(self,block_number, block_data):
        a1=pickle.dumps(block_number)
        a2=pickle.dumps(block_data)
        client[2].update_data_block(a1, a2)

    def status2(self):
        print("This is server2")
        a1=pickle.loads(client[2].status())
        return a1

    def update_inode_table2(self,inode, inode_number):
        a1=pickle.dumps(inode)
        a2=pickle.dumps(inode_number)
        client[2].update_inode_table(a1, a2)

    def inode_number_to_inode3(self,inode_number):
        a1=pickle.dumps(inode_number)
        a2=client[3].inode_number_to_inode(a1)
        return pickle.loads(a2)

    def get_data_block3(self,block_number):
        a1=pickle.dumps(block_number)
        a2=pickle.loads(client[3].get_data_block(a1))
        return ''.join(a2)

    def get_valid_data_block3(self):
        a1=pickle.loads(client[3].get_valid_data_block())
        return a1

    def free_data_block3(self,block_number):
        a1=pickle.dumps(block_number)
        client[3].free_data_block((a1))

    def update_data_block3(self,block_number, block_data):
        a1=pickle.dumps(block_number)
        a2=pickle.dumps(block_data)
        client[3].update_data_block(a1, a2)

    def status3(self):
        print("This is server3")
        a1=pickle.loads(client[3].status())
        return a1

    def update_inode_table3(self,inode, inode_number):
        a1=pickle.dumps(inode)
        a2=pickle.dumps(inode_number)
        client[3].update_inode_table(a1, a2)





