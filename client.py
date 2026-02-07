import socket

# Connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

print("Welcome to the ATM!")
print("Connected to the bank server.\n")

# Keep showing menu until user quits
while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Quit")
    print("====================")

    # Get user choice
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        # Check balance
        client_socket.send("BALANCE".encode())
        response = client_socket.recv(1024).decode()
        print(f"\nYour current balance is: ${response}")

    elif choice == "2":
        # Deposit money
        amount_str = input("Enter amount to deposit: $")

        # Check if it's a valid number
        try:
            amount = int(amount_str)
            if amount <= 0:
                print("Error: Please enter a positive whole number")
                continue
        except ValueError:
            print("Error: Please enter a whole number (no decimals or letters)")
            continue

        # Send deposit command
        message = f"DEPOSIT {amount}"
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()

        if response.startswith("SUCCESS"):
            new_balance = response.split()[1]
            print(f"Deposit successful! New balance: ${new_balance}")
        else:
            print(response)

    elif choice == "3":
        # Withdraw money
        amount_str = input("Enter amount to withdraw: $")

        # Check if it's a valid number
        try:
            amount = int(amount_str)
            if amount <= 0:
                print("Error: Please enter a positive whole number")
                continue
        except ValueError:
            print("Error: Please enter a whole number (no decimals or letters)")
            continue

        # Send withdraw command
        message = f"WITHDRAW {amount}"
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()

        if response.startswith("SUCCESS"):
            new_balance = response.split()[1]
            print(f"Withdrawal successful! New balance: ${new_balance}")
        else:
            print(response)

    elif choice == "4":
        # Quit
        client_socket.send("QUIT".encode())
        response = client_socket.recv(1024).decode()
        print("\nThank you for using our ATM!")
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4")

# Close the connection
client_socket.close()
