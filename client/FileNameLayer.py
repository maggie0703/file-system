'''
THIS MODULE ACTS LIKE FILE NAME LAYER AND PATH NAME LAYER (BOTH) ABOVE INODE LAYER.
IT RECIEVES INPUT AS PATH (WITHOUT INITIAL '/'). THE LAYER IMPLEMENTS LOOKUP TO FIND INODE NUMBER OF THE REQUIRED DIRECTORY.
PARENTS INODE NUMBER IS FIRST EXTRACTED BY LOOKUP AND THEN CHILD INODE NUMBER BY RESPECTED FUNCTION AND BOTH OF THEM ARE UPDATED
'''
import InodeNumberLayer

#HANDLE OF INODE NUMBER LAYER
interface0 = InodeNumberLayer.InodeNumberLayer0()
interface1 = InodeNumberLayer.InodeNumberLayer1()
interface2 = InodeNumberLayer.InodeNumberLayer2()
interface3 = InodeNumberLayer.InodeNumberLayer3()

class FileNameLayer0():

	#PLEASE DO NOT MODIFY
	#RETURNS THE CHILD INODE NUMBER FROM THE PARENTS INODE NUMBER
	def CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(self, childname, inode_number_of_parent):
		inode = interface0.INODE_NUMBER_TO_INODE(inode_number_of_parent)
		if not inode:
			print("Error FileNameLayer: Lookup Failure!")
			return -1
		if inode.type == 0:
			print("Error FileNameLayer: Invalid Directory!")
			return -1
		if childname in inode.directory: return inode.directory[childname]
		print("Error FileNameLayer: Lookup Failure!")
		return -1

	#PLEASE DO NOT MODIFY
	#RETUNS THE PARENT INODE NUMBER FROM THE PATH GIVEN FOR A FILE/DIRECTORY
	def LOOKUP(self, path, inode_number_cwd):
		name_array = path.split('/')
		if len(name_array) == 1: return inode_number_cwd
		else:
			child_inode_number = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(name_array[0], inode_number_cwd)
			if child_inode_number == -1: return -1
			return self.LOOKUP("/".join(name_array[1:]), child_inode_number)

	#PLEASE DO NOT MODIFY
	#MAKES NEW ENTRY OF INODE
	def new_entry(self, path, inode_number_cwd, type):
		if path == '/': #SPECIAL CASE OF INITIALIZING FILE SYSTEM
			interface0.new_inode_number(type, inode_number_cwd, "root")
			return True
		parent_inode_number = self.LOOKUP(path, inode_number_cwd)
		parent_inode = interface0.INODE_NUMBER_TO_INODE(parent_inode_number)
		childname = path.split('/')[-1]
		if not parent_inode: return -1
		if childname in parent_inode.directory:
			print("Error FileNameLayer: File already exists!")
			return -1
		child_inode_number = interface0.new_inode_number(type, parent_inode_number, childname)  #make new child
		if child_inode_number != -1:
			parent_inode.directory[childname] = child_inode_number
			interface0.update_inode_table(parent_inode, parent_inode_number)


	#IMPLEMENTS READ
	def read(self, path, inode_number_cwd, offset, length):
		inode_number_parent = self.LOOKUP(path, inode_number_cwd)
		if inode_number_parent == -1:  # directory inode doesn't exist
			print("Error FileNameLayer: Wrong Path Given!\n")
			return -1
		childname = path.split('/')[-1]
		inode_number_child = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(childname, inode_number_parent)
		if inode_number_child == -1:  # file doesn't exist
			print('Error FileNameLayer: Wrong Path Given!\n')
			return -1
		return interface0.read(inode_number_child, offset, length, inode_number_parent)  # call read function


	#IMPLEMENTS WRITE
	def write(self, path, inode_number_cwd, offset, data):
		'''WRITE YOUR CODE HERE'''
		inode_number_parent = self.LOOKUP(path, inode_number_cwd)
		if inode_number_parent == -1:  # parent directory doesn't exist
			print("Error FileNameLayer: Wrong Path Given!\n")
			return -1
		childname = path.split('/')[-1]
		child_inode_number = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(childname, inode_number_parent)
		if child_inode_number == -1:  # file doesn't exist
			print('Error FileNameLayer: Wrong Path Given!\n')
			return -1
		interface0.write(child_inode_number, offset, data, inode_number_parent)  # call write function

	#HARDLINK
	def link(self, old_path, new_path, inode_number_cwd):
		'''WRITE YOUR CODE HERE'''
		old_inode_number_parent = self.LOOKUP(old_path, inode_number_cwd)
		old_childname = old_path.split('/')[-1]
		old_child_inode_number = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(old_childname,
																				  old_inode_number_parent)
		old_child_inode = interface0.link(old_child_inode_number)
		if old_child_inode.type == 1:  # Type of Destination inode of old path should be file
			print('Error FileNameLayer: Wrong Destination Inode Type!\n')
			return -1

		# destination is a folder in move function
		if new_path.split('.')[-1] != 'txt':
			new_inode_number_parent = self.LOOKUP(new_path, inode_number_cwd)
			if new_inode_number_parent == -1:
				print('Error FileNameLayer: Wrong Path Given!\n')
				return -1
			new_childname = new_path.split('/')[-1]
			new_inode_number_child = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(new_childname,
																					  new_inode_number_parent)
			if new_inode_number_child == -1:
				print('Error FileNameLayer: Wrong Path Given!\n')
				return -1
			new_inode_child = interface0.INODE_NUMBER_TO_INODE(new_inode_number_child)
			new_inode_child.directory[
				old_childname] = old_child_inode_number  # add a new binding in directory of new child inode
			old_child_inode.links += 1  # increment reference link of old child inode
			interface0.update_inode_table(old_child_inode, old_child_inode_number)  # save old child inode in the memory
			interface0.update_inode_table(new_inode_child, new_inode_number_child)  # save new inode child in the memory
		# print ("block number of old child inode",old_child_inode.blk_numbers)

		else:  # destination is a file
			new_inode_number_parent = self.LOOKUP(new_path, inode_number_cwd)
			if new_inode_number_parent == -1:
				print('Error FileNameLayer: Wrong Path Given!\n')
				return -1
			new_childname = new_path.split('/')[-1]
			new_inode_parent = interface0.INODE_NUMBER_TO_INODE(new_inode_number_parent)
			new_inode_parent.directory[new_childname] = old_child_inode_number
			old_child_inode.links += 1
			interface0.update_inode_table(old_child_inode, old_child_inode_number)  # save old child inode in the memory
			interface0.update_inode_table(new_inode_parent,
										 new_inode_number_parent)  # save new inode child in the memory

	#REMOVES THE FILE/DIRECTORY
	def unlink(self, path, inode_number_cwd):
		if path == "":
			print("Error FileNameLayer: Cannot delete root directory!")
			return -1
		parent_inode_number = self.LOOKUP(path, inode_number_cwd)
		if parent_inode_number == -1:  # file doesn't exist
			print('Error FileNameLayer: Wrong Path Given!\n')
			return -1
		childname = path.split('/')[-1]
		child_inode_number = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(childname, parent_inode_number)
		if child_inode_number == -1:  # file doesn't exist
			print('Error FileNameLayer: Wrong Path Given!\n')
			return -1

		child_inode = interface0.INODE_NUMBER_TO_INODE(child_inode_number)

		if (child_inode.type) == 1:  # can't unlink a directory
			print('Error FileNameLayer: Can not unlink a directory\n')
			return -1

		parent_inode = interface0.INODE_NUMBER_TO_INODE(parent_inode_number)

		del parent_inode.directory[childname]  # delete the binding in directory of parent inode
		child_inode.links -= 1  # decrease links of file inode
		# print ("links of child inode",child_inode.links)
		interface0.update_inode_table(child_inode, child_inode_number)  # update child inode table
		interface0.unlink(child_inode_number)  # if links count is 0, then free blocks and inode

		interface0.update_inode_table(parent_inode, parent_inode_number)  # update parent inode table

	#MOVE
	def mv(self, old_path, new_path, inode_number_cwd):
		new_inode_number_parent = self.LOOKUP(new_path, inode_number_cwd)
		if new_inode_number_parent == -1:  # parent inode doesn't exist
			print('Error FileNameLayer: Wrong Path Given!\n')
			return -1
		new_childname = new_path.split('/')[-1]
		new_child_inode_number = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(new_childname,
																				  new_inode_number_parent)
		if new_child_inode_number == -1:  # file doesn't exist
			print('Error FileNameLayer: Wrong Path Given!\n')
			return -1
		new_child_inode = interface0.link(new_child_inode_number)
		if new_child_inode.type == 0:  # destination inode is not allowed to be a file
			print('Error FileNameLayer: Destination Folder Is Not Given!\n')
			return -1
		# move the file from one folder to another
		self.link(old_path, new_path, inode_number_cwd)
		self.unlink(old_path, inode_number_cwd)

class FileNameLayer1():

	#PLEASE DO NOT MODIFY
	#RETURNS THE CHILD INODE NUMBER FROM THE PARENTS INODE NUMBER
	def CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(self, childname, inode_number_of_parent):
		inode = interface1.INODE_NUMBER_TO_INODE(inode_number_of_parent)
		if not inode:
			print("Error FileNameLayer: Lookup Failure!")
			return -1
		if inode.type == 0:
			print("Error FileNameLayer: Invalid Directory!")
			return -1
		if childname in inode.directory: return inode.directory[childname]
		print("Error FileNameLayer: Lookup Failure!")
		return -1

	#PLEASE DO NOT MODIFY
	#RETUNS THE PARENT INODE NUMBER FROM THE PATH GIVEN FOR A FILE/DIRECTORY
	def LOOKUP(self, path, inode_number_cwd):
		name_array = path.split('/')
		if len(name_array) == 1: return inode_number_cwd
		else:
			child_inode_number = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(name_array[0], inode_number_cwd)
			if child_inode_number == -1: return -1
			return self.LOOKUP("/".join(name_array[1:]), child_inode_number)

	#PLEASE DO NOT MODIFY
	#MAKES NEW ENTRY OF INODE
	def new_entry(self, path, inode_number_cwd, type):
		if path == '/': #SPECIAL CASE OF INITIALIZING FILE SYSTEM
			interface1.new_inode_number(type, inode_number_cwd, "root")
			return True
		parent_inode_number = self.LOOKUP(path, inode_number_cwd)
		parent_inode = interface1.INODE_NUMBER_TO_INODE(parent_inode_number)
		childname = path.split('/')[-1]
		if not parent_inode: return -1
		if childname in parent_inode.directory:
			print("Error FileNameLayer: File already exists!")
			return -1
		child_inode_number = interface1.new_inode_number(type, parent_inode_number, childname)  #make new child
		if child_inode_number != -1:
			parent_inode.directory[childname] = child_inode_number
			interface1.update_inode_table(parent_inode, parent_inode_number)


	#IMPLEMENTS READ
	def read(self, path, inode_number_cwd, offset, length):
		inode_number_parent = self.LOOKUP(path, inode_number_cwd)
		if inode_number_parent == -1:  # directory inode doesn't exist
			print("Error FileNameLayer: Wrong Path Given!\n")
			return -1
		childname = path.split('/')[-1]
		inode_number_child = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(childname, inode_number_parent)
		if inode_number_child == -1:  # file doesn't exist
			print('Error FileNameLayer: Wrong Path Given!\n')
			return -1
		return interface1.read(inode_number_child, offset, length, inode_number_parent)  # call read function

	#IMPLEMENTS WRITE
	def write(self, path, inode_number_cwd, offset, data):
		'''WRITE YOUR CODE HERE'''
		inode_number_parent = self.LOOKUP(path, inode_number_cwd)
		if inode_number_parent == -1:  # parent directory doesn't exist
			print("Error FileNameLayer: Wrong Path Given!\n")
			return -1
		childname = path.split('/')[-1]
		child_inode_number = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(childname, inode_number_parent)
		if child_inode_number == -1:  # file doesn't exist
			print('Error FileNameLayer: Wrong Path Given!\n')
			return -1
		interface1.write(child_inode_number, offset, data, inode_number_parent)  # call write function

	#HARDLINK
	def link(self, old_path, new_path, inode_number_cwd):
		'''WRITE YOUR CODE HERE'''
		old_inode_number_parent = self.LOOKUP(old_path, inode_number_cwd)
		old_childname = old_path.split('/')[-1]
		old_child_inode_number = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(old_childname,
																				  old_inode_number_parent)
		old_child_inode = interface1.link(old_child_inode_number)
		if old_child_inode.type == 1:  # Type of Destination inode of old path should be file
			print('Error FileNameLayer: Wrong Destination Inode Type!\n')
			return -1

		# destination is a folder in move function
		if new_path.split('.')[-1] != 'txt':
			new_inode_number_parent = self.LOOKUP(new_path, inode_number_cwd)
			if new_inode_number_parent == -1:
				print('Error FileNameLayer: Wrong Path Given!\n')
				return -1
			new_childname = new_path.split('/')[-1]
			new_inode_number_child = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(new_childname,
																					  new_inode_number_parent)
			if new_inode_number_child == -1:
				print('Error FileNameLayer: Wrong Path Given!\n')
				return -1
			new_inode_child = interface1.INODE_NUMBER_TO_INODE(new_inode_number_child)
			new_inode_child.directory[
				old_childname] = old_child_inode_number  # add a new binding in directory of new child inode
			old_child_inode.links += 1  # increment reference link of old child inode
			interface1.update_inode_table(old_child_inode, old_child_inode_number)  # save old child inode in the memory
			interface1.update_inode_table(new_inode_child, new_inode_number_child)  # save new inode child in the memory
		# print ("block number of old child inode",old_child_inode.blk_numbers)

		else:  # destination is a file
			new_inode_number_parent = self.LOOKUP(new_path, inode_number_cwd)
			if new_inode_number_parent == -1:
				print('Error FileNameLayer: Wrong Path Given!\n')
				return -1
			new_childname = new_path.split('/')[-1]
			new_inode_parent = interface1.INODE_NUMBER_TO_INODE(new_inode_number_parent)
			new_inode_parent.directory[new_childname] = old_child_inode_number
			old_child_inode.links += 1
			interface1.update_inode_table(old_child_inode, old_child_inode_number)  # save old child inode in the memory
			interface1.update_inode_table(new_inode_parent,
										 new_inode_number_parent)  # save new inode child in the memory

	#REMOVES THE FILE/DIRECTORY
	def unlink(self, path, inode_number_cwd):
		if path == "":
			print("Error FileNameLayer: Cannot delete root directory!")
			return -1
		parent_inode_number = self.LOOKUP(path, inode_number_cwd)
		if parent_inode_number == -1:  # file doesn't exist
			print('Error FileNameLayer: Wrong Path Given!\n')
			return -1
		childname = path.split('/')[-1]
		child_inode_number = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(childname, parent_inode_number)
		if child_inode_number == -1:  # file doesn't exist
			print('Error FileNameLayer: Wrong Path Given!\n')
			return -1

		child_inode = interface1.INODE_NUMBER_TO_INODE(child_inode_number)

		if (child_inode.type) == 1:  # can't unlink a directory
			print('Error FileNameLayer: Can not unlink a directory\n')
			return -1

		parent_inode = interface1.INODE_NUMBER_TO_INODE(parent_inode_number)

		del parent_inode.directory[childname]  # delete the binding in directory of parent inode
		child_inode.links -= 1  # decrease links of file inode
		# print ("links of child inode",child_inode.links)
		interface1.update_inode_table(child_inode, child_inode_number)  # update child inode table
		interface1.unlink(child_inode_number)  # if links count is 0, then free blocks and inode

		interface1.update_inode_table(parent_inode, parent_inode_number)  # update parent inode table

	#MOVE
	def mv(self, old_path, new_path, inode_number_cwd):
		new_inode_number_parent = self.LOOKUP(new_path, inode_number_cwd)
		if new_inode_number_parent == -1:  # parent inode doesn't exist
			print('Error FileNameLayer: Wrong Path Given!\n')
			return -1
		new_childname = new_path.split('/')[-1]
		new_child_inode_number = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(new_childname,
																				  new_inode_number_parent)
		if new_child_inode_number == -1:  # file doesn't exist
			print('Error FileNameLayer: Wrong Path Given!\n')
			return -1
		new_child_inode = interface1.link(new_child_inode_number)
		if new_child_inode.type == 0:  # destination inode is not allowed to be a file
			print('Error FileNameLayer: Destination Folder Is Not Given!\n')
			return -1
		# move the file from one folder to another
		self.link(old_path, new_path, inode_number_cwd)
		self.unlink(old_path, inode_number_cwd)

class FileNameLayer2():

	#PLEASE DO NOT MODIFY
	#RETURNS THE CHILD INODE NUMBER FROM THE PARENTS INODE NUMBER
	def CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(self, childname, inode_number_of_parent):
		inode = interface2.INODE_NUMBER_TO_INODE(inode_number_of_parent)
		if not inode:
			print("Error FileNameLayer: Lookup Failure!")
			return -1
		if inode.type == 0:
			print("Error FileNameLayer: Invalid Directory!")
			return -1
		if childname in inode.directory: return inode.directory[childname]
		print("Error FileNameLayer: Lookup Failure!")
		return -1

	#PLEASE DO NOT MODIFY
	#RETUNS THE PARENT INODE NUMBER FROM THE PATH GIVEN FOR A FILE/DIRECTORY
	def LOOKUP(self, path, inode_number_cwd):
		name_array = path.split('/')
		if len(name_array) == 1: return inode_number_cwd
		else:
			child_inode_number = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(name_array[0], inode_number_cwd)
			if child_inode_number == -1: return -1
			return self.LOOKUP("/".join(name_array[1:]), child_inode_number)

	#PLEASE DO NOT MODIFY
	#MAKES NEW ENTRY OF INODE
	def new_entry(self, path, inode_number_cwd, type):
		if path == '/': #SPECIAL CASE OF INITIALIZING FILE SYSTEM
			interface2.new_inode_number(type, inode_number_cwd, "root")
			return True
		parent_inode_number = self.LOOKUP(path, inode_number_cwd)
		parent_inode = interface2.INODE_NUMBER_TO_INODE(parent_inode_number)
		childname = path.split('/')[-1]
		if not parent_inode: return -1
		if childname in parent_inode.directory:
			print("Error FileNameLayer: File already exists!")
			return -1
		child_inode_number = interface2.new_inode_number(type, parent_inode_number, childname)  #make new child
		if child_inode_number != -1:
			parent_inode.directory[childname] = child_inode_number
			interface2.update_inode_table(parent_inode, parent_inode_number)


	#IMPLEMENTS READ
	def read(self, path, inode_number_cwd, offset, length):
		inode_number_parent = self.LOOKUP(path, inode_number_cwd)
		if inode_number_parent == -1:  # directory inode doesn't exist
			print("Error FileNameLayer: Wrong Path Given!\n")
			return -1
		childname = path.split('/')[-1]
		inode_number_child = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(childname, inode_number_parent)
		if inode_number_child == -1:  # file doesn't exist
			print('Error FileNameLayer: Wrong Path Given!\n')
			return -1
		return interface2.read(inode_number_child, offset, length, inode_number_parent)  # call read function


	#IMPLEMENTS WRITE
	def write(self, path, inode_number_cwd, offset, data):
		'''WRITE YOUR CODE HERE'''
		inode_number_parent = self.LOOKUP(path, inode_number_cwd)
		if inode_number_parent == -1:  # parent directory doesn't exist
			print("Error FileNameLayer: Wrong Path Given!\n")
			return -1
		childname = path.split('/')[-1]
		child_inode_number = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(childname, inode_number_parent)
		if child_inode_number == -1:  # file doesn't exist
			print('Error FileNameLayer: Wrong Path Given!\n')
			return -1
		interface2.write(child_inode_number, offset, data, inode_number_parent)  # call write function

	#HARDLINK
	def link(self, old_path, new_path, inode_number_cwd):
		'''WRITE YOUR CODE HERE'''
		old_inode_number_parent = self.LOOKUP(old_path, inode_number_cwd)
		old_childname = old_path.split('/')[-1]
		old_child_inode_number = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(old_childname,
																				  old_inode_number_parent)
		old_child_inode = interface2.link(old_child_inode_number)
		if old_child_inode.type == 1:  # Type of Destination inode of old path should be file
			print('Error FileNameLayer: Wrong Destination Inode Type!\n')
			return -1

		# destination is a folder in move function
		if new_path.split('.')[-1] != 'txt':
			new_inode_number_parent = self.LOOKUP(new_path, inode_number_cwd)
			if new_inode_number_parent == -1:
				print('Error FileNameLayer: Wrong Path Given!\n')
				return -1
			new_childname = new_path.split('/')[-1]
			new_inode_number_child = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(new_childname,
																					  new_inode_number_parent)
			if new_inode_number_child == -1:
				print('Error FileNameLayer: Wrong Path Given!\n')
				return -1
			new_inode_child = interface2.INODE_NUMBER_TO_INODE(new_inode_number_child)
			new_inode_child.directory[
				old_childname] = old_child_inode_number  # add a new binding in directory of new child inode
			old_child_inode.links += 1  # increment reference link of old child inode
			interface2.update_inode_table(old_child_inode, old_child_inode_number)  # save old child inode in the memory
			interface2.update_inode_table(new_inode_child, new_inode_number_child)  # save new inode child in the memory
		# print ("block number of old child inode",old_child_inode.blk_numbers)

		else:  # destination is a file
			new_inode_number_parent = self.LOOKUP(new_path, inode_number_cwd)
			if new_inode_number_parent == -1:
				print('Error FileNameLayer: Wrong Path Given!\n')
				return -1
			new_childname = new_path.split('/')[-1]
			new_inode_parent = interface2.INODE_NUMBER_TO_INODE(new_inode_number_parent)
			new_inode_parent.directory[new_childname] = old_child_inode_number
			old_child_inode.links += 1
			interface2.update_inode_table(old_child_inode, old_child_inode_number)  # save old child inode in the memory
			interface2.update_inode_table(new_inode_parent,
										 new_inode_number_parent)  # save new inode child in the memory

	#REMOVES THE FILE/DIRECTORY
	def unlink(self, path, inode_number_cwd):
		if path == "":
			print("Error FileNameLayer: Cannot delete root directory!")
			return -1
		parent_inode_number = self.LOOKUP(path, inode_number_cwd)
		if parent_inode_number == -1:  # file doesn't exist
			print('Error FileNameLayer: Wrong Path Given!\n')
			return -1
		childname = path.split('/')[-1]
		child_inode_number = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(childname, parent_inode_number)
		if child_inode_number == -1:  # file doesn't exist
			print('Error FileNameLayer: Wrong Path Given!\n')
			return -1

		child_inode = interface2.INODE_NUMBER_TO_INODE(child_inode_number)

		if (child_inode.type) == 1:  # can't unlink a directory
			print('Error FileNameLayer: Can not unlink a directory\n')
			return -1

		parent_inode = interface2.INODE_NUMBER_TO_INODE(parent_inode_number)

		del parent_inode.directory[childname]  # delete the binding in directory of parent inode
		child_inode.links -= 1  # decrease links of file inode
		# print ("links of child inode",child_inode.links)
		interface2.update_inode_table(child_inode, child_inode_number)  # update child inode table
		interface2.unlink(child_inode_number)  # if links count is 0, then free blocks and inode

		interface2.update_inode_table(parent_inode, parent_inode_number)  # update parent inode table

	#MOVE
	def mv(self, old_path, new_path, inode_number_cwd):
		new_inode_number_parent = self.LOOKUP(new_path, inode_number_cwd)
		if new_inode_number_parent == -1:  # parent inode doesn't exist
			print('Error FileNameLayer: Wrong Path Given!\n')
			return -1
		new_childname = new_path.split('/')[-1]
		new_child_inode_number = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(new_childname,
																				  new_inode_number_parent)
		if new_child_inode_number == -1:  # file doesn't exist
			print('Error FileNameLayer: Wrong Path Given!\n')
			return -1
		new_child_inode = interface2.link(new_child_inode_number)
		if new_child_inode.type == 0:  # destination inode is not allowed to be a file
			print('Error FileNameLayer: Destination Folder Is Not Given!\n')
			return -1
		# move the file from one folder to another
		self.link(old_path, new_path, inode_number_cwd)
		self.unlink(old_path, inode_number_cwd)

class FileNameLayer3():

	#PLEASE DO NOT MODIFY
	#RETURNS THE CHILD INODE NUMBER FROM THE PARENTS INODE NUMBER
	def CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(self, childname, inode_number_of_parent):
		inode = interface3.INODE_NUMBER_TO_INODE(inode_number_of_parent)
		if not inode:
			print("Error FileNameLayer: Lookup Failure!")
			return -1
		if inode.type == 0:
			print("Error FileNameLayer: Invalid Directory!")
			return -1
		if childname in inode.directory: return inode.directory[childname]
		print("Error FileNameLayer: Lookup Failure!")
		return -1

	#PLEASE DO NOT MODIFY
	#RETUNS THE PARENT INODE NUMBER FROM THE PATH GIVEN FOR A FILE/DIRECTORY
	def LOOKUP(self, path, inode_number_cwd):
		name_array = path.split('/')
		if len(name_array) == 1: return inode_number_cwd
		else:
			child_inode_number = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(name_array[0], inode_number_cwd)
			if child_inode_number == -1: return -1
			return self.LOOKUP("/".join(name_array[1:]), child_inode_number)

	#PLEASE DO NOT MODIFY
	#MAKES NEW ENTRY OF INODE
	def new_entry(self, path, inode_number_cwd, type):
		if path == '/': #SPECIAL CASE OF INITIALIZING FILE SYSTEM
			interface3.new_inode_number(type, inode_number_cwd, "root")
			return True
		parent_inode_number = self.LOOKUP(path, inode_number_cwd)
		parent_inode = interface3.INODE_NUMBER_TO_INODE(parent_inode_number)
		childname = path.split('/')[-1]
		if not parent_inode: return -1
		if childname in parent_inode.directory:
			print("Error FileNameLayer: File already exists!")
			return -1
		child_inode_number = interface3.new_inode_number(type, parent_inode_number, childname)  #make new child
		if child_inode_number != -1:
			parent_inode.directory[childname] = child_inode_number
			interface3.update_inode_table(parent_inode, parent_inode_number)


	#IMPLEMENTS READ
	def read(self, path, inode_number_cwd, offset, length):
		inode_number_parent = self.LOOKUP(path, inode_number_cwd)
		if inode_number_parent == -1:  # directory inode doesn't exist
			print("Error FileNameLayer: Wrong Path Given!\n")
			return -1
		childname = path.split('/')[-1]
		inode_number_child = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(childname, inode_number_parent)
		if inode_number_child == -1:  # file doesn't exist
			print('Error FileNameLayer: Wrong Path Given!\n')
			return -1
		return interface3.read(inode_number_child, offset, length, inode_number_parent)  # call read function

	#IMPLEMENTS WRITE
	def write(self, path, inode_number_cwd, offset, data):
		'''WRITE YOUR CODE HERE'''
		inode_number_parent = self.LOOKUP(path, inode_number_cwd)
		if inode_number_parent == -1:  # parent directory doesn't exist
			print("Error FileNameLayer: Wrong Path Given!\n")
			return -1
		childname = path.split('/')[-1]
		child_inode_number = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(childname, inode_number_parent)
		if child_inode_number == -1:  # file doesn't exist
			print('Error FileNameLayer: Wrong Path Given!\n')
			return -1
		interface3.write(child_inode_number, offset, data, inode_number_parent)  # call write function

	#HARDLINK
	def link(self, old_path, new_path, inode_number_cwd):
		'''WRITE YOUR CODE HERE'''
		old_inode_number_parent = self.LOOKUP(old_path, inode_number_cwd)
		old_childname = old_path.split('/')[-1]
		old_child_inode_number = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(old_childname,
																				  old_inode_number_parent)
		old_child_inode = interface3.link(old_child_inode_number)
		if old_child_inode.type == 1:  # Type of Destination inode of old path should be file
			print('Error FileNameLayer: Wrong Destination Inode Type!\n')
			return -1

		# destination is a folder in move function
		if new_path.split('.')[-1] != 'txt':
			new_inode_number_parent = self.LOOKUP(new_path, inode_number_cwd)
			if new_inode_number_parent == -1:
				print('Error FileNameLayer: Wrong Path Given!\n')
				return -1
			new_childname = new_path.split('/')[-1]
			new_inode_number_child = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(new_childname,
																					  new_inode_number_parent)
			if new_inode_number_child == -1:
				print('Error FileNameLayer: Wrong Path Given!\n')
				return -1
			new_inode_child = interface3.INODE_NUMBER_TO_INODE(new_inode_number_child)
			new_inode_child.directory[
				old_childname] = old_child_inode_number  # add a new binding in directory of new child inode
			old_child_inode.links += 1  # increment reference link of old child inode
			interface3.update_inode_table(old_child_inode, old_child_inode_number)  # save old child inode in the memory
			interface3.update_inode_table(new_inode_child, new_inode_number_child)  # save new inode child in the memory
		# print ("block number of old child inode",old_child_inode.blk_numbers)

		else:  # destination is a file
			new_inode_number_parent = self.LOOKUP(new_path, inode_number_cwd)
			if new_inode_number_parent == -1:
				print('Error FileNameLayer: Wrong Path Given!\n')
				return -1
			new_childname = new_path.split('/')[-1]
			new_inode_parent = interface3.INODE_NUMBER_TO_INODE(new_inode_number_parent)
			new_inode_parent.directory[new_childname] = old_child_inode_number
			old_child_inode.links += 1
			interface3.update_inode_table(old_child_inode, old_child_inode_number)  # save old child inode in the memory
			interface3.update_inode_table(new_inode_parent,
										 new_inode_number_parent)  # save new inode child in the memory

	#REMOVES THE FILE/DIRECTORY
	def unlink(self, path, inode_number_cwd):
		if path == "":
			print("Error FileNameLayer: Cannot delete root directory!")
			return -1
		parent_inode_number = self.LOOKUP(path, inode_number_cwd)
		if parent_inode_number == -1:  # file doesn't exist
			print('Error FileNameLayer: Wrong Path Given!\n')
			return -1
		childname = path.split('/')[-1]
		child_inode_number = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(childname, parent_inode_number)
		if child_inode_number == -1:  # file doesn't exist
			print('Error FileNameLayer: Wrong Path Given!\n')
			return -1

		child_inode = interface3.INODE_NUMBER_TO_INODE(child_inode_number)

		if (child_inode.type) == 1:  # can't unlink a directory
			print('Error FileNameLayer: Can not unlink a directory\n')
			return -1

		parent_inode = interface3.INODE_NUMBER_TO_INODE(parent_inode_number)

		del parent_inode.directory[childname]  # delete the binding in directory of parent inode
		child_inode.links -= 1  # decrease links of file inode
		# print ("links of child inode",child_inode.links)
		interface3.update_inode_table(child_inode, child_inode_number)  # update child inode table
		interface3.unlink(child_inode_number)  # if links count is 0, then free blocks and inode

		interface3.update_inode_table(parent_inode, parent_inode_number)  # update parent inode table

	#MOVE
	def mv(self, old_path, new_path, inode_number_cwd):
		new_inode_number_parent = self.LOOKUP(new_path, inode_number_cwd)
		if new_inode_number_parent == -1:  # parent inode doesn't exist
			print('Error FileNameLayer: Wrong Path Given!\n')
			return -1
		new_childname = new_path.split('/')[-1]
		new_child_inode_number = self.CHILD_INODE_NUMBER_FROM_PARENT_INODE_NUMBER(new_childname,
																				  new_inode_number_parent)
		if new_child_inode_number == -1:  # file doesn't exist
			print('Error FileNameLayer: Wrong Path Given!\n')
			return -1
		new_child_inode = interface3.link(new_child_inode_number)
		if new_child_inode.type == 0:  # destination inode is not allowed to be a file
			print('Error FileNameLayer: Destination Folder Is Not Given!\n')
			return -1
		# move the file from one folder to another
		self.link(old_path, new_path, inode_number_cwd)
		self.unlink(old_path, inode_number_cwd)
