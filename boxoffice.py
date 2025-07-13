import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Box Office Lifetime Predictor", page_icon="🎬")

st.title(" Box Office Lifetime Predictor")
st.write("Predict a movie's **lifetime box office** in ₹ million based on opening weekend and word of mouth (WOM).")

# 📥 Input: Opening Weekend
opening_weekend_million = st.number_input(
    "Enter Opening Weekend Collection (in ₹ **million**)",
    min_value=0.0, step=10.0
)

# 📥 Input: WOM Level
wom_level = st.selectbox("Select Word of Mouth (WOM) Level", [
    "Exceptional", "Very Good", "Good", "Average", "Poor", "Disaster"
])

# 🧠 Map WOM → Legs
legs_ranges = {
    "Exceptional": (4.0, 5.0),
    "Very Good": (3.0, 3.9),
    "Good": (2.5, 2.9),
    "Average": (2.0, 2.4),
    "Poor": (1.5, 1.9),
    "Disaster": (1.1, 1.4)
}
low_legs, high_legs = legs_ranges[wom_level]

# ✅ Predict lifetime
if opening_weekend_million > 0:
    lowball = opening_weekend_million * low_legs
    highball = opening_weekend_million * high_legs

    st.success(f"📉 Lowball Lifetime Prediction: ₹{lowball:,.2f} million")
    st.success(f"📈 Highball Lifetime Prediction: ₹{highball:,.2f} million")
    st.caption(f"(Using legs range: {low_legs} – {high_legs} for **{wom_level}** WOM)")

    # 📊 Weekly breakdown
    weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6"]
    week_split = [0.35, 0.25, 0.15, 0.10, 0.08, 0.07]  # % split of lifetime

    low_weekly = [round(lowball * pct, 2) for pct in week_split]
    high_weekly = [round(highball * pct, 2) for pct in week_split]

    df_chart = pd.DataFrame({
        "Week": weeks,
        "Lowball (₹M)": low_weekly,
        "Highball (₹M)": high_weekly
    })

    st.subheader("📊 Projected Weekly Box Office Collection")
    st.line_chart(df_chart.set_index("Week"))

else:
    st.info("Please enter the opening weekend collection to get prediction.")

# ℹ️ Help
with st.expander("ℹ️ What is 'legs' and WOM?"):
    st.write("""
    **Legs** = How much more a movie earns after its opening weekend.  
    Formula: `Lifetime Gross = Opening Weekend × Legs`

    **Word of Mouth (WOM)** = How much the audience liked the movie:
    - Exceptional WOM = Huge legs
    - Poor WOM = Movie crashes early

    Example:  
    ₹100M opening × 3.5 legs = ₹350M lifetime
    """)

st.markdown("---")
st.caption("Made for Movie Buffs ")