from employee import Employee
import pytest


@pytest.fixture
def employee():
    return Employee('John', 'Smith', 10000)


def test_give_default_raise():
    employee = Employee('John', 'Smith', 10000)
    assert employee.give_raise() == 15000


def test_custom_raise(employee):
    assert employee.give_raise(10000) == 20000
