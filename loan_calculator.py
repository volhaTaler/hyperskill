import math
import sys

# write your code here

def period_type(principal, payment, interest):
    loan_principal = principal
    monthly_payment = payment
    loan_interest = interest
    i = loan_interest / 1200
    base = i + 1
    numerator = monthly_payment / (monthly_payment - i * loan_principal)
    n = math.ceil(math.log(numerator, base))
    n = int(n)
    overpayment = int(n * monthly_payment - loan_principal)
    if n < 24:
        if n == 1:
            print("It will take 1 month to repay this loan!")
            print(f"Overpayment = {overpayment}")
        elif n < 12:
            print(f"It will take {n} months to repay this loan!")
            print(f"Overpayment = {overpayment}")
        elif n == 13:
            print("It will take 1 year and 1 month to repay this loan!")
            print(f"Overpayment = {overpayment}")
        else:
            months = n - 12
            print(f"It will take 1 year and {months} months to repay this loan!")
            print(f"Overpayment = {overpayment}")  
        elif n % 12 == 0:
            n = int(n / 12)
            print(f"It will take {n} years to repay this loan!")
            print(f"Overpayment = {overpayment}")
        else:
            years = int(n / 12) 
            months = n - (years * 12)
            if months == 1:
                print(f"It will take {years} years and 1 month to repay this loan!")
                print(f"Overpayment = {overpayment}")
            else:
                print(f"It will take {years} years and {months} months to repay this loan!")
                print(f"Overpayment = {overpayment}")


def loan_type(payment, interest, periods):
    annuity_payment = payment
    num_periods = periods
    loan_interest = interest
    i = loan_interest / 1200
    base = i + 1
    loan_principal = annuity_payment / (i * math.pow(base, num_periods) / (math.pow(base, num_periods) - 1))
    loan_principal = math.ceil(loan_principal)
    overpayment = num_periods * annuity_payment - loan_principal
    print(f"Your loan principal = {loan_principal}!")  
    print(f"Overpayment = {overpayment}")
    

def payment_type(principal, periods, interest):
    loan_principal = principal
    num_periods = periods
    loan_interest = interest
    i = loan_interest / 1200
    base = i + 1
    power_part = math.pow(base, num_periods)
    div_result = i * power_part / (power_part - 1)
    monthly_payment = math.ceil(loan_principal * div_result)
    overpayment = monthly_payment * periods - principal
    print(f"Your annuity payment = {monthly_payment}!")
    print(f"Overpayment = {overpayment}")

if len(sys.argv) == 5:   
    params = {}
    
    for i in range(1, len(sys.argv)):
        p, value = sys.argv[i].split("=")
        params[p[2:]] = value
    operation_type = params["type"]
    keys = params.keys()
    if operation_type == "diff" and "payment" not in keys and "interest" in keys:
        principal = float(params["principal"])
        periods = int(params["periods"])
        interest = float(params["interest"])
        if principal > 0 and periods > 0 and interest > 0:
            lst_payments = []
            i = interest / 1200
            for j in range(periods):
                j += 1
                loan_part = principal * (j - 1) / periods
                payment = principal / periods + i * (principal - (loan_part))
                lst_payments.append(math.ceil(payment))
                
            overpayment = sum(lst_payments) - principal
            for i, p in enumerate(lst_payments):
                month = i + 1
                print(f"Month {month}: payment is {p}")
            print(f"Overpayment = {overpayment}")
        else:
            print("Incorrect parameters")
    elif operation_type == "annuity" and "interest" in keys:
        if "payment" not in keys:
            principal = float(params["principal"])
            interest = float(params["interest"])
            periods = int(params["periods"])
            if principal > 0 and periods > 0 and interest > 0:
                payment_type(principal=principal, interest=interest, periods=periods)
            else:
                 print("Incorrect parameters")
        elif "principal" not in keys:
            payment = float(params["payment"])
            interest = float(params["interest"])
            periods = int(params["periods"])
            if payment > 0 and interest > 0 and periods > 0:
                loan_type(payment=payment, interest=interest, periods=periods)
            else:
                print("test 9")
                print('Incorrect parameters')
        elif "periods" not in keys:
            payment = float(params["payment"])
            interest = float(params["interest"])
            principal = float(params["principal"])
            if payment > 0 and interest > 0 and principal > 0:
                period_type(payment=payment, interest=interest, principal=principal)
            else:
                print('Incorrect parameters')  
    else:
        print('Incorrect parameters')
else:   
    print('Incorrect parameters')