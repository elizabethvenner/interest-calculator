class Calculator:

    def calculate(self, amount, annual_interest, days):
        daily_interest_rate = annual_interest/365
        print(daily_interest_rate)
        interest_per_day = amount / 100 * daily_interest_rate
        print(interest_per_day)
        return interest_per_day * days
