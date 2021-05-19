class Category:

    ledger = []
    balance = 0

    def __init__(self, in_name: str):
        self.name = in_name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, in_name: str):
        self._name = in_name
    
    def deposit(self, in_amount, in_description = ""):
        self.ledger.append({"amount": in_amount, "description": in_description})
        self.balance +=in_amount
    
    def withdraw(self, out_amount, out_description = ""):
        if not self.check_funds(out_amount):
            return False
        
        self.deposit(-out_amount, out_description)
        return True
    
    def get_balance(self):
        return self.balance
    
    def check_funds(self, amount):
        return amount <= self.balance
    
    def transfer(self, amount : float, transfer_category):
        if not self.check_funds(amount):
            return False
        
        self.withdraw(amount, f"Transfer to {transfer_category.name}")

        transfer_category.deposit(amount, f"Transfer from {self.name}")

        return True

    def __repr__(self):
        num_stars = 30 - len(self.name)

        title = self.name.join(["*"*(num_stars // 2), "*" * (num_stars // 2 if num_stars % 2 == 0 else num_stars // 2+1)])


        body = [
            f"{entry['description'][:23]:<23}{entry['amount']:>7.2f}"
            for entry in self.ledger
        ]

        body = "\n".join(body)

        return "\n".join([title, body, f"Total: {self.balance:0.2f}"])


def create_spend_chart(categories):
    pass