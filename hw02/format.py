import pandas as pd

# Read the submission.csv file
df = pd.read_csv('submission.csv')

# Add a new column 'id' at the front
df.insert(0, 'id', range(0, len(df)))

# Save the new dataframe to submission_format.csv
df.to_csv('submission_format.csv', index=False)