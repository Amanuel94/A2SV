class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """

        self.balance = balance
        self.number_of_accounts = len(balance)
        

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """

        if account1 <= self.number_of_accounts and account2 <= self.number_of_accounts and self.balance[account1-1] >= money:

            self.balance[account1-1] -=  money
            self.balance[account2-1] += money

            return True

        else:
            return False

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if account <= self.number_of_accounts:

            self.balance[account-1]+=money
            return True

        return False

        

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if account <= self.number_of_accounts and self.balance[account-1] >= money:

            self.balance[account-1]-=money
            return True

        return False



# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
