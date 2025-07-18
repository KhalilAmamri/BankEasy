from client import Client
from account import Account

# Add a new client
new_client = Client("John Doe", "john@example.com")
new_client.add_to_db()

# Add a new account
new_account = Account("Savings", 1000.0, 1)  # Example: name, balance, client_id
new_account.add_to_db()

# Print all clients
print("Clients:")
for client in Client.get_all():
    print(f"ID: {client[0]}, Name: {client[1]}, Email: {client[2]}")

# Print all accounts
print("\nAccounts:")
for account in Account.get_all():
    print(f"ID: {account[0]}, Name: {account[1]}, Balance: {account[2]}, Client ID: {account[3]}")

