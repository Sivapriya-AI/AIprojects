import streamlit as st
import pandas as pd

st.title("📊 CSV Analyser")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    # Read CSV into DataFrame
    df = pd.read_csv(uploaded_file)
    
    if df.empty:
        st.error("CSV is empty!")
    else:
        st.subheader("🔍 Data Preview")
        st.dataframe(df.head())

        st.write("**Shape:**", df.shape)
        st.write("**Describe:**")
        st.write(df.describe())

        # Check anomalies
        st.subheader("🚨 Anomaly Detection")
        nullvalue_count = df.isnull().sum()
        #print(nullvalue_count)
        st.write("Null values:", nullvalue_count)
        duplicated_values = df[df.duplicated]
        if (duplicated_values.empty):
            st.write(f"No Duplicate rows")
        else:
            st.write(f"Duplicate rows: {duplicated_values}")
        #print("Duplicate values")
        #print(duplicated_values)
       

        # Option to clean data
        if st.button("🧹 Clean Data"):
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
            # Remove duplicates
            df = df.drop_duplicates()

            st.success("Data cleaned!")
            st.dataframe(df.head())
            st.write("**Shape:**", df.shape)

            # Download cleaned CSV
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="⬇ Download Cleaned CSV",
                data=csv,
                file_name="cleaned_data.csv",
                mime="text/csv"
            )
