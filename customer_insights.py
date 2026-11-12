import pandas as pd

def classify_insights(df):
    positive_words = [
        "love", "excellent", "great", "helpful",
        "easy to use", "saves me time"
    ]

    feature_words = [
        "would like", "need a feature", "request",
        "add a feature", "real time", "track my orders"
    ]

    results = []

    for feedback in df["feedback"].dropna():
        text = feedback.lower()

        if any(word in text for word in feature_words):
            insight_type = "Feature Request"
        elif any(word in text for word in positive_words):
            insight_type = "Positive Feedback"
        else:
            insight_type = "Customer Pain Point"

        results.append({
            "feedback": feedback,
            "insight_type": insight_type
        })

    return pd.DataFrame(results)


if __name__ == "__main__":
    df = pd.read_csv("customer_feedback.csv")
    insights = classify_insights(df)

    print("\nCUSTOMER INSIGHTS SUMMARY")
    print(insights["insight_type"].value_counts())

    insights.to_csv("customer_insights_report.csv", index=False)
    print("\nSaved: customer_insights_report.csv")
