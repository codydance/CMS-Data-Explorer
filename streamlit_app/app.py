import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os

# Database connection
DATABASE_URL = os.getenv("AIRFLOW__DATABASE__SQL_ALCHEMY_CONN")
engine = create_engine(DATABASE_URL)

st.title("CMS DRG Cheapest Locations Explorer")

# Fetch distinct DRGs
drgs = pd.read_sql(
    "SELECT * from distinct_drgs", 
    engine
)

# Dropdown to select DRG
selected_drg = st.selectbox("Select a DRG", drgs['DRG_Desc'])

# Query the 10 cheapest city-state combos for selected DRG
query = """
SELECT
    city,
    state,
    avg_charge
FROM cost_by_city_and_state
WHERE "DRG_Desc" = %(drg)s
ORDER BY avg_charge ASC
LIMIT 10;
"""

df = pd.read_sql(query, engine, params={"drg": selected_drg})

# Show results
st.subheader(f"Cheapest City-State Combinations for: {selected_drg}")
st.dataframe(df)

# Bar chart
#dropping the bar chart for now. Single line comments don't show up in the app
#df_chart = df.copy()
#df_chart["city_state"] = df_chart["city"] + ", " + df_chart["state"]
#st.bar_chart(df_chart.set_index("city_state")["avg_charge"])
