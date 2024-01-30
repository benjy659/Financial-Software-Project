"""
Description: A class meant to manage Mortgage options.
Author: Benjamin Omoregie
Date: 11/11/2023
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""

from mortgage.pixell_lookup import MortgageRate, MortgageFrequency, VALID_AMORTIZATION

class Mortgage:
   # A class used to manage mortgage options.
    def __init__(self, loan_amount: float, rate: MortgageRate, frequency: MortgageFrequency, Amortization: int):
        """
        Initialize a new mortgage object with a loan amount, rate, frequency and amortization.
        Loan Amount (float): The amount of the mortgage loan.
        Rate (MortgageRate): The annual interest rate.
        Frequency (int): The number of payments per year.
        Amortization (int): The number of years to repay the mortgage loan.
        returns: 
            None
        raises:
            value error: When the loan amount is negative.
            value error: When the rate provided is invalid.
            value error: When the frequency provided is invalid.
            value error: When the amortization provided is invalid.
        """
        if loan_amount > 0:
            self._loan_amount = loan_amount
        else:
            raise ValueError("Loan amount must be positive.")
        if isinstance(rate, MortgageRate):
            self._rate = rate
        else:
            raise ValueError("Rate provided is invalid.")
        if isinstance(frequency, MortgageFrequency):
            self._frequency = frequency
        else:
            raise ValueError("Frequency provided is invalid.")
        if Amortization in VALID_AMORTIZATION:
            self._amortization = Amortization
        else:
            raise ValueError("Amortization provided is invalid.")
        
     # Accessors for Loan Amount
    @property
    def loan_amount(self) -> float:
        """
        The loan amount property.
        returns: 
            The loan amount as a float.
        """
        return self._loan_amount
    
     # Mutators for Loan Amount
    @loan_amount.setter
    def loan_amount(self, amount: float):
        """
        The loan amount mutator.
        args:
            loan_amount(float): The new loan amount must be a float.
        returns:
            None
        raises:
            ValueError: When the loan amount is Zero or negative.
        """
        if amount > 0:
            self._loan_amount = amount
        else:
            raise ValueError("Loan amount must be positive.")
    
    #Accessors for Rate
    @property
    def rate(self) -> MortgageRate:
        """
        The rate property.
        returns: 
            The rate if in MortgageRate class.
        """
        return self._rate
    #Mutators for Rate
    @rate.setter
    def rate(self, value: MortgageRate):
        """
        The rate mutator.
        args:
            rate(MortgageRate): The new rate must be in MortgageRate class.
        returns:
            None
        raises:
            ValueError: When the rate is not in MortgageRate class.
        """
        if  isinstance(value, MortgageRate):
            self._rate = value
        else:
            raise ValueError("Rate provided is invalid.")
        
    
    #Accessors for Frequency
    @property
    def frequency(self) -> MortgageFrequency:
        """
        The frequency property.
        returns: 
            The frequency if in MortgageFrequency class.
        """
        return self._frequency
    #Mutators for Frequency
    @frequency.setter
    def frequency(self, value: MortgageFrequency):
        """
        The frequency mutator.
        args:
            frequency(MortgageFrequency): The new frequency must be in MortgageFrequency class.
        returns:
            None
        raises:
            ValueError: When the frequency is not in MortgageFrequency class.
        """  
        if isinstance(value, MortgageFrequency):
            self._frequency = value
        else:
            raise ValueError("Frequency provided is invalid.")
    
    #Accessors for Amortization
    @property
    def amortization(self) -> int:
        """
        The amortization property.
        returns: 
            The amortization as an int.
        """
        return self._amortization
    
    #Mutators for Amortization
    @amortization.setter
    def amortization(self, value: int):
        """
        The amortization mutator.
        args:
            amortization(int): The new amortization must be an integer.
        returns:
            None
        raises:
            ValueError: When the amortization is not in VALID_AMORTIZATION.
        """
        if value in VALID_AMORTIZATION:
            self._amortization = value
        else:
            raise ValueError("Amortization provided is invalid.")
        
    # Calculate the mortgage payment.
    def calculate_payment(self) -> float:
        """
        Calculate the mortgage payment.
        returns:
            The mortgage payment as a float.
        """
        i = self._rate.value / self._frequency.value
        n = self._amortization * self._frequency.value
        loan_amount = self._loan_amount

        payment = loan_amount * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
        payment = round(payment, 2)
        return payment
    
    # __str__ representation for mortgage payments.
    def __str__(self) -> str:
        """
        The string representation for a mortgage payment.
        returns:
            The mortgage amount, Rate, Amorization and frequency  as a string.
        """
        return (f"Mortage Amount: ${self._loan_amount:,.2f}"
                + f"\nRate: {self._rate.value:.2%}"
                + f"\nAmortization: {self._amortization}"
                + f"\nFrequency: {self._frequency.name} -- Calculated Payment: ${self.calculate_payment():,.2f}")
    
    # __repr__ representation for mortgage payments.
    def __repr__(self) -> str:
        """
        The representation for a mortgage payment.
        returns:
            The mortgage as a string.
        """
        return (f"{self._loan_amount:,.2f},{self._rate.value},{self._amortization},{self._frequency.value}")
    


    


