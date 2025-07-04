import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Decibel Calculator & Visualizer")
st.write("This app helps you understand the relationship between sound intensity and loudness using the formula:")
st.latex("L = 10 \\log_{10}(I / I_0)")

I0 = 1e-12  # Reference intensity

# Mode selection
mode = st.radio("What would you like to enter?", ("Intensity (I)", "Loudness (L)"))

if mode == "Intensity (I)":
    I = st.slider("Select intensity (I) in W/m²", min_value=1e-12, max_value=1.0, value=1e-6, format="%.2e")
    L = 10 * np.log10(I / I0)
    st.write(f"Calculated Loudness: **{L:.2f} dB**")
    
elif mode == "Loudness (L)":
    L = st.slider("Select loudness (L) in dB", min_value=0.0, max_value=150.0, value=60.0)
    I = I0 * 10**(L / 10)
    st.write(f"Calculated Intensity: **{I:.2e} W/m²**")

# Plotting
I_values = np.logspace(-12, 0, 500)
L_values = 10 * np.log10(I_values / I0)

fig, ax = plt.subplots()
ax.plot(I_values, L_values, label="L = 10 log₁₀(I / I₀)")
ax.set_xscale("log")
ax.set_xlabel("Intensity (W/m²)")
ax.set_ylabel("Loudness (dB)")
ax.set_title("Logarithmic Relationship Between Intensity and Loudness")

# Highlight user point
ax.axvline(I, color='red', linestyle='--', label="Selected I")
ax.axhline(L, color='green', linestyle='--', label="Selected L")
ax.legend()

st.pyplot(fig)
