import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Asq4help",
    page_icon="👋",
)

st.write("# Welcome to Asq4help! 👋")

st.sidebar.success("Use the controls to filter.")

st.markdown(
    """
    Ask4help is a platform through which prospective students can reach out to current students and 
    alumni for information. This comes at no cost. **We are working on bringing you more volunteers. 
    If you do not find what you are looking for, please check back. **If you would like to volunteer 
    your time to help prospective students with information, we appreciate you. Please, fill this 
    [form](https://forms.gle/5zE2dq2wfc3QxcNFA)**. 
    
    **👈 Use controls in the sidebar** to see who you may be able to get help from!
    
    ### We ask that
    - You be polite and understanding. These people are volunteers and also have other responsibilities.
    - You do not ask for financial assistance from volunteers. In the same vein, please, do not give money to anyone
    who asks for it. No volunteer on this platform will ask you for money.
"""
)

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQhgNAggMfCTWHfxRB-iJV1Ddcb8318M3uwM9s0bqv-Xsu-xkiuyrseAEKFpQZAvR0vzCd0p-OfZlBT/pub?output=xlsx'

df = pd.read_excel(url, sheet_name=0)

countries = df['School Country'].unique()
country = st.sidebar.selectbox(
    'Select A Country',
    countries
)

states = df[df['School Country'] == country]['School State'].unique()
state = st.sidebar.selectbox(
    'Select State/Province',
    states
)

schools = df[(df['School Country'] == country) & (df['School State'] == state)]['School Name'].unique()
school = st.sidebar.selectbox(
    'Select School',
    schools
)


helpers = df[
    (df['School Country'] == country) & 
    (df['School State'] == state) &
    (df['School Name'] == school)
]

helpers.reset_index(inplace=True)

for i in range(len(helpers)):
    name = helpers.loc[i, 'First Name']
    phone = helpers.loc[i, 'Phone Number']
    email = helpers.loc[i, 'Email']
    twitter = helpers.loc[i, 'Twitter']
    linkedin = helpers.loc[i, 'LinkedIn']


    with st.container():
        col, _ = st.columns(2)
        if pd.isna(name) == False:
            st.text(f'Name: {name}')
        if pd.isna(phone) == False:
            st.text(f'Phone Number: {int(phone)}')
        if pd.isna(email) == False:
            st.text(f'Email Address: {email}')
        if pd.isna(twitter) == False:
            if twitter.startswith('@'):
                st.text(f'Twitter Handle: {twitter}')
            else:
                st.text(f'Twitter Handle: @{twitter}')
        if pd.isna(linkedin) == False:
            st.text(f'LinkedIn Profile: https://www.linkedin.com/in/{linkedin}')

    st.markdown(
        """
            <style>
            [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
                box-shadow: rgb(0 255 255 / 20%) 0px 2px 1px -1px, rgb(0 255 255 / 14%) 0px 1px 1px 0px, rgb(0 255 255 / 12%) 0px 1px 3px 0px;
                border-radius: 15px;
                padding: 5% 5% 5% 10%;
                padding-left: 20px;
                padding-bottom: 10px;
                margin-top: 50px;
            }

            [data-testid="column"] {
                box-shadow: rgb(0 0 0 / 20%) 0px 2px 1px -1px, rgb(0 0 0 / 14%) 0px 1px 1px 0px, rgb(0 0 0 / 12%) 0px 1px 3px 0px;
                border-radius: 15px;
                width: 200px
                padding: 5% 5% 5% 10%;
            }
            </style>
        """,
        unsafe_allow_html = True
    )



    



