import pickle

def add_to_file(filename, newContent):
    addFile = open(filename, "ab")
    pickle.dump(newContent, addFile)
    addFile.close()

def load_to_list(filename, listname):
    f = open(filename, "rb")
    while True:
        try:
            newLoad = pickle.load(f)
            listname.append(newLoad)
        except EOFError:
            f.close()
            break

class Customer:
    def __init__(self):
        self.cid = ""
        self.cname = ""
        self.acc_no = ""
        self.balance = ""
        self.credit_card = ""

    def create_new_cust(self):
        self.cid = str(input("Enter Customer ID: "))
        self.cname = str(input("Enter Customer Name: "))
        self.acc_no = str(input("Enter Account Number: "))
        self.balance = int(input("Enter Balance: "))

    def display_cust(self):
        print("ID = " + str(self.cid))
        print("Name = " + str(self.cname))
        print("Account Number = " + str(self.acc_no))
        print("Balance = " + str(self.balance))
        print("Credit Card Number = " + str(self.credit_card))

    def add_card(self, card_num):
        self.credit_card = card_num

class Card:
    def __init__(self):
        self.card_no = ""
        self.cvv = ""
        self.expiry_date = ""
        self.balance = ""

    def create_card(self):
        self.card_no = str(input("Enter Card Number: "))
        self.cvv = str(input("Enter CVV: "))
        self.expiry_date = str(input("Enter Expiry Date: "))

    def update_bal(self, new_bal):
        self.balance = new_bal

    def display_card(self):
        print("Card Number = " + str(self.card_no))
        print("CVV = " + str(self.cvv))
        print("Expiry Date = " + str(self.expiry_date))
        print("Balance = " + str(self.balance))

customerList = []
cardList = []

load_to_list("customer.dat", customerList)
load_to_list("card.dat", cardList)

while True:
    user_choice = input("1. Create new customer\n2. Create new card\n3. Transfer funds\n4. Assign card"
                        "\n5. Display customers\n6. Display card information\n7. Exit\n")
    if user_choice == "1":
        newCustomer = Customer()
        newCustomer.create_new_cust()
        add_to_file("customer.dat", newCustomer)
        customerList.append(newCustomer)
    elif user_choice == "2":
        newCard = Card()
        newCard.create_card()
        add_to_file("card.dat", newCard)
        cardList.append(newCard)
    elif user_choice == "3":
        id_from = input("Enter Customer ID to transfer from: ")
        id_to = input("Enter Customer ID to transfer to: ")
        bal_transfer = int(input("Enter Balance to transfer: "))
        for i in range(len(customerList)):
            try:
                cust_from = customerList[i]
                if cust_from.cid == id_from:
                    for j in range(len(customerList)):
                        try:
                            cust_to = customerList[j]
                            if cust_to.cid == id_to:
                                if bal_transfer <= cust_from.balance:
                                    cust_from.balance = cust_from.balance - bal_transfer
                                    cust_to.balance = cust_to.balance + bal_transfer
                                    cust_from.display_cust()
                                    try:
                                        for k in range(len(cardList)):
                                            update_card_bal = cardList[i]
                                            if update_card_bal.card_no == cust_from.credit_card:
                                                update_card_bal.balance = cust_from.balance
                                            elif update_card_bal.card_no == cust_to.credit_card:
                                                update_card_bal.balance = cust_to.balance
                                    except IndexError:
                                        print("Invalid Card Number")
                                else:
                                    print("Transfer is greater than balance")
                        except IndexError:
                            print("Invalid customer to ID")
            except IndexError:
                print("Invalid customer from ID")

    elif user_choice == "4":
        customer_id = input("Enter Customer ID: ")
        card_info = input("Enter card number: ")
        try:
            for i in range(len(cardList)):
                try:
                    card = cardList[i]
                    if card.card_no == card_info:
                        for j in range(len(customerList)):
                            add_card_cust = customerList[j]
                            if add_card_cust.cid == customer_id:
                                add_card_cust.add_card(card_info)
                                card.update_bal(add_card_cust.balance)
                except IndexError:
                    print("Invalid user ID")
        except IndexError:
            print("Invalid card number")
    elif user_choice == "5":
        for i in range(len(customerList)):
            cust = customerList[i]
            cust.display_cust()
    elif user_choice == "6":
        for i in range(len(cardList)):
            card = cardList[i]
            card.display_card()
    elif user_choice == "7":
        break

    saveCust = open("customer.dat", "wb")
    for i in customerList:
        pickle.dump(i, saveCust)
    saveCust.close()
    saveCard = open("card.dat", "wb")
    for i in cardList:
        pickle.dump(i, saveCard)
    saveCard.close()
    print("")