# 7-bo'lim
class BankProfit:
    def __init__(self, amounts, interest_rates):
        self.amounts = amounts
        self.interest_rates = interest_rates

    def calculate_profit(self):
        total_profit = sum(a * r / 100 for a, r in zip(self.amounts, self.interest_rates))
        print(f"Total profit: {total_profit}")
        return total_profit


bank_profit = BankProfit(amounts=[1000, 2000, 3000], interest_rates=[5, 2, 3])
bank_profit.calculate_profit() 
