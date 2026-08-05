import streamlit as st
import pandas as pd

# ---------------- Page Config ---------------- #
st.set_page_config(
    page_title="VisionGuard AI",
    page_icon="🛡️",
    layout="wide"
)

# ---------------- Header ---------------- #
st.title("🛡️ VisionGuard AI")
st.caption("Smart AI-Powered Product Quality Inspection System")

st.divider()

st.markdown(
    """
### 🤖 AI Product Inspection Dashboard

This prototype uses an AI model to inspect products and classify them as **PASS** or **FAIL**.
"""
)

# ---------------- Images ---------------- #

left, right = st.columns(2)

with left:
    with st.container(border=True):
        st.subheader("📷 Input Product")
        st.image(
            "prediction.jpg",
            caption="Input Image",
            use_container_width=True
        )

with right:
    with st.container(border=True):
        st.subheader("🤖 AI Prediction")
        st.image(
            "prediction.jpg",
            caption="Prediction Result",
            use_container_width=True
        )

# ---------------- Metrics ---------------- #

st.divider()

st.subheader("📊 Inspection Summary")

c1, c2, c3, c4 = st.columns(4)

c1.metric("📦 Total Inspected", "1")
c2.metric("✅ Passed", "0")
c3.metric("❌ Failed", "1")
c4.metric("🎯 Confidence", "100%")

# ---------------- Inspection Result ---------------- #

st.divider()

st.subheader("🔍 Inspection Result")

col1, col2 = st.columns([2,1])

with col1:

    st.error("❌ PRODUCT FAILED INSPECTION")

    st.write("### Prediction : Defective")

    st.write("### Confidence : **100%**")

    st.write("### Status : **Rejected**")

with col2:

    st.info(
        """
**Product Details**

🧴 Product : Bottle

🆔 Product ID : BTL-001

⏱ Inspection Time : 0.45 sec
"""
    )

# ---------------- History ---------------- #

st.divider()

st.subheader("📑 Inspection History")

history = pd.DataFrame({
    "Product":["Bottle"],
    "Prediction":["Defective"],
    "Result":["FAIL"],
    "Confidence":["100%"]
})

st.dataframe(history, use_container_width=True)

# ---------------- AI Model ---------------- #

st.divider()

st.subheader("🤖 AI Model Information")

col1, col2, col3 = st.columns(3)

col1.success("YOLOv8 Classification")

col2.info("Ultralytics Framework")

col3.warning("Inference Time : 0.45 sec")

# ---------------- Sidebar ---------------- #

st.sidebar.title("🛡️ VisionGuard AI")

st.sidebar.success("System Status : Online")

st.sidebar.markdown("---")

st.sidebar.write("### Demo Information")

st.sidebar.write("✔ AI Product Inspection")

st.sidebar.write("✔ Hackathon Prototype")

st.sidebar.write("✔ Streamlit Dashboard")

st.sidebar.write("✔ YOLOv8 Classification")

# ---------------- Footer ---------------- #

st.divider()

st.caption("© 2026 VisionGuard AI | AI-Powered Product Quality Inspection for MSMEs")