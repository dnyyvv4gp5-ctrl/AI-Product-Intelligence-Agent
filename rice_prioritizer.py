features = [
    {
        "name": "Optimise application speed",
        "reach": 800,
        "impact": 3,
        "confidence": 90,
        "effort": 4
    },
    {
        "name": "Improve system stability",
        "reach": 700,
        "impact": 3,
        "confidence": 85,
        "effort": 5
    },
    {
        "name": "Reduce application crashes",
        "reach": 600,
        "impact": 3,
        "confidence": 95,
        "effort": 3
    },
    {
        "name": "Improve customer support experience",
        "reach": 300,
        "impact": 2,
        "confidence": 80,
        "effort": 3
    }
]

for feature in features:
    feature["rice_score"] = (
        feature["reach"]
        * feature["impact"]
        * (feature["confidence"] / 100)
        / feature["effort"]
    )

ranked_features = sorted(
    features,
    key=lambda feature: feature["rice_score"],
    reverse=True
)

report = [
    "# RICE Feature Prioritization Report",
    "",
    "RICE = (Reach × Impact × Confidence) / Effort",
    "",
    "| Rank | Feature | Reach | Impact | Confidence | Effort | RICE Score |",
    "|---|---|---:|---:|---:|---:|---:|"
]

for rank, feature in enumerate(ranked_features, start=1):
    report.append(
        f"| {rank} | {feature['name']} | "
        f"{feature['reach']} | {feature['impact']} | "
        f"{feature['confidence']}% | {feature['effort']} | "
        f"{feature['rice_score']:.2f} |"
    )

report.extend([
    "",
    "## Product Recommendation",
    "",
    f"Prioritise **{ranked_features[0]['name']}** because it has "
    f"the highest RICE score of {ranked_features[0]['rice_score']:.2f}.",
    "",
    "## Important Note",
    "",
    "These are illustrative estimates for this portfolio project, "
    "not measured product data. Real teams should validate these "
    "values using analytics, customer research and engineering estimates."
])

with open("rice_prioritization_report.md", "w", encoding="utf-8") as file:
    file.write("\n".join(report))

print("\n" + "=" * 55)
print("       RICE FEATURE PRIORITIZATION")
print("=" * 55)

for rank, feature in enumerate(ranked_features, start=1):
    print(
        f"{rank}. {feature['name']} "
        f"— Score: {feature['rice_score']:.2f}"
    )

print("\nRecommendation:", ranked_features[0]["name"])
print("\nSaved file: rice_prioritization_report.md")
print("=" * 55)
