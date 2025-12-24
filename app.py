import pandas as pd
from io import BytesIO
import streamlit as st
import STRIDE, USPA, MUFTI, T_BASE
from io import BytesIO


st.title("PT file formattor")

brand = st.selectbox("Select your brand", ["USPA", "MUFTI", "T-BASE", "STRIDE"])
brand_map = {
    "USPA": USPA.format,
    "MUFTI": MUFTI.format,
    "T-BASE": T_BASE.format,
    "STRIDE": STRIDE.format,
}

season = None
if brand in ["T-BASE", "STRIDE"]:
    season = st.text_input("Enter Season", placeholder="AW-25 / SS-25")

file = st.file_uploader("Upload your excel", type=["xls", "xlsx"])
butt = st.button("Click to format")

if butt:
    df = pd.read_excel(file)
    formatted_file, billno = brand_map[brand](df, season=season)
    st.dataframe(formatted_file.head(5))

    output = BytesIO()


    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        formatted_file.to_excel(writer, index=False, sheet_name="Barcode")
    output.seek(0)

    st.download_button(
        label="Download Excel",
        data=output,
        file_name=f"{int(billno)}_{brand}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )