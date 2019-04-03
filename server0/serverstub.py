#!/usr/bin/python
import SimpleXMLRPCServer,Memory

server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost",8000))
print("Listening on port 8000...")

filesystem = Memory.Operations()
server.register_function(Memory.Initialize)
server.register_function(filesystem.addr_inode_table)
server.register_function(filesystem.get_data_block)
server.register_function(filesystem.get_valid_data_block)
server.register_function(filesystem.free_data_block)
server.register_function(filesystem.update_data_block)
server.register_function(filesystem.inode_number_to_inode)
server.register_function(filesystem.update_inode_table)
server.register_function(filesystem.status)

# Start the server
try:
		print('Use Control-C to exit')
		server.serve_forever()
except KeyboardInterrupt:
	    print('Exiting')

