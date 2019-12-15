import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mean = 1
std = 0.1
n_reps = 500
n_simulations = 100

# plt.hist(targets, bins=10)
# plt.show()

# Inputs
sales_pct = np.random.normal(mean, std, n_reps).round(2)

sales_expected = [75000, 100000, 200000, 300000, 400000, 500000]
sales_prob = [0.3, 0.3, 0.2, 0.1, 0.05, 0.05]
sales_target = np.random.choice(sales_expected, n_reps, p=sales_prob)
sales_actual = sales_target * sales_pct


def commision_rate_func(
    x): return 0.02 if x <= 0.9 else 0.03 if x <= .99 else 0.04


commission_rate = [commision_rate_func(pct) for pct in sales_pct]
commission_ammount = commission_rate * sales_actual

df = pd.DataFrame(data={
    'sales_expected': sales_target,
    'sales_percentage': sales_pct,
    'sales_actual': sales_actual,
    'commission_rate': commission_rate,
    'commission_amount': commission_ammount
})

print(df.head())
