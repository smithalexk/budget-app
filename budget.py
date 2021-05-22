class Category:

    def __init__(self, in_name: str):
        self.name = in_name
        self.balance = 0
        self.ledger = []
    
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
    o_title = "Percentage spent by category"

    spend_per = [
        abs(
            sum(trans['amount'] for trans in cat.ledger if trans['amount'] < 0)
        )
        * 100
        // cat.ledger[0]['amount']
        for cat in categories
    ]

    spend_tot = sum(spend_per)

    spend_per = [ int(x*10 // spend_tot * 10) for x in spend_per]

    o_num = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

    o_data = []
    for idx, num in enumerate(o_num):
        o_data.append(f"{num:>3}|")

        for per in spend_per:
            if per >= num:
                o_data[idx] = " ".join([o_data[idx], "o "])
            else:
                o_data[idx] = " ".join([o_data[idx], "  "])
        
        o_data[idx] = "".join([o_data[idx]," "])
    
    o_dashes = 4*" " + "-" + (3*"-")*len(spend_per)

    cats = [cat.name for cat in categories]
    
    o_cats = []
    max_str = len(max(cats, key=len))
    for idx in range(max_str):
        o_cats.append("   ")
        for cat in cats:
            if len(cat) > idx:
                o_cats[idx] = "  ".join([o_cats[idx], cat[idx]])
            else:
                o_cats[idx] = "  ".join([o_cats[idx], " "])
        
        o_cats[idx] = "".join([o_cats[idx],"  "])

    o_data = "\n".join(o_data)
    o_cats = "\n".join(o_cats)

    return "\n".join([o_title, o_data, o_dashes, o_cats])
        
   



    
