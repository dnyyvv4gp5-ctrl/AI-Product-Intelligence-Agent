import csv
from collections import Counter

print("\n" + "=" * 60)
print("          CUSTOMER FEEDBACK ANALYSIS ENGINE")
print("=" * 60)

with open("customer_feedback.csv", "r", encoding="utf-8") as file:
    feedback_data = list(csv.DictReader(file))

positive_words = [
    "love", "excellent", "great", "helpful",
    "easy", "quickly", "saves", "resolved"
]

negative_words = [
    "slow", "crashes", "confusing", "frustrating",
    "unhappy", "expensive", "errors", "takes too long"
]

categories = {
    "Performance": ["slow", "crashes", "loading", "errors"],
    "User Experience": ["confusing", "navigation", "find", "steps"],
    "Customer Support": ["support", "respond", "resolved"],
    "Pricing": ["expensive", "pricing", "price"],
    "Product Features": ["feature", "dashboard", "analytics", "track"]
}

sentiments = Counter()
category_counts = Counter()
total = len(feedback_data)

print(f"\nTotal customer reviews analysed: {total}")

print("\n1. SENTIMENT ANALYSIS")
print("-" * 40)

for item in feedback_data:
    review = item["feedback"].lower()

    positive_score = sum(word in review for word in positive_words)
    negative_score = sum(word in review for word in negative_words)

    if positive_score > negative_score:
        sentiment = "Positive"
    elif negative_score > positive_score:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    sentiments[sentiment] += 1

    matched_categories = set()

    for category, keywords in categories.items():
        if any(word in review for word in keywords):
            matched_categories.add(category)

    for category in matched_categories:
        category_counts[category] += 1

    print(f"Review {item['id']}: {sentiment} - {item['feedback']}")

print("\n2. SENTIMENT SUMMARY")
print("-" * 40)

for sentiment, count in sentiments.items():
    percentage = count / total * 100
    print(f"{sentiment}: {count} ({percentage:.1f}%)")

print("\n3. CUSTOMER PAIN POINTS")
print("-" * 40)

for category, count in category_counts.most_common():
    print(f"{category}: {count} mentions")

print("\n4. PRODUCT IMPROVEMENT OPPORTUNITIES")
print("-" * 40)

for category, count in category_counts.most_common(3):
    print(f"Priority opportunity: Improve {category}")

print("\nAnalysis completed successfully!")
print("=" * 60)
