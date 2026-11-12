import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="AI Product Intelligence", page_icon="📊", layout="wide")

BASE = Path(__file__).parent
uploaded_file = st.sidebar.file_uploader("Upload customer feedback CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if "feedback" not in df.columns:
        st.error("CSV must contain a feedback column.")
        st.stop()
    st.sidebar.success("CSV uploaded successfully!")
else:
    df = pd.read_csv(BASE / "customer_feedback.csv")
    st.sidebar.info("Showing sample feedback.")

def sentiment(text):
    text = str(text).lower()
    positive = ["love", "excellent", "easy", "great", "good", "helpful"]
    negative = ["slow", "crash", "cannot", "difficult", "problem", "issue", "poor", "bad"]
    pos = sum(w in text for w in positive)
    neg = sum(w in text for w in negative)
    return "Positive" if pos > neg else "Negative" if neg > pos else "Neutral"

def category(text):
    text = str(text).lower()
    if any(w in text for w in ["slow", "crash", "speed", "performance"]):
        return "Performance & Stability"
    if any(w in text for w in ["support", "respond", "help"]):
        return "Customer Support"
    if any(w in text for w in ["payment", "price", "cost"]):
        return "Pricing & Payments"
    if any(w in text for w in ["dashboard", "button", "navigation", "find", "easy"]):
        return "User Experience"
    return "Product Features"

df["Sentiment"] = df["feedback"].apply(sentiment)
df["Category"] = df["feedback"].apply(category)

st.title("AI Product Intelligence Agent")
st.caption("Customer insights | Product opportunities | Feature prioritisation")

st.sidebar.header("Filters")
sentiments = st.sidebar.multiselect("Sentiment", sorted(df["Sentiment"].unique()), default=sorted(df["Sentiment"].unique()))
categories = st.sidebar.multiselect("Category", sorted(df["Category"].unique()), default=sorted(df["Category"].unique()))

data = df[df["Sentiment"].isin(sentiments) & df["Category"].isin(categories)]

st.subheader("Product health overview")
a, b, c, d = st.columns(4)
a.metric("Total feedback", len(data))
b.metric("Positive", (data["Sentiment"] == "Positive").sum())
c.metric("Negative", (data["Sentiment"] == "Negative").sum())
d.metric("Neutral", (data["Sentiment"] == "Neutral").sum())

left, right = st.columns(2)

with left:
    st.subheader("Customer sentiment")
    counts = data["Sentiment"].value_counts().reset_index()
    counts.columns = ["Sentiment", "Count"]
    if not counts.empty:
        st.plotly_chart(px.pie(counts, names="Sentiment", values="Count", hole=0.5), use_container_width=True)

with right:
    st.subheader("Customer pain points")
    counts = data["Category"].value_counts().reset_index()
    counts.columns = ["Category", "Count"]
    if not counts.empty:
        st.plotly_chart(px.bar(counts, x="Category", y="Count"), use_container_width=True)

st.subheader("RICE feature prioritisation")
rice = BASE / "rice_prioritization_report.md"
if rice.exists():
    st.markdown(rice.read_text(encoding="utf-8"))

st.subheader("Customer feedback explorer")
search = st.text_input("Search feedback")
results = data.copy()
if search:
    results = results[results["feedback"].str.contains(search, case=False, na=False)]
st.dataframe(results, use_container_width=True, hide_index=True)


st.divider()
st.header("🤖 AI-powered customer feedback analysis")
st.caption("Powered by Qwen running locally through Ollama.")

from local_ai import analyse_feedback

feedback_options = df["feedback"].dropna().astype(str).tolist()

if feedback_options:
    selected_feedback = st.selectbox(
        "Select customer feedback to analyse",
        feedback_options
    )

    if st.button("Analyse with Local AI"):
        with st.spinner("AI is analysing customer feedback..."):
            ai_result = analyse_feedback(selected_feedback)
        st.markdown("### AI analysis and product recommendations")
        st.write(ai_result)


st.divider()
st.header("Customer Insights")

from customer_insights import classify_insights

insights = classify_insights(df)
counts = insights["insight_type"].value_counts()

col1, col2, col3 = st.columns(3)
col1.metric("Customer Pain Points", int(counts.get("Customer Pain Point", 0)))
col2.metric("Positive Feedback", int(counts.get("Positive Feedback", 0)))
col3.metric("Feature Requests", int(counts.get("Feature Request", 0)))

st.bar_chart(counts)
st.dataframe(insights, use_container_width=True)


st.divider()
st.header("Product Roadmap Generator")

from roadmap_generator import generate_roadmap, save_roadmap

if st.button("Generate Product Roadmap"):
    roadmap = generate_roadmap(df)
    save_roadmap(roadmap)
    st.session_state["roadmap_data"] = roadmap
    st.success("Product roadmap generated!")

if "roadmap_data" in st.session_state:
    roadmap = st.session_state["roadmap_data"]
    st.dataframe(roadmap, use_container_width=True)

    report_path = Path("product_roadmap.md")
    if report_path.exists():
        st.download_button(
            "Download Product Roadmap",
            data=report_path.read_text(),
            file_name="product_roadmap.md",
            mime="text/markdown"
        )


st.divider()
st.header("AI-Powered Product Strategy")
st.write("Use the local Qwen model to analyse your generated product roadmap.")

if st.button("Generate AI Product Strategy"):
    from roadmap_ai import analyse_roadmap

    roadmap_path = Path("product_roadmap.md")

    if roadmap_path.exists():
        with st.spinner("Qwen is analysing your product roadmap..."):
            strategy = analyse_roadmap(roadmap_path.read_text())

        st.subheader("AI Product Strategy Report")
        st.markdown(strategy)
    else:
        st.warning("Please generate your Product Roadmap first.")

st.caption("Portfolio prototype | Sample data | Rule-based analysis, not production AI.")
