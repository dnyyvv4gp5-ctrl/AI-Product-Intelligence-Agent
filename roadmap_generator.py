import pandas as pd
from opportunity_cluster import cluster_opportunities

RECOMMENDATIONS = {
    "Application Stability": (
        "Improve crash detection, error handling and system reliability.",
        "Reduce application crashes and improve user retention.",
        "Application crash rate, system uptime"
    ),
    "Performance": (
        "Optimise loading speed and application responsiveness.",
        "Reduce waiting time and improve customer satisfaction.",
        "Page load time, response time"
    ),
    "User Experience": (
        "Simplify navigation and improve checkout usability.",
        "Reduce user frustration and improve task completion.",
        "Task completion rate, checkout abandonment"
    ),
    "Navigation & Discoverability": (
        "Make important controls, including search, easier to find.",
        "Help users complete tasks more efficiently.",
        "Search usage, search success rate"
    ),
    "New Feature Requests": (
        "Evaluate and develop the requested product capabilities.",
        "Address unmet customer needs and increase engagement.",
        "Feature adoption, active users"
    ),
    "Product Analytics": (
        "Expand dashboard analytics and reporting capabilities.",
        "Help users make better data-driven decisions.",
        "Analytics feature usage, report engagement"
    ),
    "Customer Support": (
        "Improve support response times and issue resolution.",
        "Improve customer satisfaction and reduce support effort.",
        "First response time, resolution time"
    ),
    "Pricing": (
        "Review pricing and communicate product value more clearly.",
        "Improve perceived value and reduce price-related churn.",
        "Price-related churn, conversion rate"
    )
}

def generate_roadmap(feedback_df):
    clusters = cluster_opportunities(feedback_df["feedback"].dropna())

    summary = (
        clusters.groupby("opportunity")
        .size()
        .sort_values(ascending=False)
    )

    summary = summary[
        summary.index != "Positive User Experience"
    ]

    roadmap = []

    for rank, (category, count) in enumerate(summary.items(), start=1):
        details = RECOMMENDATIONS.get(
            category,
            (
                "Investigate this customer feedback and define an improvement.",
                "Address an identified customer need.",
                "Customer satisfaction, feature usage"
            )
        )

        priority = "High" if rank <= 2 else "Medium" if rank <= 4 else "Low"

        roadmap.append({
            "priority": priority,
            "opportunity": category,
            "feedback_count": int(count),
            "recommendation": details[0],
            "business_impact": details[1],
            "kpis": details[2]
        })

    return pd.DataFrame(roadmap)


def save_roadmap(roadmap):
    with open("product_roadmap.md", "w") as file:
        file.write("# AI Product Intelligence Roadmap\n\n")
        file.write("> Portfolio prototype | Sample customer feedback\n\n")

        for _, item in roadmap.iterrows():
            file.write(f"## {item['priority']} Priority: {item['opportunity']}\n")
            file.write(f"- Customer feedback entries: {item['feedback_count']}\n")
            file.write(f"- Recommended improvement: {item['recommendation']}\n")
            file.write(f"- Business impact: {item['business_impact']}\n")
            file.write(f"- Suggested KPIs: {item['kpis']}\n\n")

    print("Saved: product_roadmap.md")


if __name__ == "__main__":
    df = pd.read_csv("customer_feedback.csv")
    roadmap = generate_roadmap(df)
    print(roadmap.to_string(index=False))
    save_roadmap(roadmap)
