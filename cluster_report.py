from opportunity_cluster import cluster_opportunities
import pandas as pd

df = pd.read_csv("customer_feedback.csv")
clusters = cluster_opportunities(df["feedback"].dropna())

summary = clusters.groupby("opportunity").agg(
    feedback_count=("feedback", "count"),
    customer_examples=("feedback", lambda x: " | ".join(x))
).reset_index()

summary = summary.sort_values("feedback_count", ascending=False)

recommendations = {
    "Application Stability": "Investigate crashes, improve error handling and preserve user state.",
    "Customer Support": "Improve response times and customer issue resolution.",
    "User Experience": "Simplify navigation and improve the checkout experience.",
    "Performance": "Optimise loading speed and application responsiveness.",
    "Pricing": "Review subscription pricing and communicate value more clearly.",
    "Other": "Investigate the feedback to identify an improvement opportunity."
}

with open("product_opportunity_summary.md", "w") as file:
    file.write("# Product Opportunity Summary\n\n")
    for _, row in summary.iterrows():
        category = row["opportunity"]
        file.write(f"## {category}\n")
        file.write(f"- Feedback entries: {row['feedback_count']}\n")
        file.write(f"- Recommendation: {recommendations[category]}\n")
        file.write(f"- Customer evidence: {row['customer_examples']}\n\n")

print(summary[["opportunity", "feedback_count"]].to_string(index=False))
print("\nSaved: product_opportunity_summary.md")
