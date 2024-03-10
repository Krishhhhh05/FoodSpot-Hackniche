import numpy as np # linear algebra
import pandas as pd
import matplotlib.pyplot as plt
from apyori import apriori

transactions = []

with open('groceries.csv') as f:
    next(f) # Skip the first line
    for line in f:
        transaction = [item for item in line.strip().split(',') if item != '']
        transactions.append(transaction)
# Delete elements that originate from the first column - Item(s)
for lists in transactions:
    del lists[0]
transactions[:3]