from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date
from rich import print



if __name__ == '__main__':
    
    today = date.today()
    print(f'Текущая дата: {today}')
    calculate_salary()
    get_employees()