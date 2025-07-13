import streamlit as st

st.set_page_config(page_title="Box Office Lifetime Predictor", page_icon="🎬")

st.title("🎬 Box Office Lifetime Predictor")

st.write("Predict a movie's **lifetime box office** in ₹ million based on opening weekend and word of mouth (WOM).")

# 📥 User Input: Opening Weekend
opening_weekend_million = st.number_input(
    "Enter Opening Weekend Collection (in ₹ **million**)",
    min_value=0.0, step=10.0
)

# 📥 User Input: WOM Level
wom_level = st.selectbox("Select Word of Mouth (WOM) Level", [
    "Exceptional", "Very Good", "Good", "Average", "Poor", "Disaster"
])

# 🧠 Map WOM to legs range
legs_ranges = {
    "Exceptional": (4.0, 5.0),
    "Very Good": (3.0, 3.9),
    "Good": (2.5, 2.9),
    "Average": (2.0, 2.4),
    "Poor": (1.5, 1.9),
    "Disaster": (1.1, 1.4)
}

low_legs, high_legs = legs_ranges[wom_level]

# ✅ Calculate and show prediction
if opening_weekend_million > 0:
    lowball = opening_weekend_million * low_legs
    highball = opening_weekend_million * high_legs

    st.success(f"📉 Lowball Lifetime Prediction: ₹{lowball:,.2f} million")
    st.success(f"📈 Highball Lifetime Prediction: ₹{highball:,.2f} million")

    st.caption(f"(Using legs range: {low_legs} – {high_legs} for **{wom_level}** WOM)")
else:
    st.info("Please enter the opening weekend collection to get prediction.")

# ℹ️ Explanation section
with st.expander("ℹ️ What is 'legs' and WOM?"):
    st.write("""
    **Legs** = How much more a movie earns after its opening weekend.  
    Formula: `Lifetime Gross = Opening Weekend × Legs`

    **Word of Mouth (WOM)** = How much audience liked it:
    - Better WOM → Higher legs
    - Poor WOM → Movie drops fast

    Example:  
    Opening ₹500 million × Legs 3.2 = Lifetime ₹1600 million
    """)

st.markdown("---")
st.caption("Made for Box office lovers ")
