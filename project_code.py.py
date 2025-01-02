import pandas as pd
employee_data = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Amit', 'age': 34, 'department': 'Engineering', 'salary': 75000},
    103: {'name': 'Priya', 'age': 29, 'department': 'Marketing', 'salary': 60000},
    104: {'name': 'Rahul', 'age': 40, 'department': 'Sales', 'salary': 55000}
}

def main_menu():
    while True:
        print("\n--Employee Management System--")
        print("1.Search Employee")
        print("2.view all Employee ")
        print("3 Add Employee ")
        print("4. Exit")
        choice=int(input("please choose option from 1 to 4"))
        if choice == 1:
            Search_employee()
        elif choice == 2:
            view_employees()
        elif choice == 3:
            add_employee()
        elif choice == 4:
            print("Thank you for using the Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
def add_employee():
    print("Enter Employee detail")
    try:
        emp_id=int(input("create id"))
    except ValueError:
        print("Invalid input for Employee ID. It must be an integer.")
        return
    if emp_id in employee_data:
        print("!employee ID already Exist")
        return
    name=input("Enter Name")
    try:
        age=int(input("Enter Age"))
        salary=float(input("Enter Salary"))
    except ValueError:
        print("invalid input!")
        return
    department=input("Department Name")
    employee_data[emp_id]={"name": name,
                          "age": age,
                          "Department": department,
                          "salary": salary}  
    print(f"Employee {name} added successfully!")

def Search_employee():
    try:
        emp_id=int(input("enter emp ID"))
    except ValueError:
        print("enter only emp ID e.g==101,102 etc")
        return
    if emp_id in employee_data:
        details=employee_data[emp_id]
        print(f"\nEmployee Found:")
        print(f"Name: {details['name']}")
        print(f"Age: {details['age']}")
        print(f"Department: {details['department']}")
        print(f"Salary: {details['salary']}")
    else:
        print("Employee not found.")
def view_employees():
    print("\n--- All Employees ---")
    df=pd.DataFrame(employee_data)
    print(df)
main_menu()
    
