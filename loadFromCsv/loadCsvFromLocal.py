# Import the `pandas` library as `pd`
import pandas as pd

# Load in the data from local with `read_csv()`
digits = pd.read_csv("optdigits.tra", header=None)

# Print out `digits`
print(digits)