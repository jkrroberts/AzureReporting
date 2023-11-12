# getCSVtoDF.py
import pandas as pd
import os

# set data path variables.
output_data_path = os.path.abspath('/output')
input_data_path = os.path.abspath('z:\AzureReporting\\raw data')

# set the path for the raw data Z:\AzureReporting\raw data
def createDF(csvFile, dfName):
        # raw_data_path = os.path.abspath('z:\AzureReporting\\raw data')
        # get_csv = os.path.join(raw_data_path, 'SprintUserStoryWithFeature.csv')
        get_csv = os.path.join(input_data_path, csvFile)
        dfName = pd.read_csv(get_csv, index_col='ID')
        return dfName


def df_csv_out(df, path, file):
    import os
    import datetime
    ts = datetime.datetime.now()
    ts_str = ts.strftime("%Y%m%d%I%M%S%f")
    file_ts = file + ts_str + '.csv'
    print(file_ts)
    write_df_csv_path = os.path.join(path, file_ts)
    # write df to a csv file
    df.to_csv(write_df_csv_path)


def df_rename_columns(retain_columns, objName):
    rename_columns = {}
    for name in retain_columns:
        new_name = objName + name.replace(" ", "")
        rename_columns[name] = new_name
    return rename_columns


def df_parse_data(df):
    # Parse the values concationated is column StoryIterationPath into 3 new columns
    split_values = df['Iteration Path'].str.split('\\', expand=True)
    num_columns = split_values.shape[1]

    if num_columns >= 3:
        df['Company'] = split_values[0]
        df['Team'] = split_values[1]
        df['Sprint'] = split_values[2]
    elif num_columns == 2:
        df['Company'] = split_values[0]
        df['Team'] = split_values[1]
    else:
        df['Company'] = split_values[0]

    df[['Assigned To', 'Email']] = df['Assigned To'].str.split('<', expand=True)
    df['Email'] = df['Email'].str.rstrip('>')
    return df



dfTask = createDF('AzureTask.csv', 'dfTask')
dfTask = df_parse_data(dfTask)
df_col_names = dfTask.columns
rename_columns = df_rename_columns(df_col_names, 'Task')
dfTask = dfTask.rename(columns= rename_columns)

dfProj = createDF('AzureProject.csv', 'dfProj')
dfProj = df_parse_data(dfProj)
df_col_names = dfProj.columns
rename_columns = df_rename_columns(df_col_names, 'Project')
dfProj = dfProj.rename(columns= rename_columns)

dfFeature = createDF('AzureFeature.csv', 'dfFeature')
dfFeature = df_parse_data(dfFeature)
df_col_names = dfFeature.columns
rename_columns = df_rename_columns(df_col_names, 'Feature')
dfFeature = dfFeature.rename(columns= rename_columns)

dfStory = createDF('AzureStory.csv', 'dfStory')
dfStory = df_parse_data(dfStory)
df_col_names = dfStory.columns
rename_columns = df_rename_columns(df_col_names, 'Story')
dfStory = dfStory.rename(columns= rename_columns)
# Add the id of the story as a persisted field
dfStory['StoryID'] = dfStory.index

dfEpic = createDF('AzureEpic.csv', 'dfEpic')
dfEpic = df_parse_data(dfEpic)
df_col_names = dfEpic.columns
rename_columns = df_rename_columns(df_col_names, 'Epic')
dfEpic = dfEpic.rename(columns= rename_columns)

dfInc = createDF('AzureIncident.csv', 'dfInc')
dfInc = df_parse_data(dfInc)
df_col_names = dfInc.columns
rename_columns = df_rename_columns(df_col_names, 'Inc')
dfInc = dfInc.rename(columns= rename_columns)

# Join story and Features df together
df = pd.merge(dfStory, dfFeature, how='left', left_on='StoryParent', right_on='ID')
df = pd.merge(df, dfEpic, how='left', left_on='FeatureParent', right_on='ID')
df = pd.merge(df, dfProj, how='left', left_on='EpicParent', right_on='ID')

# Perform aggregation on the data
df['StoryCompletedPoints'] = \
    df.apply(lambda row: row['StoryStoryPoints'] if row['StoryState'] == 'Closed' else None, axis=1)

# df.drop('CompletedPoints', axis=1, inplace=True)
# dfTask['TaskActivity'].unique() gives a distinct of all values in the column

df_csv_out(df, output_data_path, 'AzureOutput')
df_csv_out(dfStory, output_data_path, 'StoryOutput') # have 594 records and 14 columns
df_csv_out(dfFeature, output_data_path, 'FeatureOutput')
df_csv_out(dfEpic, output_data_path, 'EpicOutput')
df_csv_out(dfInc, output_data_path, 'IncOutput')
df_csv_out(dfTask, output_data_path, 'TaskOutput')

