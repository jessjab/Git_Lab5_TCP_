Program Title: TCP SOCKET Program

Modules and their IOs for this program:

		Client_TCP: keyboard input = Server IP Adress, UDP Port Number, Input File Name- ---------->Press enter
				   example = "127.0.0.1 5010 TCP_file.txt"----------------------------------------------------->Press enter 

		Server_TCP: keyboard input= TCP Port Number, Output file name
				   example = "5010 TCP_Output_file.txt"--------------------------------------->Press enter

		*RUN SERVER THEN CLIENT*

What this program does:

	1. Sets up a socket between multiple (at least 2) clients and a server, where the server waits and listens for messages from the client.
	2. The client accepts the above defined inputs (server's IP address, port number, input file name) from the keyboard and and reads the file 1024 bytes at a time.
	3. After each 1024 byte chunk is read in, the client sends it using TCP commands.
	4. The client then close when the entire file has been sent.
	

	5. The server accepts the above defined inputs (the port number, output file name). 
	6. When the server recieves the 1024 byte chunks from the client(s), the server writes them to the output file.