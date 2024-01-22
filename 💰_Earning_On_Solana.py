import streamlit as st
from streamlit_extras.colored_header import colored_header

st.set_page_config(
    page_title="Earning On Solana",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": "https://twitter.com/tweb3girl",
        "About": None
    }
)

#style metric containers
st.markdown("""
<style>
div[data-testid="metric-container"] {
   background-color: #c8d7db;
   border: 1px solid rgba(28, 131, 225, 0.1);
   padding: 5% 5% 5% 10%;
   border-radius: 5px;
   color: rgb(30, 103, 119);
   overflow-wrap: break-word;
}

/* breakline for metric text         */
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color: #b0020d;
}
</style>
"""
            , unsafe_allow_html=True)

st.markdown(f'<h1 style="color:#434346;font-size:60px;text-align:center;">{"Earning On Solana"}</h1>', unsafe_allow_html=True)
colored_header(
    label="",
    description="",
    color_name="gray-70",
)

text_1 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 20px;">Uniswap has consistently maintained its position as a market leader since the launch of its V1 contract on the Ethereum mainnet in November 2018. In the ever-changing crypto market, staying at the forefront is not guaranteed; sustaining a leading position requires continuous effort, especially with the emergence of new contenders. The focus of this dashboard is to scrutinize Uniswap\'s performance in relation to its competitors, placing particular emphasis on key metrics such as trading volume, total value locked (TVL), and transaction volume.</p>'
st.markdown(text_1, unsafe_allow_html=True)

