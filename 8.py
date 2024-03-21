# 8-bo'lim
class SupermarketSales:
    def __init__(self, quantities, prices, sales):
        self.quantities = quantities
        self.prices = prices
        self.sales = sales

    def calculate_sales(self):
        total_sales = sum(s * p for s, p in zip(self.sales, self.prices))
        remaining_quantities = [q - s for q, s in zip(self.quantities, self.sales)]
        print(f"Total sales: {total_sales}")
        print(f"Remaining quantities: {remaining_quantities}")
        return total_sales, remaining_quantities



supermarket_sales = SupermarketSales(quantities=[100, 200, 150], prices=[1.5, 2.0, 0.5], sales=[50, 100, 75])

total_sales, remaining_quantities = supermarket_sales.calculate_sales()
