from local_ai import analyse_feedback

def analyse_all_feedback(feedback_list):
    results = []

    for number, feedback in enumerate(feedback_list, start=1):
        print(f"Analysing feedback {number}/{len(feedback_list)}...")

        result = analyse_feedback(feedback)
        results.append({
            "feedback": feedback,
            "ai_analysis": result
        })

    return results


if __name__ == "__main__":
    sample_feedback = [
        "The app crashes during payment.",
        "The application takes too long to load.",
        "Customer support takes days to respond.",
        "The checkout process is confusing.",
        "The app crashes whenever I open my profile."
    ]

    results = analyse_all_feedback(sample_feedback)

    for item in results:
        print("\nCUSTOMER FEEDBACK:")
        print(item["feedback"])
        print("\nAI ANALYSIS:")
        print(item["ai_analysis"])
        print("-" * 50)
