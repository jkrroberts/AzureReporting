# testCode.py

x = 'Ramesh Chirumamilla <rchirumamilla@ltcg.com>'
split = x.split('<', 1)
x.split('<', 1)[0]

dfStory['Sprint'].notna
# displays only values that are not null
"""
str.strip() removes leading and trailing whitespace from each value in the 'Sprint' column.
notna() creates a boolean mask that checks whether each stripped value in the 'Sprint' column is not null.
Applying this mask to the DataFrame using df[...] filters out the rows where 'Sprint' is null or consists only of whitespace.
Finally, ['Sprint'] selects only the 'Sprint' column from the filtered DataFrame.
"""
dfStory[dfStory['Sprint'].str.strip().notna()]['Sprint']

dfStory.StoryIterationPath.values[200].split('\\',-1)[1]
dfStory.StoryTeam = dfStory.StoryIterationPath.values.split('\\',-1)[1]
dfStory['StoryIterationPath'].str.extract(r'\\([^\\]+)$')
# below will extract out just the team name from the below example
LTCG\\luma Data Engineering\\Sprint 8
df[['Company', 'Team', 'Sprint']] = df['iteration'].str.split('\\', expand=True)
df['Result'] = df['Column'].str.extract(r'LTCG\\(.*)\\')
dfStory['StoryTeam'] = dfStory['StoryIterationPath'].str.extract(r'LTCG\\(.*)\\')
y = dfStory['StoryIterationPath'].str.extract(r'\\([^\\]+)$')
# Query values from the DataFrame and exclude NaN values
result = dfStory.query('StoryTeam' == 'LTCG').dropna()
# Query values from the DataFrame and exclude NaN values
result = df.query('column_name == column_value').dropna()
z = 'LTCG'
df[['Company', 'Team', 'Sprint']] = df['Iteration Path'].str.split('\\', expand=True)

"""
    for index, row in df.iterrows():
        try:
            split_values = row['Iteration Path'].split('\\')
            row['Company'] = split_values[0]
            row['Team'] = split_values[1]
            row['Sprint'] = split_values[2]
        except Exception as e:
            print(f"Error processing row {index}: {e}")
    # Parse StoryAssignedTo into 2 new columns
"""