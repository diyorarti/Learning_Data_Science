"""
Filtering:
    1. Filtering with comparision operations:
        df[culumn_name]  Value:
                        ==   equal to
                        !=   not equal to
                        >    greater than
                        <    less than
                        >=   greater than or equal to
                        <=   less than or equal to

    2. filtering with multiple conditions:
        &   and
        |   or
        ~   not
        df[ (condition 1) & / | / ~ (condition 2) ]

    3. Filtering text data: 
        .str.:
            .str.contains()
            .str.startswith()
            .str.endswith()
            .str.lower()
            .str.upper()
            .str.strip()
            .str.replace()
            .str.split()
            .str.len()

        df[ df[column_name].str.contains(specific_word) ]

    4. .isin(), .between(), .isna()
"""
