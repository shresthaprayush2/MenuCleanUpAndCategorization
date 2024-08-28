import pandas as pd
import numpy as np

data = pd.read_excel('testing.xlsx')
columnsToRemove = ['Unit','Counter','Created by','Modified by','SN']
data.drop(columns=columnsToRemove,inplace=True)
print(data.columns)


# List of tuples containing keyword and corresponding category
categories = [
    ('pizza', 'Pizza'),
    ('wrap', 'Wrap'),
    ('momo', 'Momo'),
    ('sandwich', 'Sandwich'),
    ('soup', 'Soup'),
    ('pasta', 'Pasta'),
    ('salad', 'Salad'),
    ('noodles', 'Noodles'),
    ('thukpa', 'Thukpa'),
    ('spaghetti', 'Spaghetti'),
    ('topping', 'Topping'),
]

# Convert the 'Name' column to lowercase
data['name_lower'] = data['Name'].str.lower()

# Initialize the 'category' column with a default value
data['category'] = 'z'

# Loop through the categories list and update the 'category' column
for keyword, category in categories:
    data['category'] = np.where(data['name_lower'].str.contains(keyword), category, data['category'])

# Sort by 'Department' and 'Name'
data.sort_values(by=['Department', 'Name'], inplace=True)

# Save to Excel
data.to_excel('FixedMenu.xlsx', index=False)

# Drop the temporary 'name_lower' column if not needed anymore
data.drop(columns=['name_lower'], inplace=True)


