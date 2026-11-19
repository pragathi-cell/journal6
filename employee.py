
import sys

def employee_details(name, emp_id, department, salary):
    return (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Please provide employee details!")
        print("Usage: py employee.py name id department salary")
        sys.exit(1)

    name = sys.argv[1]
    emp_id = sys.argv[2]
    department = sys.argv[3]
    salary = sys.argv[4]

    print(employee_details(name, emp_id, department, salary))
    print("usn:01fe25bca151")
