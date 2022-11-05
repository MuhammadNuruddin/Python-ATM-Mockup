class Account():
    def __init__(self, first_name, last_name,card_number,pin,balance):
        self.first_name = first_name
        self.last_name = last_name
        self.card_number = card_number
        self.pin = pin
        self.balance = balance
    
    # ===
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_card_number(self):
        return self.card_number

    def get_pin(self):
        return self.pin

    def get_balance(self):
        return self.balance

    # ==== 
    def set_first_name(self,value):
        self.first_name = value 

    def set_last_name(self,value):
        self.last_name = value 

    def set_card_number(self,value):
        self.card_number = value 

    def set_pin(self,value):
        self.pin = value 

    def set_balance(self,value):
        self.balance = value   

    # =======
    def get_info(self):
        print(f'Account name: {self.first_name} {self.last_name}')
        print(f'Account Balance: {self.balance}')
        print(f'Card Number #: {self.card_number}')