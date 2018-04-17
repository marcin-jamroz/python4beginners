from zad2 import BankAccount
import pytest
from unittest import mock

@pytest.fixture
def bankAccount():
      return BankAccount()
    
def test_zero_on_new_account(bankAccount):
    assert bankAccount.get_balance() == 0

def test_balance_after_deposit(bankAccount):
    bankAccount.deposit(100)
    assert 100 == bankAccount.get_balance()

def test_balance_with_promo(bankAccount):
    with mock.patch('random.random') as mock_object:
        mock_object.return_value = 0.1
        bankAccount.deposit(100, with_promo=True)

    assert bankAccount.get_balance() == 101