"""
SELECTING in Pandas
    1. Column name 
    2. .loc[row_label, column_label] - select by labels/names
    3. .iloc[row_position, column_position] - select by labels/names
               name   age   salary
            a   Ali   22    2000
            b  John   25    3000
            c  Sara   21    2500
            d   Tom   30    4000
        df.loc['a'], df.loc['name']
        df.iloc[1], df.iloc[2]
    4. Selecting rows by condition
    5. Selecting rows by multiple conditions (&, |, ~ )
    6. Selecting columns after filtering rows
    7. Selecting with .isin()
    8. Selecting with .between()
    9. Selecting with .isna() 
    10. .query()
    
    Selecting string values with .str: 
                                        .str.contains()
                                        .str.startswith()
                                        .str.endswith()
                                        .str.lower()
                                        .str.upper()
                                        .str.strip()
                                        .str.replace()
                                        .str.split()
                                        .str.len()

"""

import pandas as pd

data = {
    "Name": ["Ali", "Vali", "Sara", "John"],
    "Age": [20, 25, 22, 30],
    "City": ["Tashkent", "Samarkand", "Warsaw", "London"],
    "Score": [85, 90, 78, 95]
}
df = pd.DataFrame(data)
df = df.set_index('Name')
