class BankAccount:
    
    def __init__(self,id, owner_name, balance):
        self.id = id
        self.owner_name = owner_name
        self.balance = balance

    def add_balance(self):
        add_sum = float(input("Введіть суму, на яку хочете поповнити рахунок: "))
        info[1] = info[1] + add_sum

    def withdraw(self):
        withdraw_sum = float(input("Введіть суму, на яку хочете зняти рахунок: "))
        info[1] = info[1] - withdraw_sum

    def showAccount(id):
        return info




class Bank:
    def __init__(self) -> None:
        self.all_banks_account = {1009: ["Roman", 2000],
                     2009: ["Nazar", 3500],
                     1450: ["Danylo", 2350],
                     3457: ["Serhii", 4500] }
    
    

    def add_account(self, account: BankAccount):
        global info 
        info = [account.owner_name, account.balance]
        self.all_banks_account[account.id] = info
        print(self.all_banks_account)



    def delete(self):
        deleted = int(input("Введіть id акаунту, який бажаєте видалити:"))
        if deleted in self.all_banks_account:
            del self.all_banks_account[deleted]
        else:
            print(f"Акаунту з таким id {deleted} не існує")

    def sortByBalance(self):
        return sorted(self.all_banks_account.items(),key = lambda x: x[1][1], reverse=True)

if __name__ == "__main__":
    account1 = BankAccount(
        id = 1009, 
        owner_name = "asdf",
        balance = 100600)
    
    account2 = BankAccount(
        id = 1234, 
        owner_name = "User1",
        balance = 100500)

    privat = Bank()  
    privat.add_account(account1)
    account1.add_balance()
    print(privat.all_banks_account)

    privat.add_account(account2)
    account2.add_balance()
    print(privat.all_banks_account)
    
    for i in privat.sortByBalance():
        print(f"Account name: {i[1][0]}, account ballance: {i[1][1]}")

    print(">>>>> WITHDRAW")
    account2.withdraw()
    print(privat.all_banks_account)

    print(">>>>> DELETE")
    privat.delete()
    

    print(privat.all_banks_account)