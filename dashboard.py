# ==========================================================
# VisionGuard AI - Intelligent Product Quality Inspection
# Professional Streamlit Dashboard
# Part 1
# ==========================================================

import streamlit as st
import pandas as pd
import json
import os
from PIL import Image
import matplotlib.pyplot as plt
from datetime import datetime

# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------
st.set_page_config(
    page_title="VisionGuard AI",
    page_icon="🛡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------------
# CUSTOM CSS
# ----------------------------------------------------------

st.markdown("""
<style>

.main{
    background-color:#F5F7FA;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

h1,h2,h3{
    color:#003366;
}

.metric-card{
    background:white;
    border-radius:15px;
    padding:20px;
    box-shadow:0px 3px 12px rgba(0,0,0,0.15);
    text-align:center;
}

.section-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.12);
    margin-bottom:25px;
}

.footer{
    text-align:center;
    color:gray;
    font-size:14px;
}

.pass-box{
    background:#D4EDDA;
    color:#155724;
    padding:12px;
    border-radius:10px;
    font-weight:bold;
    text-align:center;
}

.fail-box{
    background:#F8D7DA;
    color:#721C24;
    padding:12px;
    border-radius:10px;
    font-weight:bold;
    text-align:center;
}

.wait-box{
    background:#FFF3CD;
    color:#856404;
    padding:12px;
    border-radius:10px;
    font-weight:bold;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# HEADER
# ----------------------------------------------------------

st.title("🛡 VisionGuard AI")

st.markdown("""
### Intelligent Product Quality Inspection System

AI Powered Defect Detection using YOLO • OpenCV • Python
""")

st.divider()

# ----------------------------------------------------------
# LOAD JSON RESULT
# ----------------------------------------------------------

default_result = {
    "image_name":"Waiting...",
    "product":"Waiting...",
    "damage_detected":"Waiting...",
    "result":"Waiting",
    "confidence":0
}

if os.path.exists("result.json"):

    try:

        with open("result.json","r") as f:
            result = json.load(f)

    except:

        result = default_result

else:

    result = default_result

# ----------------------------------------------------------
# LOAD CSV HISTORY
# ----------------------------------------------------------

if os.path.exists("inspection.csv"):

    try:

        df = pd.read_csv("inspection.csv")

    except:

        df = pd.DataFrame(
            columns=[
                "Product",
                "Result",
                "Confidence"
            ]
        )

else:

    df = pd.DataFrame(
        columns=[
            "Product",
            "Result",
            "Confidence"
        ]
    )

# ----------------------------------------------------------
# CALCULATE METRICS
# ----------------------------------------------------------

total = len(df)

passed = len(df[df["Result"]=="PASS"]) if total>0 else 0

failed = len(df[df["Result"]=="FAIL"]) if total>0 else 0

accuracy = 0

if total>0:
    accuracy = round((passed/total)*100,2)

# ----------------------------------------------------------
# SIDEBAR
# ----------------------------------------------------------

with st.sidebar:

    st.image(
        "https://img.icons8.com/fluency/96/artificial-intelligence.png",
        width=90
    )

    st.header("Dashboard")

    st.write("### Current Time")

    st.info(datetime.now().strftime("%d %B %Y\n\n%I:%M:%S %p"))

    st.divider()

    st.write("### Project")

    st.success("VisionGuard AI")

    st.write("Developed for MSME Idea Hackathon")

    st.divider()

    st.write("### Files Status")

    st.write("✅ result.json" if os.path.exists("result.json") else "❌ result.json")

    st.write("✅ inspection.csv" if os.path.exists("inspection.csv") else "❌ inspection.csv")

    st.write("✅ result.jpg" if os.path.exists("result.jpg") else "❌ result.jpg")

    st.divider()

    st.caption("Version 1.0")


# ----------------------------------------------------------
# ADD LATEST RESULT TO HISTORY
# ----------------------------------------------------------

if result.get("result") in ["PASS", "FAIL"]:

    new_row = {
        "Product": result.get("product", "Unknown"),
        "Result": result.get("result"),
        "Confidence": result.get("confidence", 0)
    }

    # Prevent duplicate entries
    if df.empty or not (
        (df["Product"] == new_row["Product"]) &
        (df["Result"] == new_row["Result"]) &
        (df["Confidence"] == new_row["Confidence"])
    ).any():

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

        df.to_csv("inspection.csv", index=False)

# ==========================================================
# KPI CARDS
# ==========================================================

st.subheader("📊 Dashboard Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="📦 Total Inspections",
        value=total
    )

with col2:
    st.metric(
        label="✅ Passed",
        value=passed
    )

with col3:
    st.metric(
        label="❌ Failed",
        value=failed
    )

with col4:
    st.metric(
        label="🎯 Accuracy",
        value=f"{accuracy}%"
    )

st.divider()

# ==========================================================
# LATEST INSPECTION
# ==========================================================

st.subheader("🔍 Latest Inspection")

left, right = st.columns([1,1.2])

# ==========================================================
# IMAGE PANEL
# ==========================================================

with left:

    st.markdown("### 📷 Product Image")

    if os.path.exists("result.jpg"):

        try:

            image = Image.open("result.jpg")

            st.image(
                image,
                caption="Detected Product",
                use_container_width=True
            )

        except Exception:

            st.error("Unable to open result.jpg")

    else:

        st.info("No inspection image found.")

# ==========================================================
# DETAILS PANEL
# ==========================================================

with right:

    st.markdown("### 📋 Inspection Details")

    st.write("")

    st.markdown(
        f"""
**📷 Image Name**

{result.get('image_name','Waiting...')}
"""
    )

    st.markdown(
        f"""
**📦 Product**

{result.get('product','Waiting...')}
"""
    )

    st.markdown(
        f"""
**🔍 Defect**

{result.get('damage_detected','Waiting...')}
"""
    )

    st.markdown(
        f"""
**🎯 Confidence**

{result.get('confidence',0)}%
"""
    )

    confidence = result.get("confidence",0)

    st.progress(
        min(confidence/100,1.0)
    )

    st.write("")

# ==========================================================
# STATUS BOX
# ==========================================================

    status = str(result.get("result","Waiting")).upper()

    if status == "PASS":

        st.markdown(
            """
<div class="pass-box">
✅ PRODUCT PASSED INSPECTION
</div>
""",
            unsafe_allow_html=True
        )

    elif status == "FAIL":

        st.markdown(
            """
<div class="fail-box">
❌ PRODUCT FAILED INSPECTION
</div>
""",
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
<div class="wait-box">
⌛ WAITING FOR INSPECTION
</div>
""",
            unsafe_allow_html=True
        )

st.divider()

# ==========================================================
# QUICK SUMMARY
# ==========================================================

st.subheader("📝 Inspection Summary")

summary1, summary2 = st.columns(2)

with summary1:

    st.info(
        f"""
**Latest Product**

{result.get('product','Waiting...')}
"""
    )

with summary2:

    st.info(
        f"""
**Detection Confidence**

{result.get('confidence',0)}%
"""
    )

st.divider()

# ==========================================================
# INSPECTION HISTORY
# ==========================================================

st.subheader("📋 Inspection History")

if not df.empty:

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.download_button(
        label="📥 Download Inspection History",
        data=df.to_csv(index=False),
        file_name="inspection_history.csv",
        mime="text/csv"
    )

else:

    st.info("No inspection history available.")

st.divider()

# ==========================================================
# CHARTS
# ==========================================================

chart1, chart2 = st.columns(2)

# ----------------------------------------------------------
# PASS / FAIL PIE CHART
# ----------------------------------------------------------

with chart1:

    st.subheader("📈 Pass vs Fail")

    if total > 0:

        labels = ["PASS", "FAIL"]
        values = [passed, failed]

        fig, ax = plt.subplots(figsize=(5,5))

        colors = ["#2ECC71", "#E74C3C"]

        ax.pie(
            values,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90,
            colors=colors,
            wedgeprops={"edgecolor":"white"}
        )

        ax.axis("equal")

        st.pyplot(fig)

    else:

        st.info("No data available.")

# ----------------------------------------------------------
# CONFIDENCE CHART
# ----------------------------------------------------------

with chart2:

    st.subheader("📉 Confidence Trend")

    if not df.empty and "Confidence" in df.columns:

        fig2, ax2 = plt.subplots(figsize=(7,4))

        ax2.plot(
            df.index + 1,
            df["Confidence"],
            marker="o",
            linewidth=2
        )

        ax2.set_xlabel("Inspection")

        ax2.set_ylabel("Confidence (%)")

        ax2.set_ylim(0,100)

        ax2.grid(True)

        st.pyplot(fig2)

    else:

        st.info("No confidence data available.")

st.divider()

# ==========================================================
# RECENT INSPECTIONS
# ==========================================================

st.subheader("🕒 Recent Inspections")

if not df.empty:

    recent = df.tail(5)

    st.table(recent)

else:

    st.info("No recent inspections.")

st.divider()

# ==========================================================
# SYSTEM STATUS
# ==========================================================

st.subheader("⚙ System Status")

status1, status2, status3 = st.columns(3)

with status1:

    if os.path.exists("result.json"):

        st.success("JSON Connected")

    else:

        st.error("JSON Missing")

with status2:

    if os.path.exists("inspection.csv"):

        st.success("CSV Connected")

    else:

        st.error("CSV Missing")

with status3:

    if os.path.exists("result.jpg"):

        st.success("Image Loaded")

    else:

        st.warning("Waiting for Image")

st.divider()

# ==========================================================
# PROJECT INFORMATION
# ==========================================================

with st.expander("ℹ About VisionGuard AI"):

    st.markdown("""

### VisionGuard AI

An AI-powered product quality inspection system developed for the **MSME Idea Hackathon**.

### Features

- YOLO-based defect detection
- Automatic PASS / FAIL prediction
- Real-time inspection dashboard
- Confidence analysis
- Inspection history
- Performance visualization

### Technology Stack

- Python
- Streamlit
- YOLO
- OpenCV
- Pandas
- Matplotlib

""")

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.markdown(
"""
<div class='footer'>

© 2026 VisionGuard AI

Intelligent Product Quality Inspection System

Built with ❤️ using Python • Streamlit • YOLO

</div>
""",
unsafe_allow_html=True
)