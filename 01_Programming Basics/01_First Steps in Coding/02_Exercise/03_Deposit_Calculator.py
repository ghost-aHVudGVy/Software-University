deposit_amount = float(input())
time_deposit_in_months = int(input())
annual_interest = float(input())

total_annual_interest = deposit_amount * (annual_interest / 100)

interest_per_month = total_annual_interest / 12

total_interest_for_the_period = interest_per_month * time_deposit_in_months

total = deposit_amount + total_interest_for_the_period
print(total)
