from application.salary import calculate_salary
from application.db.peaple import get_employees
from datetime import date
from rich import print

today = date.today()

if __name__ == '__main__':
    print(f'Текущая дата: {today}')
    calculate_salary()
    get_employees()