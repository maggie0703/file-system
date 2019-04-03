'''
THIS MODULE SERVE AS A TOP MOST MODULE OF FILE SYSTEM LAYER. IT CONNECTS THE FILE SYSTEM OPERATIONS WITH FILE SYSTEM LAYERS. 
IT ALSO PROVIDES ABSOLUTE PATH RESPECTIVE TO ROOT DIRECTORY. IT TAKES COMPLETE PATH AS THE INPUT.
'''

import FileNameLayer


#HANDLE OF FILE NAME LAYER
interface0 = FileNameLayer.FileNameLayer0()
interface1 = FileNameLayer.FileNameLayer1()
interface2 = FileNameLayer.FileNameLayer2()
interface3 = FileNameLayer.FileNameLayer3()

class AbsolutePathNameLayer0():

	#RETURNS INODE NUMBER OF HOME DIRECTORY IF CORRECT PATH IS GIVEN
	def GENERAL_PATH_TO_HOME_INODE_NUMBER(self, path):
		path_array = path.split('/')
		if len(path_array) > 1 and path_array[0] == '': return 0
		else: return -1


	#MAKES NEW
	def new_entry(self, path, type):
		if path == '/':   #SPECIAL CASE OF INITIALIZING FILE SYSTEM
			interface0.new_entry('/', -1, type)
			return
		inode_number_of_parent = self.GENERAL_PATH_TO_HOME_INODE_NUMBER(path)
		if inode_number_of_parent == -1:
			print("Error AbsolutePathLayer: Wrong Path!")
			return -1
		interface0.new_entry(path[1:], inode_number_of_parent, type)


	#IMPLEMENTS READ
	def read(self, path, offset, length):
		inode_number_of_parent = self.GENERAL_PATH_TO_HOME_INODE_NUMBER(path)
		if inode_number_of_parent == -1:
			print("Error AbsolutePathLayer: Wrong Path Given!\n")
			return -1
		return interface0.read(path[1:], inode_number_of_parent, offset, length)


	#IMPLEMENTS WRITE
	def write(self, path, offset, data):
		inode_number_of_parent = self.GENERAL_PATH_TO_HOME_INODE_NUMBER(path)
		if inode_number_of_parent == -1:
			print("Error AbsolutePathLayer: Wrong Path Given!\n")
			return -1
		interface0.write(path[1:], inode_number_of_parent, offset, data)


	#IMPLEMENTS THE HARDLINK
	def link(self, old_path, new_path):
		inode_number_of_parent = self.GENERAL_PATH_TO_HOME_INODE_NUMBER(old_path)
		if inode_number_of_parent == -1:
			print("Error AbsolutePathLayer: Wrong Path Given!\n")
			return -1
		interface0.link(old_path[1:], new_path[1:], inode_number_of_parent)


	#IMPLEMENTS DELETE
	def unlink(self, path):
		inode_number_of_parent = self.GENERAL_PATH_TO_HOME_INODE_NUMBER(path)
		if inode_number_of_parent == -1:
			print("Error AbsolutePathLayer: Wrong Path Given!\n")
			return -1
		interface0.unlink(path[1:], inode_number_of_parent)


	#MOVE
	def mv(self, old_path, new_path):
		inode_number_of_parent = self.GENERAL_PATH_TO_HOME_INODE_NUMBER(old_path)
		if inode_number_of_parent == -1:
			print("Error AbsolutePathLayer: Wrong Path Given!\n")
			return -1
		interface0.mv(old_path[1:], new_path[1:], inode_number_of_parent)


class AbsolutePathNameLayer1():

	#RETURNS INODE NUMBER OF HOME DIRECTORY IF CORRECT PATH IS GIVEN
	def GENERAL_PATH_TO_HOME_INODE_NUMBER(self, path):
		path_array = path.split('/')
		if len(path_array) > 1 and path_array[0] == '': return 0
		else: return -1


	#MAKES NEW
	def new_entry(self, path, type):
		if path == '/':   #SPECIAL CASE OF INITIALIZING FILE SYSTEM
			interface1.new_entry('/', -1, type)
			return
		inode_number_of_parent = self.GENERAL_PATH_TO_HOME_INODE_NUMBER(path)
		if inode_number_of_parent == -1:
			print("Error AbsolutePathLayer: Wrong Path!")
			return -1
		interface1.new_entry(path[1:], inode_number_of_parent, type)


	#IMPLEMENTS READ
	def read(self, path, offset, length):
		inode_number_of_parent = self.GENERAL_PATH_TO_HOME_INODE_NUMBER(path)
		if inode_number_of_parent == -1:
			print("Error AbsolutePathLayer: Wrong Path Given!\n")
			return -1
		return interface1.read(path[1:], inode_number_of_parent, offset, length)


	#IMPLEMENTS WRITE
	def write(self, path, offset, data):
		inode_number_of_parent = self.GENERAL_PATH_TO_HOME_INODE_NUMBER(path)
		if inode_number_of_parent == -1:
			print("Error AbsolutePathLayer: Wrong Path Given!\n")
			return -1
		interface1.write(path[1:], inode_number_of_parent, offset, data)


	#IMPLEMENTS THE HARDLINK
	def link(self, old_path, new_path):
		inode_number_of_parent = self.GENERAL_PATH_TO_HOME_INODE_NUMBER(old_path)
		if inode_number_of_parent == -1:
			print("Error AbsolutePathLayer: Wrong Path Given!\n")
			return -1
		interface1.link(old_path[1:], new_path[1:], inode_number_of_parent)


	#IMPLEMENTS DELETE
	def unlink(self, path):
		inode_number_of_parent = self.GENERAL_PATH_TO_HOME_INODE_NUMBER(path)
		if inode_number_of_parent == -1:
			print("Error AbsolutePathLayer: Wrong Path Given!\n")
			return -1
		interface1.unlink(path[1:], inode_number_of_parent)


	#MOVE
	def mv(self, old_path, new_path):
		inode_number_of_parent = self.GENERAL_PATH_TO_HOME_INODE_NUMBER(old_path)
		if inode_number_of_parent == -1:
			print("Error AbsolutePathLayer: Wrong Path Given!\n")
			return -1
		interface1.mv(old_path[1:], new_path[1:], inode_number_of_parent)


class AbsolutePathNameLayer2():

	#RETURNS INODE NUMBER OF HOME DIRECTORY IF CORRECT PATH IS GIVEN
	def GENERAL_PATH_TO_HOME_INODE_NUMBER(self, path):
		path_array = path.split('/')
		if len(path_array) > 1 and path_array[0] == '': return 0
		else: return -1


	#MAKES NEW
	def new_entry(self, path, type):
		if path == '/':   #SPECIAL CASE OF INITIALIZING FILE SYSTEM
			interface2.new_entry('/', -1, type)
			return
		inode_number_of_parent = self.GENERAL_PATH_TO_HOME_INODE_NUMBER(path)
		if inode_number_of_parent == -1:
			print("Error AbsolutePathLayer: Wrong Path!")
			return -1
		interface2.new_entry(path[1:], inode_number_of_parent, type)


	#IMPLEMENTS READ
	def read(self, path, offset, length):
		inode_number_of_parent = self.GENERAL_PATH_TO_HOME_INODE_NUMBER(path)
		if inode_number_of_parent == -1:
			print("Error AbsolutePathLayer: Wrong Path Given!\n")
			return -1
		return interface2.read(path[1:], inode_number_of_parent, offset, length)


	#IMPLEMENTS WRITE
	def write(self, path, offset, data):
		inode_number_of_parent = self.GENERAL_PATH_TO_HOME_INODE_NUMBER(path)
		if inode_number_of_parent == -1:
			print("Error AbsolutePathLayer: Wrong Path Given!\n")
			return -1
		interface2.write(path[1:], inode_number_of_parent, offset, data)


	#IMPLEMENTS THE HARDLINK
	def link(self, old_path, new_path):
		inode_number_of_parent = self.GENERAL_PATH_TO_HOME_INODE_NUMBER(old_path)
		if inode_number_of_parent == -1:
			print("Error AbsolutePathLayer: Wrong Path Given!\n")
			return -1
		interface2.link(old_path[1:], new_path[1:], inode_number_of_parent)


	#IMPLEMENTS DELETE
	def unlink(self, path):
		inode_number_of_parent = self.GENERAL_PATH_TO_HOME_INODE_NUMBER(path)
		if inode_number_of_parent == -1:
			print("Error AbsolutePathLayer: Wrong Path Given!\n")
			return -1
		interface2.unlink(path[1:], inode_number_of_parent)


	#MOVE
	def mv(self, old_path, new_path):
		inode_number_of_parent = self.GENERAL_PATH_TO_HOME_INODE_NUMBER(old_path)
		if inode_number_of_parent == -1:
			print("Error AbsolutePathLayer: Wrong Path Given!\n")
			return -1
		interface2.mv(old_path[1:], new_path[1:], inode_number_of_parent)


class AbsolutePathNameLayer3():

	#RETURNS INODE NUMBER OF HOME DIRECTORY IF CORRECT PATH IS GIVEN
	def GENERAL_PATH_TO_HOME_INODE_NUMBER(self, path):
		path_array = path.split('/')
		if len(path_array) > 1 and path_array[0] == '': return 0
		else: return -1


	#MAKES NEW
	def new_entry(self, path, type):
		if path == '/':   #SPECIAL CASE OF INITIALIZING FILE SYSTEM
			interface3.new_entry('/', -1, type)
			return
		inode_number_of_parent = self.GENERAL_PATH_TO_HOME_INODE_NUMBER(path)
		if inode_number_of_parent == -1:
			print("Error AbsolutePathLayer: Wrong Path!")
			return -1
		interface3.new_entry(path[1:], inode_number_of_parent, type)


	#IMPLEMENTS READ
	def read(self, path, offset, length):
		inode_number_of_parent = self.GENERAL_PATH_TO_HOME_INODE_NUMBER(path)
		if inode_number_of_parent == -1:
			print("Error AbsolutePathLayer: Wrong Path Given!\n")
			return -1
		return interface3.read(path[1:], inode_number_of_parent, offset, length)


	#IMPLEMENTS WRITE
	def write(self, path, offset, data):
		inode_number_of_parent = self.GENERAL_PATH_TO_HOME_INODE_NUMBER(path)
		if inode_number_of_parent == -1:
			print("Error AbsolutePathLayer: Wrong Path Given!\n")
			return -1
		interface3.write(path[1:], inode_number_of_parent, offset, data)


	#IMPLEMENTS THE HARDLINK
	def link(self, old_path, new_path):
		inode_number_of_parent = self.GENERAL_PATH_TO_HOME_INODE_NUMBER(old_path)
		if inode_number_of_parent == -1:
			print("Error AbsolutePathLayer: Wrong Path Given!\n")
			return -1
		interface3.link(old_path[1:], new_path[1:], inode_number_of_parent)


	#IMPLEMENTS DELETE
	def unlink(self, path):
		inode_number_of_parent = self.GENERAL_PATH_TO_HOME_INODE_NUMBER(path)
		if inode_number_of_parent == -1:
			print("Error AbsolutePathLayer: Wrong Path Given!\n")
			return -1
		interface3.unlink(path[1:], inode_number_of_parent)


	#MOVE
	def mv(self, old_path, new_path):
		inode_number_of_parent = self.GENERAL_PATH_TO_HOME_INODE_NUMBER(old_path)
		if inode_number_of_parent == -1:
			print("Error AbsolutePathLayer: Wrong Path Given!\n")
			return -1
		interface3.mv(old_path[1:], new_path[1:], inode_number_of_parent)
