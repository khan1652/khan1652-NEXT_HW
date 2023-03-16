class Bank:
    def __init__(self, total_amount, limit_for_loan, limit_for_withdrawal):
        self.total_amount = total_amount
        self.limit_for_loan = limit_for_loan
        self.limit_for_withdrawal = limit_for_withdrawal

def repeat_withdrawing_money(self, amount, limit_for_withdrawal):
    count = amount // limit_for_withdrawal
    rest = amount % limit_for_withdrawal

    for i in range(count):
        print(f'This is your money - {limit_for_withdrawal}')

        if i == (count-1):
            print(f'This is your money - {rest}')

def show_me_the_money(self, amount):
    if amount <= self.total_amount:
        self.repeat_withrawing_money(amount, self.limit_for_withdrawal)
    elif amount <= (self.total_amount + self.limit_for_loan):
        print('Wait!! Do you want loan?')
    else:
        print('Your money is not enough')