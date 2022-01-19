class Category:

    ledger = list()
    name = ''

    def __init__(self, nm):
        self.name = nm

    def __str__(self):
        int_asterisk = (30 - (len(self.name) - 1)) / 2
        str_asterisk = ''
        while int_asterisk > 0:
            str_asterisk += "*"
            int_asterisk -= 1
        final_string = str_asterisk + self.name + str_asterisk
        final_string += "\n"
        for s in self.ledger:
            spaces = 30 - len(s["description"]) - len(str((s["amount"])))
            final_string += s["description"]
            while spaces >= 0:
                final_string += " "
                spaces -= 1
            final_string = final_string + str(s["amount"]) + "\n"
        final_string = final_string + "Total: " + str(self.get_balance())
        return(final_string)

    def deposit(self, amount, description):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description):
        if self.check_funds(amount) == False:
            return(False)
        self.ledger.append({"amount": amount * -1, "description": description})
        return(True)

    def get_balance(self):
        summ = 0
        for i in self.ledger:
            summ += i["amount"]
        return(summ)

    def transfer(self, amount, category):
        if self.withdraw(amount, "Transfer to " + category.name) == False:
            return(False)
        category.deposit(amount, "Transfer from " + self.name)
        return(True)
    
    def check_funds(self, amount):
        self.get_balance()
        if amount > self.get_balance():
            return(False)
        return(True)


# def create_spend_chart(categories):




t = Category("qwert")
t.deposit(500, "lalala")
t.withdraw(300, "blabla")
print(t)