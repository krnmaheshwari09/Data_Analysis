import numpy as np
import pandas as pd

# below code is for make our output more readable
pd.options.display.max_columns = 20
pd.options.display.max_rows = 20
pd.options.display.max_colwidth = 80
np.set_printoptions(precision=4, suppress=True)

data = [np.random.standard_normal() for i in range(7)]
print(data)

s = r"this\has\no\special\characters"
print(s)

for i in range(10):
    if i == 5:
        pass
    print(i)