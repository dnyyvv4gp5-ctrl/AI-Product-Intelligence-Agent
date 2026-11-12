import pandas as pd

def cluster_opportunities(feedback_list):
    rules = {
        "Application Stability": ["crash", "crashes", "freeze", "error"],
        "Performance": ["slow", "loading", "lag", "speed"],
        "User Experience": ["confusing", "difficult", "interface", "checkout"],
        "Customer Support": ["support", "service", "response", "ticket"],
        "Pricing": ["price", "expensive", "subscription", "cost"],
        "Navigation & Discoverability": ["search button", "find the search", "difficult to find"],
        "New Feature Requests": ["track my orders", "real time", "feature to track"],
        "Product Analytics": ["more analytics", "analytics"],
        "Positive User Experience": ["excellent", "love the new design", "easy to use", "saves me time"]
    }

    rows = []

    for feedback in feedback_list:
        text = str(feedback).lower()
        matched = [
            category for category, keywords in rules.items()
            if any(keyword in text for keyword in keywords)
        ]

        category = matched[0] if matched else "Other"

        rows.append({
            "feedback": feedback,
            "opportunity": category
        })

    return pd.DataFrame(rows)


if __name__ == "__main__":
    df = pd.read_csv("customer_feedback.csv")
    result = cluster_opportunities(df["feedback"].dropna())

    print("\nPRODUCT OPPORTUNITY CLUSTERS")
    print(result.groupby("opportunity").size().sort_values(ascending=False))
    result.to_csv("opportunity_clusters.csv", index=False)
    print("\nSaved: opportunity_clusters.csv")
