
import socket

# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

# Initialize the bank account with $100
balance = 100

print("ATM Server is running...")
print("Waiting for client connection...")

while True:
    # Accept a client connection
    client_socket, address = server_socket.accept()
    print(f"Client connected from {address}")

    # Keep the connection alive for multiple transactions
    while True:
        try:
            # Receive command from client
            data = client_socket.recv(1024).decode()

            if not data:
                break

            # Process the command
            parts = data.split()
            command = parts[0]

            if command == "BALANCE":
                # Send the current balance
                response = str(balance)
                client_socket.send(response.encode())

            elif command == "DEPOSIT":
                # Get the amount to deposit
                amount = int(parts[1])

                # Check if amount is valid
                if amount <= 0:
                    client_socket.send("ERROR: Amount must be positive".encode())
                else:
                    balance = balance + amount
                    response = "SUCCESS " + str(balance)
                    client_socket.send(response.encode())

            elif command == "WITHDRAW":
                # Get the amount to withdraw
                amount = int(parts[1])

                # Check if amount is valid
                if amount <= 0:
                    client_socket.send("ERROR: Amount must be positive".encode())
                elif amount > balance:
                    client_socket.send("ERROR: Insufficient funds".encode())
                else:
                    balance = balance - amount
                    response = "SUCCESS " + str(balance)
                    client_socket.send(response.encode())

            elif command == "QUIT":
                client_socket.send("GOODBYE".encode())
                break

            else:
                client_socket.send("ERROR: Invalid command".encode())

        except ValueError:
            # Handle non-integer amounts
            client_socket.send("ERROR: Amount must be a whole number".encode())
        except IndexError:
            # Handle missing amount
            client_socket.send("ERROR: Amount required".encode())
        except Exception as e:
            # Handle any other errors
            client_socket.send(f"ERROR: {str(e)}".encode())

    # Close the client connection
    client_socket.close()
    print("Client disconnected")
    print("Waiting for next client...")
    
