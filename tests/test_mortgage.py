"""
Description: A class used to test the Mortgage class.
Author: Benjamin Omoregie
Date: 11/11/2023
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""
from unittest import TestCase
import unittest
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, MortgageFrequency, VALID_AMORTIZATION 

class MortageTests(unittest.TestCase):
    def test_init_invalid_loan_amount(self):
        #Test that a ValueError is raised when an invalid loan amount is provided.
        #Arrange
        loan_amount = -100
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 25
        expected = "Loan amount must be positive."
        #Act and Assert
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, rate, frequency, amortization)
        self.assertEqual(expected, str(context.exception))
    
    def test_init_invalid_rate(self):
        #Test that a ValueError is raised when an invalid rate is provided.
        #Arrange
        loan_amount = 100
        rate = "INVALID"
        frequency = MortgageFrequency.MONTHLY
        amortization = 25
        expected = "Rate provided is invalid."
        #Act and Assert
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, rate, frequency, amortization)
        self.assertEqual(expected, str(context.exception))
    
    def test_init_invalid_frequency(self):
        #Test that a ValueError is raised when an invalid frequency is provided.
        #Arrange
        loan_amount = 100
        rate = MortgageRate.FIXED_5
        frequency = "INVALID"
        amortization = 25
        expected = "Frequency provided is invalid."
        #Act and Assert
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, rate, frequency, amortization)
        self.assertEqual(expected, str(context.exception))
    
    def test_init_invalid_amortization(self):
        #Test that a ValueError is raised when an invalid amortization is provided.
        #Arrange
        loan_amount = 100
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 10000
        expected = "Amortization provided is invalid."
        #Act and Assert
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, rate, frequency, amortization)
        self.assertEqual(expected, str(context.exception))

    def test_negative_loan_amount_mutator(self):
        #Test that a ValueError is raised when a negative loan amount is provided.
        #Arrange
        loan_amount = 100
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 25
        expected = "Loan amount must be positive."
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        #Act and Assert
        with self.assertRaises(ValueError) as context:
            mortgage.loan_amount = -100
        self.assertEqual(expected, str(context.exception))
    
    def test_zero_loan_amount_mutator(self):
        #Test that a ValueError is raised when a Zero loan amount is provided.
        #Arrange
        loan_amount = 100
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 25
        expected = "Loan amount must be positive."
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        #Act and Assert
        with self.assertRaises(ValueError) as context:
            mortgage.loan_amount = 0
        self.assertEqual(expected, str(context.exception))
    
    def test_positive_loan_amount_mutator(self):
        #Test that a positive loan amount is provided.
        #Arrange
        loan_amount = 100
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 25
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        expected =  mortgage.loan_amount
        #Act and Assert
        self.assertEqual(loan_amount, expected)
    
    def test_valid_rate_mutator(self):
        #Test that a valid rate is provided.
        #Arrange
        loan_amount = 100
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 25
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        expected =  mortgage.rate
        #Act and Assert
        self.assertEqual(rate, expected)

    def test_invalid_rate_mutator(self):
        #Test for an invalid rate provided.
        #Arrange
        loan_amount = 100
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 25
        expected = "Rate provided is invalid."
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        #Act and Assert
        with self.assertRaises(ValueError) as context:
            mortgage.rate = "INVALID"
        self.assertEqual(expected, str(context.exception))
    
    def test_valid_frequency_mutator(self):
        #Test that a valid frequency is provided.
        #Arrange
        loan_amount = 100
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 25
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        expected =  mortgage.frequency
        #Act and Assert
        self.assertEqual(frequency, expected)
    
    def test_invalid_frequency_mutator(self):
        #Test for an invalid frequency provided.
        #Arrange
        loan_amount = 100
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 25
        expected = "Frequency provided is invalid."
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        #Act and Assert
        with self.assertRaises(ValueError) as context:
            mortgage.frequency = "INVALID"
        self.assertEqual(expected, str(context.exception))
    
    def test_valid_amortization_mutator(self):
        #Test that a valid amortization is provided.
        #Arrange
        loan_amount = 100
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 25
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        expected =  mortgage.amortization
        #Act and Assert
        self.assertEqual(amortization, expected)
    
    def test__init__valid(self):
        #Test that a valid loan_amount, rate, frequency and amortization is provided.
        #Arrange
        loan_amount = 100
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 25
        #Act
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        #Assert
        self.assertEqual(loan_amount, mortgage.loan_amount)
        self.assertEqual(rate, mortgage.rate)
        self.assertEqual(frequency, mortgage.frequency)
        self.assertEqual(amortization, mortgage.amortization)
    
    def test_calculated_monthly_payment(self):
        #Test that a valid monthly payment is calculated.
        #Arrange
        loan_amount = 682912.43
        rate = MortgageRate.FIXED_1
        frequency = MortgageFrequency.MONTHLY
        amortization = 30
        expected_payment = 4046.23
        #Act
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        actual = mortgage.calculate_payment()
        #Assert
        self.assertAlmostEqual(expected_payment, actual, places =2)
    
    def test__str__mortage_monthly(self):
        #Test that a valid string is returned for monthly mortgage is returned.
        #Arrange
        loan_amount = 682912.43
        rate = MortgageRate.FIXED_1
        frequency = MortgageFrequency.MONTHLY
        amortization = 30
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        expected = (f"Mortage Amount: ${loan_amount:,.2f}"
                + "\nRate: 5.89%"
                + "\nAmortization: 30"
                + f"\nFrequency: MONTHLY -- Calculated Payment: ${mortgage.calculate_payment():,.2f}")
        #Act
        actual = str(mortgage)
        #Assert
        self.assertEqual(expected, actual)
    
    def test__str__mortage_bi_weekly(self):
        #Test that a valid string is returned for bi-weekly mortgage is returned.
        #Arrange
        loan_amount = 682912.43
        rate = MortgageRate.FIXED_1
        frequency = MortgageFrequency.BI_WEEKLY
        amortization = 30
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        expected = (f"Mortage Amount: ${loan_amount:,.2f}"
                + "\nRate: 5.89%"
                + "\nAmortization: 30"
                + f"\nFrequency: BI_WEEKLY -- Calculated Payment: ${mortgage.calculate_payment():,.2f}")
        #Act
        actual = str(mortgage)
        #Assert
        self.assertEqual(expected, actual)
    
    def test__str__mortgage_weekly(self):
        #Test that a valid string is returned  for weekly mortgage is returned.
        #Arrange
        loan_amount = 682912.43
        rate = MortgageRate.FIXED_1
        frequency = MortgageFrequency.WEEKLY
        amortization = 30
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        expected = (f"Mortage Amount: ${loan_amount:,.2f}"
                + "\nRate: 5.89%"
                + "\nAmortization: 30"
                + f"\nFrequency: WEEKLY -- Calculated Payment: ${mortgage.calculate_payment():,.2f}")
        #Act
        actual = str(mortgage)
        #Assert
        self.assertEqual(expected, actual)
    
    def test__repr__mortgage(self):
        #Test that a valid representation is returned for a mortgage.
        #Arrange
        loan_amount = 682912.43
        rate = MortgageRate.FIXED_1
        frequency = MortgageFrequency.MONTHLY
        amortization = 30
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        expected = f"{loan_amount:,.2f},{rate.value},{amortization},{frequency.value}"
        #Act
        actual = repr(mortgage)
        #Assert
        self.assertEqual(expected, actual)
    


