import csv


class financial_planner:

    def __init__(self,
                 current_annual_expense, current_annual_income, current_savings,
                 interest_expense, interest_income, interest_savings,
                 extra_expense):
        self.interest_expense = interest_expense
        self.interest_income = interest_income
        self.interest_savings = interest_savings
        self.annual_expense = current_annual_expense * (1 + (self.interest_expense / 100))
        self.annual_income = current_annual_income * (1 + (self.interest_income / 100))
        self.extra_expense = extra_expense
        self.initial_savings = current_savings + self.annual_income - self.annual_expense - extra_expense
        self.extra_savings = self.annual_income - self.annual_expense - extra_expense
        self.total_savings = self.initial_savings + self.extra_savings

    def get_tuple(self, age):
        return [age, self.annual_income, self.annual_expense, self.extra_expense, self.initial_savings, self.extra_savings, self.total_savings]


def generate_financial_account(name,
                               initial_age, retirement_age, death_age,
                               initial_annual_expense, initial_annual_income, initial_savings,
                               interest_expense, interest_income, interest_savings,
                               extra_expense):
    file_name = 'Financial_Status_' + name + '.csv'
    extra_annual_expense = {}
    for i in extra_expense:
        if initial_age <= i[0] <= death_age:
            if i[0] in extra_annual_expense:
                extra_annual_expense[i[0]] += i[1]
            else:
                extra_annual_expense[i[0]] = i[1]

    def calculate_extra_expense(extra_annual_expense, age):
        if age in extra_annual_expense.keys():
            extra_expense = extra_annual_expense[age]
        else:
            extra_expense = 0
        return extra_expense

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Age", "Annual Income", "Annual Expense", "Extra Expense", "Initial Savings", "Current Savings", "Total Savings"])
        extra_expense = calculate_extra_expense(extra_annual_expense, initial_age)
        previous_status = financial_planner(initial_annual_expense, initial_annual_income, initial_savings, 0, 0, 0, extra_expense)
        writer.writerow(previous_status.get_tuple(initial_age))

        for age in range(initial_age + 1, retirement_age+1):
            extra_expense = calculate_extra_expense(extra_annual_expense, age)
            status = financial_planner(previous_status.annual_expense, previous_status.annual_income,
                                       previous_status.total_savings, interest_expense, interest_income,
                                       interest_savings, extra_expense)
            writer.writerow(status.get_tuple(age))
            previous_status = status

        previous_status = financial_planner(status.annual_expense, 0, status.total_savings, interest_expense, interest_income,
                                       interest_savings, extra_expense)
        for age in range(retirement_age+1, death_age+1):
            extra_expense = calculate_extra_expense(extra_annual_expense, age)
            status = financial_planner(previous_status.annual_expense, previous_status.annual_income,
                                       previous_status.total_savings, interest_expense, interest_income,
                                       interest_savings, extra_expense)
            writer.writerow(status.get_tuple(age))
            previous_status = status


generate_financial_account('User1', 30, 55, 75, 500000, 1000000, 200000, 1.75, 2, 8, [(30, 500000), (55, 600000), (65, 50000)])
