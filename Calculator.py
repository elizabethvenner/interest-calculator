class Calculator:

    def calculate(self, amount, annual_interest, days):
        daily_interest_rate = annual_interest/365
        interest_per_day = amount / 100 * daily_interest_rate
        return interest_per_day * days
