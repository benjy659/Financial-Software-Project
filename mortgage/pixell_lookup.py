"""
Description: Enumerations to keep track of valid mortgage rates 
and payment frequencies. A list to keep track of valid amortization periods.
Author: ACE Department
Edited By: Benjamin Omoregie
Date: 11/11/2023
Usage: The enumerations and list in this file may be used when working 
with mortgages to ensure only valid rates, frequencies and amortization 
periods are used.
"""


from enum import Enum

VALID_AMORTIZATION = [5, 10, 15, 20, 25, 30]
class MortgageRate(Enum):
    """
    An Enumeration to keep track of valid mortgage rates.
    values:
        FIXED_5: fixed  mortgage rate  for 5 years.
        FIXED_3: fixed  mortgage rate for 3 years.
        FIXED_1: fixed  mortgage rate for 1 year.
        VARIABLE_5:  variable rate mortgage for 5 years.
        VARIABLE_3:  variable rate mortgage for 3 years.
        VARIABLE_1:  variable rate mortgage for 1 year.
    """
    FIXED_5 = 0.0500
    FIXED_3 = 0.0579
    FIXED_1 = 0.0589
    VARIABLE_5 = 0.0650
    VARIABLE_3 = 0.0660
    VARIABLE_1 = 0.0679

class MortgageFrequency(Enum):
    """
    An Enumeration to keep track of valid mortgage payment frequencies.
    values:
        MONTHLY: for monthly mortgage frequency.
        BI_WEEKLY: for bi-weekly mortgage frequency.
        WEEKLY: for weekly mortgage frequency.
    """
    MONTHLY = 12
    BI_WEEKLY = 26
    WEEKLY = 52

