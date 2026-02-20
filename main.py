"""Bank Account Management System (School OOP Demo).

Shows:
- Abstraction: `Account` is an abstract base class with `deposit`, `withdraw`,
  and `calculate_interest`.
- Encapsulation: account data is private and accessed via getter/setter methods.
- Polymorphism: the demo processes different account types through the same
  interface.
- Error handling: invalid deposits/withdrawals are handled cleanly.

Run:
    python main.py
"""

from abc import ABC, abstractmethod


class TransactionError(Exception):
    """Base error for transaction problems."""


class InvalidAmountError(TransactionError):
    """Raised when a deposit/withdraw amount is not valid."""


class InsufficientFundsError(TransactionError):
    """Raised when a withdrawal breaks account rules."""


class Account(ABC):
    """Abstract base class for all bank accounts."""

    def __init__(self, account_number: str, holder_name: str, opening_balance: float = 0.0) -> None:
        self.__account_number = self._clean_text(account_number, "Account number")
        self.__holder_name = self._clean_text(holder_name, "Holder name")
        self.__balance = float(opening_balance)

    # Encapsulation: getters/setters
    def get_account_number(self) -> str:
        return self.__account_number

    def get_holder_name(self) -> str:
        return self.__holder_name

    def set_holder_name(self, name: str) -> None:
        self.__holder_name = self._clean_text(name, "Holder name")

    def get_balance(self) -> float:
        return self.__balance

    # Protected helpers for subclasses
    @staticmethod
    def _clean_text(value: str, label: str) -> str:
        if not isinstance(value, str):
            raise ValueError(f"{label} must be a string.")
        value = value.strip()
        if not value:
            raise ValueError(f"{label} cannot be empty.")
        return value

    @staticmethod
    def _validate_amount(amount: float) -> float:
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            raise InvalidAmountError("Amount must be a number.")
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than 0.")
        return amount

    def _add_to_balance(self, delta: float) -> None:
        self.__balance += float(delta)

    # Abstract interface
    @abstractmethod
    def deposit(self, amount: float) -> None:
        """Add money to the account."""

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        """Remove money from the account (if allowed)."""

    @abstractmethod
    def calculate_interest(self) -> float:
        """Apply interest/fees and return the amount applied."""

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__} | "
            f"Acct#: {self.get_account_number()} | "
            f"Holder: {self.get_holder_name()} | "
            f"Balance: ${self.get_balance():,.2f}"
        )


class SavingsAccount(Account):
    """Savings account: minimum balance + monthly interest."""

    def __init__(
        self,
        account_number: str,
        holder_name: str,
        opening_balance: float = 0.0,
        annual_interest_rate: float = 0.03,
        minimum_balance: float = 0.0,
    ) -> None:
        super().__init__(account_number, holder_name, opening_balance)
        self.__annual_interest_rate = float(annual_interest_rate)
        self.__minimum_balance = float(minimum_balance)

        if self.__annual_interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        if self.get_balance() < self.__minimum_balance:
            raise InsufficientFundsError(
                f"Opening balance must be at least ${self.__minimum_balance:,.2f}."
            )

    # Encapsulation for subclass details
    def get_annual_interest_rate(self) -> float:
        return self.__annual_interest_rate

    def set_annual_interest_rate(self, rate: float) -> None:
        rate = float(rate)
        if rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        self.__annual_interest_rate = rate

    def get_minimum_balance(self) -> float:
        return self.__minimum_balance

    def set_minimum_balance(self, minimum: float) -> None:
        self.__minimum_balance = float(minimum)

    def deposit(self, amount: float) -> None:
        amount = self._validate_amount(amount)
        self._add_to_balance(amount)

    def withdraw(self, amount: float) -> None:
        amount = self._validate_amount(amount)
        if self.get_balance() - amount < self.__minimum_balance:
            raise InsufficientFundsError(
                f"Cannot go below minimum balance (${self.__minimum_balance:,.2f})."
            )
        self._add_to_balance(-amount)

    def calculate_interest(self) -> float:
        monthly_rate = self.__annual_interest_rate / 12
        interest = self.get_balance() * monthly_rate
        self._add_to_balance(interest)
        return interest

    def __str__(self) -> str:
        return super().__str__() + (
            f" | APR: {self.__annual_interest_rate * 100:.2f}%"
            f" | MinBal: ${self.__minimum_balance:,.2f}"
        )


class CurrentAccount(Account):
    """Current account: overdraft allowed up to a limit.

    If balance is negative, a monthly overdraft charge is applied.
    """

    def __init__(
        self,
        account_number: str,
        holder_name: str,
        opening_balance: float = 0.0,
        overdraft_limit: float = 500.0,
        overdraft_annual_rate: float = 0.18,
    ) -> None:
        super().__init__(account_number, holder_name, opening_balance)
        self.__overdraft_limit = float(overdraft_limit)
        self.__overdraft_annual_rate = float(overdraft_annual_rate)

        if self.__overdraft_limit < 0:
            raise ValueError("Overdraft limit cannot be negative.")
        if self.__overdraft_annual_rate < 0:
            raise ValueError("Overdraft rate cannot be negative.")
        if self.get_balance() < -self.__overdraft_limit:
            raise InsufficientFundsError(
                f"Opening balance cannot be below -${self.__overdraft_limit:,.2f}."
            )

    # Encapsulation for subclass details
    def get_overdraft_limit(self) -> float:
        return self.__overdraft_limit

    def set_overdraft_limit(self, limit: float) -> None:
        limit = float(limit)
        if limit < 0:
            raise ValueError("Overdraft limit cannot be negative.")
        self.__overdraft_limit = limit

    def get_overdraft_annual_rate(self) -> float:
        return self.__overdraft_annual_rate

    def set_overdraft_annual_rate(self, rate: float) -> None:
        rate = float(rate)
        if rate < 0:
            raise ValueError("Overdraft rate cannot be negative.")
        self.__overdraft_annual_rate = rate

    def deposit(self, amount: float) -> None:
        amount = self._validate_amount(amount)
        self._add_to_balance(amount)

    def withdraw(self, amount: float) -> None:
        amount = self._validate_amount(amount)
        if self.get_balance() - amount < -self.__overdraft_limit:
            raise InsufficientFundsError(
                f"Overdraft limit exceeded (-${self.__overdraft_limit:,.2f})."
            )
        self._add_to_balance(-amount)

    def calculate_interest(self) -> float:
        if self.get_balance() >= 0:
            return 0.0
        monthly_rate = self.__overdraft_annual_rate / 12
        charge = self.get_balance() * monthly_rate  # negative number
        self._add_to_balance(charge)
        return charge

    def __str__(self) -> str:
        return super().__str__() + (
            f" | OD Limit: ${self.__overdraft_limit:,.2f}"
            f" | OD APR: {self.__overdraft_annual_rate * 100:.2f}%"
        )


def run_demo() -> None:
    accounts = [
        SavingsAccount("SAV-1001", "Ava Patel", opening_balance=1000, annual_interest_rate=0.04, minimum_balance=100),
        CurrentAccount("CUR-2001", "Noah Kim", opening_balance=200, overdraft_limit=300, overdraft_annual_rate=0.20),
    ]

    # Encapsulation demo
    accounts[0].set_holder_name("Ava P.")

    print("Accounts:")
    for acc in accounts:
        print("-", acc)

    print("\nTransactions (polymorphic):")
    for acc in accounts:
        print("\n" + "-" * 60)
        print("Start:", acc)

        for action, amount in [("deposit", 250), ("withdraw", 120), ("withdraw", 10_000), ("deposit", -5)]:
            try:
                if action == "deposit":
                    acc.deposit(amount)
                else:
                    acc.withdraw(amount)
                print(f"{action.title()} ${float(amount):,.2f} -> Balance: ${acc.get_balance():,.2f}")
            except TransactionError as exc:
                print(f"Rejected {action}(${float(amount):,.2f}): {exc}")

        applied = acc.calculate_interest()
        if applied > 0:
            print(f"Interest credited: ${applied:,.2f}")
        elif applied < 0:
            print(f"Overdraft charge: ${abs(applied):,.2f}")
        else:
            print("No interest/charges applied.")

        print("End:  ", acc)


if __name__ == "__main__":
    run_demo()
