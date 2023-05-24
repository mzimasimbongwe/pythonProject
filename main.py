import os


# function to read the balance from Bank Data.txt
def read_balance():
    with open('Bank Data.txt', 'r') as f:
        balance = float(f.read())
    return balance


# function to write the balance to Bank Data.txt
def write_balance(balance):
    with open('Bank Data.txt', 'w') as f:
        f.write(str(balance))


# function to log the transaction in Transaction Log.txt
def log_transaction(transaction_type, amount, balance):
    with open('Transaction Log.txt', 'a') as f:
        f.write(f'{transaction_type}: {amount:.2f}, Balance: {balance:.2f}\n')


# function to handle deposit transactions
def deposit():
    amount = input('How much would you like to deposit? ')
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except ValueError:
        print('You provided an invalid input.')
        return
    balance = read_balance()
    balance += amount
    write_balance(balance)
    log_transaction('Deposit', amount, balance)
    print(f'Deposit successful. Current balance is {balance:.2f}.')


# function to handle withdrawal transactions
def withdraw():
    amount = input('How much would you like to withdraw? ')
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except ValueError:
        print('You provided an invalid input.')
        return
    balance = read_balance()
    if amount > balance:
        print('Insufficient funds.')
        return
    balance -= amount
    write_balance(balance)
    log_transaction('Withdrawal', amount, balance)
    print(f'Withdrawal successful. Current balance is {balance:.2f}.')


# main function to interact with the user and handle transactions
def main():
    print('Welcome to the Banking Application.')
    while True:
        make_transaction = input('Would you like to make a transaction? (Yes/No) ').lower()
        if make_transaction == 'yes':
            deposit_or_withdraw = input('Would you like to make a deposit or withdrawal? (Deposit/Withdrawal) ').lower()
            if deposit_or_withdraw == 'deposit':
                balance = read_balance()
                print(f'Current balance is {balance:.2f}.')
                deposit()
            elif deposit_or_withdraw == 'withdrawal':
                balance = read_balance()
                print(f'Current balance is {balance:.2f}.')
                withdraw()
            else:
                print('You provided an invalid input.')
        elif make_transaction == 'no':
            print('Thank you for using the Banking Application.')
            break
        else:
            print('You provided an invalid input.')


if __name__ == '__main__':
    if not os.path.exists('Bank Data.txt'):
        with open('Bank Data.txt', 'w') as f:
            f.write('0.00')
    if not os.path.exists('Transaction Log.txt'):
        with open('Transaction Log.txt', 'w') as f:
            pass
    main()
