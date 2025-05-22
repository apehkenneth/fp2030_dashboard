
import streamlit as st
import pandas as pd
import plotly.express as px





# Load the data
df = pd.read_csv("FP2030_awareness.csv")

# Sidebar filter
states = df['State'].unique()
selected_states = st.sidebar.multiselect("Select State(s):", options=states, default=states)

filtered_df = df[df['State'].isin(selected_states)]

st.title("FP2030 Dashboard")

# 1. Respondents Distribution Across Demographics
st.header("1. Demographics Distribution")

demographic_columns = ['Sex', 'Age']  # Update based on actual columns
for col in demographic_columns:
    if col in filtered_df.columns:
        fig = px.histogram(filtered_df, x=col, title=f"Distribution of {col}")
        st.plotly_chart(fig)

# 2. FP2030 Awareness Levels
st.header("2. FP2030 Awareness Levels")

if 'Awareness_Level' in filtered_df.columns:
    awareness_counts = filtered_df['Awareness_Level'].value_counts(normalize=True) * 100
    fig = px.pie(values=awareness_counts.values, names=awareness_counts.index,
                 title="Awareness of FP2030 (in %)")
    st.plotly_chart(fig)

# 3. Barriers to Implementation Ranked
st.header("3. Barriers to Implementation (Ranked)")

if 'Barriers' in filtered_df.columns:
    # Assuming multiple barriers per respondent separated by commas
    barrier_series = filtered_df['Barriers'].dropna().str.split(',').explode().str.strip()
    barrier_counts = barrier_series.value_counts()
    fig = px.bar(barrier_counts.sort_values(ascending=False),
                 title="Barriers to Implementation (Descending Order)")
    st.plotly_chart(fig)

# 4. Notes
st.markdown("### 4. Use the sidebar to filter results by State.")
