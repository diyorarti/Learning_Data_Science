"""
np.where works like if/else confition on many rows at once.
"""

import numpy as np
import pandas as pd

df = pd.DataFrame({
    "score": [80, 45, 90, 30]
})

df["result"] = np.where(
    df["score"] >= 50,
    "Pass",
    "Fail"
)

print(df)