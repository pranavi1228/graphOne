import streamlit as st
import asyncio
import os

from main import main

st.set_page_config(page_title="GraphOne AI Data Pipeline", page_icon="🤖")

st.title("🤖 GraphOne AI Data Pipeline")

st.write("""
This application collects:

- 🚀 AI Startups
- 📦 AI Products
- 📚 AI Research Papers
- 📰 AI News
- 💼 AI Jobs

and exports them as CSV files.
""")

if st.button("Run Pipeline"):
    with st.spinner("Running pipeline..."):
        asyncio.run(main())

    st.success("Pipeline completed!")

    if os.path.exists("exports"):
        st.write("Generated files:")
        for file in os.listdir("exports"):
            st.write(f"✅ {file}")