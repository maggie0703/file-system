'''
THIS MODULE IS THE BLOCK LAYER OF THE FILE SYSTEM. IT ONLY DEALS WITH THE BLOCKS. THIS IS THE LOWEST LAYER OF THE FILE SYSTEM AND USES
HANDLE OF CLIENT STUDB TO CALL API FUNCTIONS OF STUB TO CONTACT TO SERVER.

'''
import MemoryInterface


functions=MemoryInterface.fcn()
class BlockLayer0():

    #RETURNS DATA BLOCK FROM THE BLOCK NUMBER
    def BLOCK_NUMBER_TO_DATA_BLOCK(self, block_number):
        return ''.join(functions.get_data_block0(block_number))


    #PROVIDES DATA AND BLOCK NUMBER ON WHICH DATA IS TO BE WRITTEN
    def update_data_block(self, block_number, block_data):
        functions.update_data_block0(block_number, block_data)


    #ASKS FOR VALID DATA BLOCK NUMBER
    def get_valid_data_block(self):
        return functions.get_valid_data_block0()


    #REMOVES THE INVALID BLOCK NUMBER.
    def free_data_block(self, block_number):
        functions.free_data_block0(block_number)

class BlockLayer1():

    #RETURNS DATA BLOCK FROM THE BLOCK NUMBER
    def BLOCK_NUMBER_TO_DATA_BLOCK(self, block_number):
        return ''.join(functions.get_data_block1(block_number))


    #PROVIDES DATA AND BLOCK NUMBER ON WHICH DATA IS TO BE WRITTEN
    def update_data_block(self, block_number, block_data):
        functions.update_data_block1(block_number, block_data)


    #ASKS FOR VALID DATA BLOCK NUMBER
    def get_valid_data_block(self):
        return functions.get_valid_data_block1()


    #REMOVES THE INVALID BLOCK NUMBER.
    def free_data_block(self, block_number):
        functions.free_data_block1(block_number)

class BlockLayer2():

    #RETURNS DATA BLOCK FROM THE BLOCK NUMBER
    def BLOCK_NUMBER_TO_DATA_BLOCK(self, block_number):
        return ''.join(fcn.get_data_block2(block_number))


    #PROVIDES DATA AND BLOCK NUMBER ON WHICH DATA IS TO BE WRITTEN
    def update_data_block(self, block_number, block_data):
        functions.update_data_block2(block_number, block_data)


    #ASKS FOR VALID DATA BLOCK NUMBER
    def get_valid_data_block(self):
        return functions.get_valid_data_block2()


    #REMOVES THE INVALID BLOCK NUMBER.
    def free_data_block(self, block_number):
        functions.free_data_block2(block_number)

class BlockLayer3():

    #RETURNS DATA BLOCK FROM THE BLOCK NUMBER
    def BLOCK_NUMBER_TO_DATA_BLOCK(self, block_number):
        return ''.join(functions.get_data_block3(block_number))


    #PROVIDES DATA AND BLOCK NUMBER ON WHICH DATA IS TO BE WRITTEN
    def update_data_block(self, block_number, block_data):
        functions.update_data_block3(block_number, block_data)


    #ASKS FOR VALID DATA BLOCK NUMBER
    def get_valid_data_block(self):
        return functions.get_valid_data_block3()


    #REMOVES THE INVALID BLOCK NUMBER.
    def free_data_block(self, block_number):
        functions.free_data_block3(block_number)


    