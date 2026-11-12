import csv
from collections import defaultdict

print("\n" + "=" * 65)
print("           PRODUCT OPPORTUNITY INTELLIGENCE ENGINE")
print("=" * 65)

# Load customer feedback
with open("customer_feedback.csv", "r", encoding="utf-8") as file:
    reviews = list(csv.DictReader(file))

# Product problem categories
categories = {
    "Performance": ["slow", "crashes", "loading", "errors"],
    "User Experience": ["confusing", "navigation", "find", "steps"],
    "Customer Support": ["support", "respond", "resolved"],
    "Pricing": ["expensive", "pricing", "price"],
    "Product Features": ["feature", "dashboard", "analytics", "track"]
}

# Product recommendations
recommendations = {
    "Performance": {
        "action": "Improve application speed and system stability.",
        "business_value": "Reduce customer frustration and improve retention.",
        "kpi": "Application crash rate and page load time"
    },
    "User Experience": {
        "action": "Simplify navigation and improve checkout usability.",
        "business_value": "Improve customer experience and conversion.",
        "kpi": "Task completion rate and checkout conversion"
    },
    "Customer Support": {
        "action": "Improve support response time and issue resolution.",
        "business_value": "Increase customer satisfaction.",
        "kpi": "First response time and customer satisfaction"
    },
    "Pricing": {
        "action": "Review pricing plans and communicate feature value.",
        "business_value": "Improve perceived value and reduce cancellations.",
        "kpi": "Customer retention and plan conversion"
    },
    "Product Features": {
        "action": "Improve dashboard insights and introduce useful features.",
        "business_value": "Increase product adoption and engagement.",
        "kpi": "Feature adoption and active users"
    }
}

# Find matching customer problems
evidence = defaultdict(list)

for review in reviews:
    text = review["feedback"].lower()

    for category, keywords in categories.items():
        if any(word in text for word in keywords):
            evidence[category].append(review["feedback"])

# Generate ranked opportunities
opportunities = sorted(
    evidence.items(),
    key=lambda item: len(item[1]),
    reverse=True
)

print("\nTOP PRODUCT OPPORTUNITIES")
print("-" * 65)

report = [
    "# AI Product Intelligence – Opportunity Report",
    "",
    f"Customer reviews analysed: {len(reviews)}",
    "",
    "## Product opportunities"
]

for rank, (category, feedback) in enumerate(opportunities, start=1):
    suggestion = recommendations[category]

    section = [
        f"\n{rank}. {category}",
        f"Customer mentions: {len(feedback)}",
        f"Recommended action: {suggestion['action']}",
        f"Business value: {suggestion['business_value']}",
        f"Suggested KPI: {suggestion['kpi']}",
        "Customer evidence:"
    ]

    print("\n" + "\n".join(section))

    report.extend(["", f"## {rank}. {category}"])
    report.extend(section[1:])

    for item in feedback:
        print(f"  - {item}")
        report.append(f"- {item}")

# Save the report automatically
with open("product_opportunity_report.md", "w", encoding="utf-8") as file:
    file.write("\n".join(report))

print("\n" + "=" * 65)
print("PRODUCT OPPORTUNITY ANALYSIS COMPLETED")
print("Report saved: product_opportunity_report.md")
print("=" * 65)
