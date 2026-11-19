
from employee import employee_details

def test_employee_details():
    result = employee_details(
        "Pragathi", "151", "BCA", "45000"
    )

    expected = (
        "Employee Name: Pragathi\n"
        "Employee ID: 151\n"
        "Department: BCA\n"
        "Salary: 45000"
    )

    assert result == expected
