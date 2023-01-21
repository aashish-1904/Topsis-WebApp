import streamlit as st
import pandas as pd
from topsis import topsis

st.set_page_config("MCDM using TOPSIS")
st.title("TOPSIS")

dataset = st.file_uploader("Upload your dataset for MCDM analysis using topsis", type=['csv'], accept_multiple_files=False, help="Click on 'Browse Files' > Choose your '.csv' file > Click 'Upload'")
weights=[]
impacts=[]
if(dataset):
    df = pd.read_csv(dataset)
    rows = len(df.axes[0])
    cols = len(df.axes[1])
    
    if(df.isnull().sum()!=0):
        st.error("There are NULL values in dataset")

    for i in range(1,cols):
        wg = st.slider(f"Weight for {df.columns[i]}", min_value=0.1, max_value=1.0, step=0.1, help="0 for 0% and 1 for 100%", key=i)
        weights.append(wg)
        imp = st.selectbox(f"Impact for {df.columns[i]}", ['+','-'],key=i*9999, help="'+' for maximize and '-' for minimize")
        impacts.append(imp)


if st.button("Submit"): 
    if(dataset):
        topsis(df, impacts, weights)
    # st.dataframe(df)
    # df.style.highlight_max(color = 'lightgreen', axis = 0)
        df['Rank'] = df['Rank'].astype(int)
        st.table(df)
        df.to_csv(r'ans.csv', index=False, header=True)
        with open('ans.csv') as f:
            st.download_button('Download CSV', f, file_name='ans.csv')
    else:
        st.error("You gotta upload a file first")
