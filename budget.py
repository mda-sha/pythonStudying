import math

def num_len(num):
    l = len(str(num))
    if num - math.trunc(num) == 0:
        l += 3
    return l

class Category:

    ledger = 0
    name = ''

    def __init__(self, nm):
        self.name = nm
        self.ledger = list()

    def __str__(self):
        int_asterisk = (30 - (len(self.name))) / 2
        str_asterisk = ''
        while int_asterisk > 0:
            str_asterisk += "*"
            int_asterisk -= 1
        final_string = str_asterisk + self.name + str_asterisk
        final_string += "\n"
        for s in self.ledger:
            spaces = 30 - len(s["description"]) - num_len(s["amount"])
            if spaces >= 1:
                final_string += s["description"]
            else:
                final_string += s["description"][: 29 - num_len(s["amount"])]
                spaces = 1
            while spaces > 0:
                final_string += " "
                spaces -= 1
            final_string = final_string + str(s["amount"])
            if s["amount"] - math.trunc(s["amount"]) == 0:
                final_string += ".00"
            final_string += "\n"
        final_string = final_string + "Total: " + str(self.get_balance())
        return(final_string)

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
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


def countTotalSum(totals):
    sum = 0
    for i in totals:
        sum += i[0]
    return(sum)

def countPercentage(totals):
    sum = countTotalSum(totals)
    percentage = list()
    for i in totals:
        percentage.append(100 / sum * i[0])
    return(percentage)

def printNames(percentage, totals):
    print("    ", end='')
    dashes = len(percentage) * 3 + 1
    while dashes > 0:
        print('-', end = '')
        dashes-=1
    print("")
    maxLen = 0
    for i in totals:
        maxLen = max(maxLen, len(i[1]))
    i = 0
    while i  < maxLen:
        print("   ", end = '')
        for t in totals:
            if i < len(t[1]):
                print(" ", t[1][i], end = '')
            else:
                print("   ", end = '')
        print("  ", end='')
        i += 1
        print("")

def printPercentage(totals, percentage):
    print("Percentage spent by category")
    perc = 100
    while perc >= 0:
        if perc == 0:
            print("  ", end = '')
        elif perc < 100:
            print(" ", end = '')
        print(perc, "|", end='', sep = '')
        for i in percentage:
            if perc <= int(i):
                print(" o ", end = '')
            else:
                print("   ", end='')
        perc -=10
        print(' ')
    printNames(percentage, totals)

def create_spend_chart(categories):
    totals = list()
    for category in categories:
        sum = 0
        for s in category.ledger:
            if s["amount"] < 0:
                sum += -s["amount"]
        totals.append((sum, category.name))
    totals = sorted(totals, reverse=True)
    percentage = countPercentage(totals)
    printPercentage(totals, percentage)



# entertainment = Category("Entertainment")
# food = Category("Food")
# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# food.transfer(20, entertainment)
# print(food)


food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
actual = create_spend_chart([business, food, entertainment])