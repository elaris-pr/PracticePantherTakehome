import pandas as pd

# set file path for original csv
csv_filepath = 'Migration_Interview_Data (Python) (1).xlsx'

# load csv into pandas dataframe
df = pd.read_excel(csv_filepath)

# load test
print(str(df.head()), "\n")

# Appending "Contact: " to column headers
df.columns = [f"Contact: {col}" for col in df.columns]

# confirming Success
print(str(df.head()), "\n")

# checking record count
record_num = "Records: \t" + str(df.shape[0])
print(record_num)

# removing duplicate records
df = df.drop_duplicates()

# checking record count post duplicate removal
print("After Removing Duplicates:\t", df.shape[0])

# Applying title casing to first three columns
df.iloc[:,:3] = df.iloc[:,:3].apply(lambda col: col.str.title())
print(df.head(), "\n")

# Changing date formatting
dob_col = "Contact: Date of Birth"
df[dob_col] = pd.to_datetime(df[dob_col], errors= 'coerce') # change to datetime
df[dob_col] = df[dob_col].dt.strftime("%m/%d/%Y") # set format

# check date reformatting
print("Date Refortmat check: \n", df.head())

# Create IDs
id_col = "Contact: ID"
df[id_col] = range(1, len(df) + 1)

# check ID creation
print("ID Creation check: \n", df.tail())

# create a key map for agent Assignment
key_map = {
    "GM" : "Gabe Michel",
    "AA" : "Aaron Artsen",
    "BL" : "Bond Liver",
    "IC" : "Individual Contributor",
    "TM" : "Tim Mint"
    }

# replace Initials with Assigned
assigned_col = "Contact: Assigned"
default_assignment = "Gabe Michel"
df[assigned_col] = df[assigned_col].str.upper().map(key_map) # replace w key matching
df[assigned_col] = df[assigned_col].fillna(default_assignment) # no matches filled with default

# check Assignment
print("Assigned check: \n", df.tail())

# Output the transformed dataframe to CSV
df.to_csv("transformed_test.csv", index=False)
