'''
THIS MODULE ACTS AS A INODE NUMBER LAYER. NOT ONLY IT SHARES DATA WITH INODE LAYER, BUT ALSO IT CONNECTS WITH MEMORY INTERFACE FOR INODE TABLE 
UPDATES. THE INODE TABLE AND INODE NUMBER IS UPDATED IN THE FILE SYSTEM USING THIS LAYER
'''
import InodeLayer, config, MemoryInterface, datetime, InodeOps
#HANDLE OF INODE LAYER
interface0 = InodeLayer.InodeLayer0()
interface1 = InodeLayer.InodeLayer1()
interface2 = InodeLayer.InodeLayer2()
interface3 = InodeLayer.InodeLayer3()

functions=MemoryInterface.fcn()

class InodeNumberLayer0():

	#PLEASE DO NOT MODIFY
	#ASKS FOR INODE FROM INODE NUMBER FROM MemoryInterface.(BLOCK LAYER HAS NOTHING TO DO WITH INODES SO SEPERTAE HANDLE)
	def INODE_NUMBER_TO_INODE(self, inode_number):
		array_inode = functions.inode_number_to_inode0(inode_number)
		inode = InodeOps.InodeOperations().convert_array_to_table(array_inode)
		if inode: inode.time_accessed = datetime.datetime.now()   #TIME OF ACCESS
		return inode


	#PLEASE DO NOT MODIFY
	#RETURNS DATA BLOCK FROM INODE NUMBER
	def INODE_NUMBER_TO_BLOCK(self, inode_number, offset, length):
		inode = self.INODE_NUMBER_TO_INODE(inode_number)
		if not inode:
			print("Error InodeNumberLayer: Wrong Inode Number! \n")
			return -1
		return interface0.read(inode, offset, length)


	#PLEASE DO NOT MODIFY
	#UPDATES THE INODE TO THE INODE TABLE
	def update_inode_table(self, table_inode, inode_number):
		if table_inode: table_inode.time_modified = datetime.datetime.now()  #TIME OF MODIFICATION
		array_inode = InodeOps.InodeOperations().convert_table_to_array(table_inode)
		functions.update_inode_table0(array_inode, inode_number)


	#PLEASE DO NOT MODIFY
	#FINDS NEW INODE INODE NUMBER FROM FILESYSTEM
	def new_inode_number(self, type, parent_inode_number, name):
		if parent_inode_number != -1:
			parent_inode = self.INODE_NUMBER_TO_INODE(parent_inode_number)
			if not parent_inode:
				print("Error InodeNumberLayer: Incorrect Parent Inode")
				return -1
			entry_size = config.MAX_FILE_NAME_SIZE + len(str(config.MAX_NUM_INODES))
			max_entries = (config.INODE_SIZE - 79 ) / entry_size
			if len(parent_inode.directory) == max_entries:
				print("Error InodeNumberLayer: Maximum inodes allowed per directory reached!")
				return -1
		for i in range(0, config.MAX_NUM_INODES):
			if self.INODE_NUMBER_TO_INODE(i) == False: #FALSE INDICTES UNOCCUPIED INODE ENTRY HENCE, FREEUMBER
				inode = interface0.new_inode(type)
				inode.name = name
				self.update_inode_table(inode, i)
				return i
		print("Error InodeNumberLayer: All inode Numbers are occupied!\n")


	#LINKS THE INODE
	def link(self, inode_number):
		inode = self.INODE_NUMBER_TO_INODE(inode_number)  # return inode
		return inode

	#REMOVES THE INODE ENTRY FROM INODE TABLE
	def unlink(self, inode_number):
		inode = self.INODE_NUMBER_TO_INODE(inode_number)
		# print ('inode link',inode.links)
		if inode.links == 0:  # if reference count is 0, then free block and inode
			# print (inode.blk_numbers)
			interface0.free_data_block(inode, 0)
			# print ("inode being deleted", inode_number)
			self.update_inode_table(False, inode_number)


	#IMPLEMENTS WRITE FUNCTIONALITY
	def write(self, inode_number, offset, data, parent_inode_number):
		inode = self.INODE_NUMBER_TO_INODE(inode_number)  # find inode according inode number
		interface0.write(inode, offset, data)  # write data to block
		self.update_inode_table(inode, inode_number)  # update inode table



	#IMPLEMENTS READ FUNCTIONALITY
	def read(self, inode_number, offset, length, parent_inode_number):
		inode = self.INODE_NUMBER_TO_INODE(inode_number)  # find inode according inode number
		inode, data = interface0.read(inode, offset, length)  # read data from block
		self.update_inode_table(inode, inode_number)  # update inode table
		return data


class InodeNumberLayer1():

	#PLEASE DO NOT MODIFY
	#ASKS FOR INODE FROM INODE NUMBER FROM MemoryInterface.(BLOCK LAYER HAS NOTHING TO DO WITH INODES SO SEPERTAE HANDLE)
	def INODE_NUMBER_TO_INODE(self, inode_number):
		array_inode = functions.inode_number_to_inode1(inode_number)
		inode = InodeOps.InodeOperations().convert_array_to_table(array_inode)
		if inode: inode.time_accessed = datetime.datetime.now()   #TIME OF ACCESS
		return inode


	#PLEASE DO NOT MODIFY
	#RETURNS DATA BLOCK FROM INODE NUMBER
	def INODE_NUMBER_TO_BLOCK(self, inode_number, offset, length):
		inode = self.INODE_NUMBER_TO_INODE(inode_number)
		if not inode:
			print("Error InodeNumberLayer: Wrong Inode Number! \n")
			return -1
		return interface1.read(inode, offset, length)


	#PLEASE DO NOT MODIFY
	#UPDATES THE INODE TO THE INODE TABLE
	def update_inode_table(self, table_inode, inode_number):
		if table_inode: table_inode.time_modified = datetime.datetime.now()  #TIME OF MODIFICATION
		array_inode = InodeOps.InodeOperations().convert_table_to_array(table_inode)
		functions.update_inode_table1(array_inode, inode_number)


	#PLEASE DO NOT MODIFY
	#FINDS NEW INODE INODE NUMBER FROM FILESYSTEM
	def new_inode_number(self, type, parent_inode_number, name):
		if parent_inode_number != -1:
			parent_inode = self.INODE_NUMBER_TO_INODE(parent_inode_number)
			if not parent_inode:
				print("Error InodeNumberLayer: Incorrect Parent Inode")
				return -1
			entry_size = config.MAX_FILE_NAME_SIZE + len(str(config.MAX_NUM_INODES))
			max_entries = (config.INODE_SIZE - 79 ) / entry_size
			if len(parent_inode.directory) == max_entries:
				print("Error InodeNumberLayer: Maximum inodes allowed per directory reached!")
				return -1
		for i in range(0, config.MAX_NUM_INODES):
			if self.INODE_NUMBER_TO_INODE(i) == False: #FALSE INDICTES UNOCCUPIED INODE ENTRY HENCE, FREEUMBER
				inode = interface1.new_inode(type)
				inode.name = name
				self.update_inode_table(inode, i)
				return i
		print("Error InodeNumberLayer: All inode Numbers are occupied!\n")


	#LINKS THE INODE
	def link(self, inode_number):
		inode = self.INODE_NUMBER_TO_INODE(inode_number)  # return inode
		return inode

	#REMOVES THE INODE ENTRY FROM INODE TABLE
	def unlink(self, inode_number):
		inode = self.INODE_NUMBER_TO_INODE(inode_number)
		# print ('inode link',inode.links)
		if inode.links == 0:  # if reference count is 0, then free block and inode
			# print (inode.blk_numbers)
			interface1.free_data_block(inode, 0)
			# print ("inode being deleted", inode_number)
			self.update_inode_table(False, inode_number)


	#IMPLEMENTS WRITE FUNCTIONALITY
	def write(self, inode_number, offset, data, parent_inode_number):
		inode = self.INODE_NUMBER_TO_INODE(inode_number)  # find inode according inode number
		interface1.write(inode, offset, data)  # write data to block
		self.update_inode_table(inode, inode_number)  # update inode table


	#IMPLEMENTS READ FUNCTIONALITY
	def read(self, inode_number, offset, length, parent_inode_number):
		inode = self.INODE_NUMBER_TO_INODE(inode_number)  # find inode according inode number
		inode, data = interface1.read(inode, offset, length)  # read data from block
		self.update_inode_table(inode, inode_number)  # update inode table
		return data


class InodeNumberLayer2():

	#PLEASE DO NOT MODIFY
	#ASKS FOR INODE FROM INODE NUMBER FROM MemoryInterface.(BLOCK LAYER HAS NOTHING TO DO WITH INODES SO SEPERTAE HANDLE)
	def INODE_NUMBER_TO_INODE(self, inode_number):
		array_inode = functions.inode_number_to_inode2(inode_number)
		inode = InodeOps.InodeOperations().convert_array_to_table(array_inode)
		if inode: inode.time_accessed = datetime.datetime.now()   #TIME OF ACCESS
		return inode


	#PLEASE DO NOT MODIFY
	#RETURNS DATA BLOCK FROM INODE NUMBER
	def INODE_NUMBER_TO_BLOCK(self, inode_number, offset, length):
		inode = self.INODE_NUMBER_TO_INODE(inode_number)
		if not inode:
			print("Error InodeNumberLayer: Wrong Inode Number! \n")
			return -1
		return interface2.read(inode, offset, length)


	#PLEASE DO NOT MODIFY
	#UPDATES THE INODE TO THE INODE TABLE
	def update_inode_table(self, table_inode, inode_number):
		if table_inode: table_inode.time_modified = datetime.datetime.now()  #TIME OF MODIFICATION
		array_inode = InodeOps.InodeOperations().convert_table_to_array(table_inode)
		functions.update_inode_table2(array_inode, inode_number)


	#PLEASE DO NOT MODIFY
	#FINDS NEW INODE INODE NUMBER FROM FILESYSTEM
	def new_inode_number(self, type, parent_inode_number, name):
		if parent_inode_number != -1:
			parent_inode = self.INODE_NUMBER_TO_INODE(parent_inode_number)
			if not parent_inode:
				print("Error InodeNumberLayer: Incorrect Parent Inode")
				return -1
			entry_size = config.MAX_FILE_NAME_SIZE + len(str(config.MAX_NUM_INODES))
			max_entries = (config.INODE_SIZE - 79 ) / entry_size
			if len(parent_inode.directory) == max_entries:
				print("Error InodeNumberLayer: Maximum inodes allowed per directory reached!")
				return -1
		for i in range(0, config.MAX_NUM_INODES):
			if self.INODE_NUMBER_TO_INODE(i) == False: #FALSE INDICTES UNOCCUPIED INODE ENTRY HENCE, FREEUMBER
				inode = interface2.new_inode(type)
				inode.name = name
				self.update_inode_table(inode, i)
				return i
		print("Error InodeNumberLayer: All inode Numbers are occupied!\n")


	#LINKS THE INODE
	def link(self, inode_number):
		inode = self.INODE_NUMBER_TO_INODE(inode_number)  # return inode
		return inode

	#REMOVES THE INODE ENTRY FROM INODE TABLE
	def unlink(self, inode_number):
		inode = self.INODE_NUMBER_TO_INODE(inode_number)
		# print ('inode link',inode.links)
		if inode.links == 0:  # if reference count is 0, then free block and inode
			# print (inode.blk_numbers)
			interface2.free_data_block(inode, 0)
			# print ("inode being deleted", inode_number)
			self.update_inode_table(False, inode_number)


	#IMPLEMENTS WRITE FUNCTIONALITY
	def write(self, inode_number, offset, data, parent_inode_number):
		inode = self.INODE_NUMBER_TO_INODE(inode_number)  # find inode according inode number
		interface2.write(inode, offset, data)  # write data to block
		self.update_inode_table(inode, inode_number)  # update inode table


	#IMPLEMENTS READ FUNCTIONALITY
	def read(self, inode_number, offset, length, parent_inode_number):
		inode = self.INODE_NUMBER_TO_INODE(inode_number)  # find inode according inode number
		inode, data = interface2.read(inode, offset, length)  # read data from block
		self.update_inode_table(inode, inode_number)  # update inode table
		return data


class InodeNumberLayer3():

	#PLEASE DO NOT MODIFY
	#ASKS FOR INODE FROM INODE NUMBER FROM MemoryInterface.(BLOCK LAYER HAS NOTHING TO DO WITH INODES SO SEPERTAE HANDLE)
	def INODE_NUMBER_TO_INODE(self, inode_number):
		array_inode = functions.inode_number_to_inode3(inode_number)
		inode = InodeOps.InodeOperations().convert_array_to_table(array_inode)
		if inode: inode.time_accessed = datetime.datetime.now()   #TIME OF ACCESS
		return inode


	#PLEASE DO NOT MODIFY
	#RETURNS DATA BLOCK FROM INODE NUMBER
	def INODE_NUMBER_TO_BLOCK(self, inode_number, offset, length):
		inode = self.INODE_NUMBER_TO_INODE(inode_number)
		if not inode:
			print("Error InodeNumberLayer: Wrong Inode Number! \n")
			return -1
		return interface3.read(inode, offset, length)


	#PLEASE DO NOT MODIFY
	#UPDATES THE INODE TO THE INODE TABLE
	def update_inode_table(self, table_inode, inode_number):
		if table_inode: table_inode.time_modified = datetime.datetime.now()  #TIME OF MODIFICATION
		array_inode = InodeOps.InodeOperations().convert_table_to_array(table_inode)
		functions.update_inode_table3(array_inode, inode_number)


	#PLEASE DO NOT MODIFY
	#FINDS NEW INODE INODE NUMBER FROM FILESYSTEM
	def new_inode_number(self, type, parent_inode_number, name):
		if parent_inode_number != -1:
			parent_inode = self.INODE_NUMBER_TO_INODE(parent_inode_number)
			if not parent_inode:
				print("Error InodeNumberLayer: Incorrect Parent Inode")
				return -1
			entry_size = config.MAX_FILE_NAME_SIZE + len(str(config.MAX_NUM_INODES))
			max_entries = (config.INODE_SIZE - 79 ) / entry_size
			if len(parent_inode.directory) == max_entries:
				print("Error InodeNumberLayer: Maximum inodes allowed per directory reached!")
				return -1
		for i in range(0, config.MAX_NUM_INODES):
			if self.INODE_NUMBER_TO_INODE(i) == False: #FALSE INDICTES UNOCCUPIED INODE ENTRY HENCE, FREEUMBER
				inode = interface3.new_inode(type)
				inode.name = name
				self.update_inode_table(inode, i)
				return i
		print("Error InodeNumberLayer: All inode Numbers are occupied!\n")


	#LINKS THE INODE
	def link(self, inode_number):
		inode = self.INODE_NUMBER_TO_INODE(inode_number)  # return inode
		return inode

	#REMOVES THE INODE ENTRY FROM INODE TABLE
	def unlink(self, inode_number):
		inode = self.INODE_NUMBER_TO_INODE(inode_number)
		# print ('inode link',inode.links)
		if inode.links == 0:  # if reference count is 0, then free block and inode
			# print (inode.blk_numbers)
			interface3.free_data_block(inode, 0)
			# print ("inode being deleted", inode_number)
			self.update_inode_table(False, inode_number)


	#IMPLEMENTS WRITE FUNCTIONALITY
	def write(self, inode_number, offset, data, parent_inode_number):
		inode = self.INODE_NUMBER_TO_INODE(inode_number)  # find inode according inode number
		interface3.write(inode, offset, data)  # write data to block
		self.update_inode_table(inode, inode_number)  # update inode table

	#IMPLEMENTS READ FUNCTIONALITY
	def read(self, inode_number, offset, length, parent_inode_number):
		inode = self.INODE_NUMBER_TO_INODE(inode_number)  # find inode according inode number
		inode, data = interface3.read(inode, offset, length)  # read data from block
		self.update_inode_table(inode, inode_number)  # update inode table
		return data





