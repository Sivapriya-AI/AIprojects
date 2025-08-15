import pandas as pd 

#import streamlit as st
print("CSV ANALYSER")

csv_file = 'data.csv'
#st.title("📊 CSV Analyser")

# Upload CSV file
#uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])


df = pd.read_csv(csv_file)

if(df.empty):
    print("CSV is empty")
else:
    print("____________________PREVIEW___________________\n")
    print("HEAD--------------\n",df.head(5))
    print("DESCRIBE--------------\n",df.describe())
    print("SHAPE--------------\n",df.shape)
    #print("INFO--------------\n",df.info) 

def check_nullandduplicates(df):
    print("____________FINDING ANANOMALY________________")
    print("\nNull values in given CSV:")
    nullvalue_count = df.isnull().sum()
    print(nullvalue_count)
    duplicated_values = df[df.duplicated]

    if (duplicated_values.empty):
        print("No duplicate values")
    else:
        print("Duplicate values ")
        print(duplicated_values)


check_nullandduplicates(df)

def clear_ananomaly(df):
    print("____________CLEARING ANANOMALY________________")
    print("handling nulls")
    for col in df.columns:
        if df["Date"].isnull().any():  # only process if NaNs exist
            # Try parsing as datetime (if it works for most values, treat as date)
            temp = pd.to_datetime(df["Date"], errors='coerce')
            temp.notna().sum() / len(temp) > 0.8
            # at least 80% valid dates
            df["Date"] = temp.fillna(pd.Timestamp("1900-01-01"))
        else:
            # Fill based on original type
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col] = df[col].fillna(0)
            else:
                df[col] = df[col].fillna("0")
    print("Hanlding Duplicates")
    # Remove duplicates based on all columns
    df =df.drop_duplicates()
    return df
    
new_df=clear_ananomaly(df)
check_nullandduplicates(new_df)
#print(df.info)

new_df.to_csv("data_cleaned.csv", index=False)
print("\n✅ Cleaned CSV saved as 'data_cleaned.csv'")