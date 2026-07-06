class BankAccount: 
    total_accounts: int = 0
    total_balance: int = 0
    
    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance

alice = BankAccount("Alice", 1000)
bob = BankAccount("Bob", 2000)

print(f"Alice's balance: ${alice.balance}")
print(f"Bob's balance: ${bob.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")

