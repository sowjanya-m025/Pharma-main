import streamlit as st
from master_agent import MasterAgent

st.set_page_config(page_title="Agentic Pharma AI", layout="wide")

st.title("💊 Agentic AI Pharma Innovation Tool")

user_query = st.text_area("Enter your molecule or research question:")

if st.button("Run Analysis"):
    if not user_query.strip():
        st.warning("Please enter a molecule or a research question first.")
    else:
        with st.spinner("Running agentic workflow..."):
            master = MasterAgent()
            report_path = master.run(user_query)
            st.success("✅ Report generated successfully!")
            with open(report_path, "rb") as report_file:
                st.download_button(
                    "Download Report", report_file.read(), file_name="Product_Story.pdf"
                )
