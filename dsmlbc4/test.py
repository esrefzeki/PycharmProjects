# TEST ANYTHING THIS LINE BELOW
# ------------------------------------
import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randint(1, 4, size=(50000, 8)),
                  columns=list('ABCDEFGH'))

df = df.apply(lambda x: x.map({1: "A", 2: "B", 3: "C"}), axis=1)
df = df.astype("category")

for col in df.columns:
    print(df[col].value_counts())

df.head()

# TESTING FOR GITHUB