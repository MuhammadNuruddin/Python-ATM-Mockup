from Account import Account

def show_options():
    print('Please make a selection...')
    print("""
    1. Check Balance 
    2. Withdraw
    3. Deposit
    4. Get Account Info
    5. Quit""")


def withdraw(Account):
    try:
        withdraw = float(input('How much do you want to withdraw? '))
        if(Account.get_balance() < withdraw):
            print('Insufficient Funds')
        else:
            Account.set_balance(Account.get_balance() - withdraw)
            print('Thank you for the transaction')
    except:
        print('Input not valid...')


def deposit(Account):
    try:
        deposit = float(input('How much do you want to deposit? '))
        Account.set_balance(Account.get_balance() + deposit)
        print(f'Thanks, your new available balance is {str(Account.get_balance())}')
    except:
        print('Input not valid...')

def balance(Account):
    print(f'Your current balance is {Account.get_balance()}')


def get_info(Account):
    Account.get_info()


if __name__ == '__main__':
    card_holder = Account('','','','','')

    accounts = []
    # accounts.append(Account('first_name','last_name','card_number','pin','balance'))
    accounts.append(Account('John','Doe','123343434',0000,126.99))
    accounts.append(Account('Isah','Kura','1233445454',2300,11.34))
    accounts.append(Account('X11','Y3R','113445665',4400,10.56))
    accounts.append(Account('Zeeyah','Kh','123345434',1900,100000.45))

    card_number = ''
    while True:
        try:
            card_number = input('Enter your card number: ')
            matched = [user for user in accounts if user.card_number == card_number]
            if(len(matched) > 0):
                card_holder = matched[0]
                break
            else:
                print('Card Number not recognized. Please try again')
        except:
            print('Card Number not valid')

    while True:
        try:
            pin = int(input('Please Enter your PIN: ').strip())
            if(card_holder.get_pin() == pin):
                break
            else:
                print('Incorrect PIN...')
        except:
            print('Invalid PIN')

    print(f'Welcome {card_holder.get_first_name()} {card_holder.get_last_name()}!')

    option = 0
    while True:
        show_options()
        try:
            option = int(input())
        except:
            print('Input not valid...')
        
        if (option == 1):
            balance(card_holder)
        elif (option == 2):
            withdraw(card_holder)
        elif (option == 3):
            deposit(card_holder)
        elif (option == 4):
            get_info(card_holder)
        elif (option == 5):
            break
        else:
            option = 0

    print('Thank you, have a lovely day!')