import MemoryInterface, AbsolutePathNameLayer,time,config

def Initialize_My_FileSystem():
    s0.Initialize_My_FileSystem()
    s1.Initialize_My_FileSystem()
    s2.Initialize_My_FileSystem()
    s3.Initialize_My_FileSystem()
    AbsolutePathNameLayer.AbsolutePathNameLayer0().new_entry('/', 1)
    AbsolutePathNameLayer.AbsolutePathNameLayer1().new_entry('/', 1)
    AbsolutePathNameLayer.AbsolutePathNameLayer2().new_entry('/', 1)
    AbsolutePathNameLayer.AbsolutePathNameLayer3().new_entry('/', 1)


# HANDLE TO ABSOLUTE PATH NAME LAYER
interface0 = AbsolutePathNameLayer.AbsolutePathNameLayer0()
interface1 = AbsolutePathNameLayer.AbsolutePathNameLayer1()
interface2 = AbsolutePathNameLayer.AbsolutePathNameLayer2()
interface3 = AbsolutePathNameLayer.AbsolutePathNameLayer3()


class FileSystemOperations():

    # MAKES NEW DIRECTORY
    def mkdir(self, path):
        interface0.new_entry(path, 1)
        interface1.new_entry(path, 1)
        interface2.new_entry(path, 1)
        interface3.new_entry(path, 1)

    # CREATE FILE
    def create(self, path):
        interface0.new_entry(path, 0)
        interface1.new_entry(path, 0)
        interface2.new_entry(path, 0)
        interface3.new_entry(path, 0)

    # WRITE TO FILE
    def write(self, path, data, index, delay,offset=0):
        if index == 1:
            time.sleep(delay)
            try:
                interface0.write(path, offset, data)
                print('Data is being written into server0.')
                self.f1=0

            except:
                print ('Server0 did not respond. ')
                self.f1=-1


            print('waiting to write into another replica')
            time.sleep(5)
            try:
                interface1.write(path, offset, data)
                print('Data is being written into server1.')
                self.f2=1

            except:
                print ('Server1 did not respond. ')
                self.f2=-1

        elif index==2:
            time.sleep(delay)
            try:
                interface1.write(path, offset, data)
                print('Data is being written into server1.')
                self.f1=1
            except:
                print('Server1 did not respond. ')
                self.f1=-1

            print('waiting to write into another replica')
            time.sleep(5)
            try:
                interface2.write(path, offset, data)
                print('Data is being written into server2.')
                self.f2=2
            except:
                print('Server2 did not respond. ')
                self.f2=-1
        elif index==3:
            time.sleep(delay)
            try:
                interface2.write(path, offset, data)
                print('Data is being written into server2.')
                self.f1=2
            except:
                print('Server2 did not respond. ')
                self.f1=-1

            print('waiting to write into another replica')
            time.sleep(5)
            try:
                interface3.write(path, offset, data)
                print('Data is being written into server3.')
                self.f2=3
            except:
                print('Server3 did not respond. ')
                self.f2=-1

        else:
            time.sleep(delay)
            try:
                interface3.write(path, offset, data)
                print('Data is being written into server3.')
                self.f1=3
            except:
                print('Server3 did not respond. ')
                self.f1=-1

            print('waiting to write into another replica')
            time.sleep(5)
            try:
                interface0.write(path, offset, data)
                print('Data is being written into server0.')
                f2=0
            except:
                print('Server0 did not respond. ')
                f2=-1
        return self.f1,self.f2

    # READ
    def read(self, path, index, count, offset=0, size=-1):
        if index == 1:
            if count % 2 == 1:
                print ('odd read')
                try:
                    read_buffer0 = interface0.read(path, offset, size)
                    if read_buffer0 != -1: print(path + " : " + read_buffer0)
                    print('Read from server0')

                except:
                    time.sleep(5)
                    read_buffer1 = interface1.read(path, offset, size)
                    if read_buffer1 != -1: print(path + " : " + read_buffer1)
                    print('Server0 did not respond. ')
                    print('Read from server1.')

            else:
                print ('even read')
                try:
                    read_buffer1 = interface1.read(path, offset, size)
                    if read_buffer1 != -1: print(path + " : " + read_buffer1)

                    print('Read from server1')
                except:
                    time.sleep(5)
                    read_buffer0 = interface0.read(path, offset, size)
                    if read_buffer0 != -1: print(path + " : " + read_buffer0)
                    print('Server1 did not respond. ')
                    print('Read from server0.')

        elif index==2:
            if count % 2 == 1:
                print ('odd read')
                try:
                    read_buffer1 = interface1.read(path, offset, size)
                    if read_buffer1 != -1: print(path + " : " + read_buffer1)
                    print('Read from server1')

                except:
                    time.sleep(5)
                    read_buffer2 = interface2.read(path, offset, size)
                    if read_buffer2 != -1: print(path + " : " + read_buffer2)
                    print('Server1 did not respond. ')
                    print('Read from server2.')

            else:
                print ('even read')
                try:
                    read_buffer2 = interface2.read(path, offset, size)
                    if read_buffer2 != -1: print(path + " : " + read_buffer2)
                    print('Read from server2')

                except:
                    time.sleep(5)
                    read_buffer1 = interface1.read(path, offset, size)
                    if read_buffer1 != -1: print(path + " : " + read_buffer1)
                    print('Server2 did not respond. ')
                    print('Read from server1.')

        elif index == 3:
            if count % 2 == 1:
                print('odd read')
                try:
                    read_buffer2 = interface2.read(path, offset, size)
                    if read_buffer2 != -1: print(path + " : " + read_buffer2)
                    print('Read from server2')

                except:
                    time.sleep(5)
                    read_buffer3 = interface3.read(path, offset, size)
                    if read_buffer3 != -1: print(path + " : " + read_buffer3)
                    print('Server2 did not respond. ')
                    print('Read from server3.')

            else:
                print('even read')
                try:
                    read_buffer3 = interface3.read(path, offset, size)
                    if read_buffer3 != -1: print(path + " : " + read_buffer3)
                    print('Read from server3')

                except:
                    time.sleep(5)
                    read_buffer2 = interface1.read(path, offset, size)
                    if read_buffer2 != -1: print(path + " : " + read_buffer2)
                    print('Server3 did not respond. ')
                    print('Read from server3.')


        else:
            if count % 2 == 1:
                print ('odd read')
                try:
                    read_buffer3 = interface3.read(path, offset, size)
                    if read_buffer3 != -1: print(path + " : " + read_buffer3)
                    print('Read from server3')

                except:
                    time.sleep(5)
                    read_buffer0 = interface0.read(path, offset, size)
                    if read_buffer0 != -1: print(path + " : " + read_buffer0)
                    print('Server3 did not respond. ')
                    print('Read from server0.')

            else:
                print ('oven read')
                try:
                    read_buffer0 = interface0.read(path, offset, size)
                    if read_buffer0 != -1: print(path + " : " + read_buffer0)
                    print('Read from server0')

                except:
                    time.sleep(5)
                    read_buffer3 = interface3.read(path, offset, size)
                    if read_buffer3 != -1: print(path + " : " + read_buffer3)
                    print('Server0 did not respond. ')
                    print('Read from server3.')




    # DELETE
    def rm(self, path):
        interface0.unlink(path)
        interface1.unlink(path)
        interface2.unlink(path)
        interface3.unlink(path)

    # MOVING FILE
    def mv(self, old_path, new_path):
        interface0.mv(old_path, new_path)
        interface1.mv(old_path, new_path)
        interface2.mv(old_path, new_path)
        interface3.mv(old_path, new_path)

    # CHECK STATUS
    def status(self):
        print(function.status0())
        print(function.status1())
        print(function.status2())
        print(function.status3())


if __name__ == '__main__':
    my_object = FileSystemOperations()
    pointi = raw_input("Please input the port number:")
    s0=MemoryInterface.server0(int(pointi))
    s1=MemoryInterface.server1(int(pointi))
    s2=MemoryInterface.server2(int(pointi))
    s3=MemoryInterface.server3(int(pointi))
    Initialize_My_FileSystem()
    function = MemoryInterface.fcn()
    start = True
    index_dict=dict()  #index assigns where a file should be stored
    count_dict=dict()
    count=1
    r_count=dict()   #read times
    s_num=dict()

    while(start==True):
        print ('Please input a command:')
        command=raw_input('$ ')
        command_array=command.split(' ')
        if command_array[0]=='mkdir':
            try:
                my_object.mkdir(command_array[1])
            except:
                print ('error')
        elif command_array[0]=='create':
            try:
                my_object.create(command_array[1])
            except:
                print ('error')
        elif command_array[0] == "write":
            starttime = time.time()
            try:
                file = command_array[1]
                if list(index_dict.keys()).count(file)==0:
                    count_dict[file]=count
                    count+=1
                if count_dict[file] % 4 == 1:
                    index = 1
                    s_num[file]=[0,1]
                elif count_dict[file] % 4 == 2:
                    index = 2
                    s_num[file]=[1,2]
                elif count_dict[file] % 4 == 3:
                    index = 3
                    s_num[file]=[2,3]
                else:
                    index = 4
                    s_num[file]=[3,0]
                index_dict[file]=index
                data = command_array[2]
                delay=1
                offset=int(command_array[3])

                if list(s_num.keys()).count(file)==0:
                    if index==4:
                        print('write into servers:' + str(index - 1) + ',' + str(0))
                    else:
                        print('write into servers:' + str(index - 1) + ',' + str(index))
                else:
                    list0=s_num[file]
                    if -1 in list0:
                        list0.remove(-1)
                        print ('write into servers:'+str(list0[0]))
                    else:
                        print ('write into servers:'+str(list0[0])+','+str(list0[1]))
                f1,f2=my_object.write(file, data, index_dict[file],delay,offset)
                s_num[file]=[f1,f2]
            except:
                print('error')
            endtime = time.time()
            print('running time:%.6fs' % (endtime - starttime))
        elif command_array[0] == "read":
            try:
                file = command_array[1]
                offset = int(command_array[2])
                length = int(command_array[3])
                index=int(index_dict[file])
                if list(r_count.keys()).count(file)==0:
                    r_count[file] = 1
                else:
                    count=r_count[file]
                    count+=1
                    r_count[file]=count
                list0 = s_num[file]
                if -1 in list0:
                    list0.remove(-1)
                    print('Data in servers:' + str(list0[0]))
                else:
                    print('Data in servers:' + str(list0[0]) + ',' + str(list0[1]))
                my_object.read(file, index, r_count[file],offset, length)
            except:
                print ('error')
        elif command_array[0]=='mv':
            try:
                file=command_array[1]
                dest=command_array[2]
                try:
                    value = index_dict[file]
                    list0 = s_num[file]
                    my_object.mv(file, dest)
                    del index_dict[file]
                    index_dict[dest]=value
                    del s_num[file]
                    s_num[dest]=list0
                except KeyError:
                    my_object.mv(file, dest)  #mv the file when the file is created without being written
            except:
                print ('error')
        elif command_array[0]=='rm':
            try:
                file=command_array[1]
                try:
                    del index_dict[file]
                    del s_num[file]
                    my_object.rm(file)
                except KeyError:
                    my_object.rm(file)   #delete the file when the file is created firstly without bing written
            except:
                print ('error')

        elif command=='status':
            my_object.status()
        elif command=='exit':
            print ('Exit')
            start=False









