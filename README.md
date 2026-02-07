# ATM Banking System - TCP Socket Programming Assignment

FILES INCLUDED:

- server.py (Server program)
- client.py (Client program)
- readme.txt (This file)

# HOW TO RUN THE PROGRAMS:

## Step 1: Start the Server

Open a terminal window and run:
python3 server.py

The server will start and display:
"ATM Server is running..."
"Waiting for client connection..."

Keep this terminal open. The server needs to be running for clients to connect.

## Step 2: Start the Client

Open a NEW terminal window and run:
python3 client.py

You will see the ATM menu with options: 1. Check Balance 2. Deposit Money 3. Withdraw Money 4. Quit

## Step 3: Using the ATM

- Enter 1-4 to select an option
- For deposits and withdrawals, enter whole numbers only (no decimals)
- The initial balance is $100
- You cannot withdraw more than your current balance
- You can withdraw the entire balance (make it $0)

## Step 4: Exiting

- Choose option 4 to quit the client
- The server will keep running for other clients
- To stop the server, press Ctrl+C in the server terminal

# IMPORTANT NOTES:

- Both programs must be run with Python 3 (use "python3" command)
- The server must be started BEFORE the client
- Only whole positive numbers are accepted for deposits/withdrawals
- The balance persists across multiple client connections
- The server maintains all account data; the client only sends requests

# TESTING ON TURING:

1. SSH into turing.uark.edu
2. Upload all three files
3. Run the server: python3 server.py
4. Open another SSH session to turing
5. Run the client: python3 client.py

# ERROR HANDLING:

- The program checks for negative numbers
- The program checks for decimal numbers
- The program prevents overdrafts
- The program validates all user input
- Invalid inputs will display error messages but won't crash the programs

