class BankAccount:
  def __init__(self, account_holder, initial_balance=0):
    self.account_holder = account_holder
    self.balance = initial_balance
    self.transaction_history = []

  def deposite(self, amount):
    if amount <= 0:
      raise ValueError("Deposit amount must be positive")
    self.balance += amount
    self.transaction_history.append(f"Deposited: ${amount}")
    print(f"Deposited ${amount}, Current Balance: ${self.balance}")

  def withdraw(self, amount):
    if amount <=0:
      raise ValueError("withdraw amount must be positive")
    if amount > self.balance:
      raise ValueError("Insufficient funds for this withdraw.")
    self.balance -= amount
    self.transaction_history.append(f"withdraw: ${amount}")
    print(f"Withdraw ${amount}. Current balance: ${self.balance}")

  def check_balance(self):
    print(f"current balance: ${self.balance}")

  def transaction_history_func(self):
    print("Transaction History:")
    if len(self.transaction_history) == 0:
      print("No Transaction yet.")
    for transaction in self.transaction_history:
      print(transaction)


def main():
  print("Welcome to the Mini Banking System!")
  name = input("Enter your name: ")

  while True:
    try:
      initial_balance = float(input("Enter your initial deposit: $"))
      if initial_balance < 0:
        raise ValueError("Initial Deposite must be non negative.")
      account = BankAccount(name, initial_balance)
      break
    except ValueError as e:
      print(f"Error: {e}, Please try again.")

  while True:
    print("\n--- Menu ---")
    print("1. Deposite")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. View Transaction History")
    print("5. Exit")

    try:
      choice = int(input("Enter your choice: "))
      if choice == 1:
        deposite_amount = float(input("Enter amount to deposite: $"))
        account.deposite(deposite_amount)
      elif choice == 2:
        withdraw_amount = float(input("Enter amount to withdraw: $"))
        account.withdraw(withdraw_amount)
      elif choice == 3:
        account.check_balance()
      elif choice == 4:
        account.transaction_history_func()
      elif choice == 5:
        print("Thank you for using the Mini Banking System! Goodbye!")
        break
      else:
        print("Invald choice. Please choose a valid option.")
    except ValueError as e:
      print(f"Error: {e}. Please enter a valid number")

if __name__ == '__main__':
  main()
