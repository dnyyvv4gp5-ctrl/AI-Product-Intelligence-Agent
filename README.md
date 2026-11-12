# AI Product Intelligence Agent

### Turning Customer Feedback into Actionable Product Decisions with AI

An AI-powered product intelligence dashboard that transforms customer feedback into actionable insights, product opportunities, prioritised improvements, and strategic recommendations.

## Project Overview

Businesses receive large amounts of customer feedback but often struggle to turn it into meaningful product decisions.

This application analyses feedback, identifies customer pain points, discovers product opportunities, prioritises improvements, and generates AI-powered product strategy recommendations.

## Key Features

1. Customer Feedback Analysis
2. Local AI Feedback Analysis using Qwen 2.5
3. Customer Insights and Pain Point Detection
4. Product Opportunity Clustering
5. RICE Prioritisation
6. Automated Product Roadmap Generation
7. AI-Powered Product Strategy

## Technology Stack

- Python
- Streamlit
- Pandas
- Plotly
- Ollama
- Qwen 2.5 (1.5B)
- CSV and Markdown

## Architecture

Customer Feedback (CSV)
    |
    v
Streamlit Dashboard
    |
    v
Feedback Analysis
    |
    +---- Rule-Based Analysis
    |
    +---- Local Qwen AI Analysis
    |
    v
Customer Insights
    |
    v
Product Opportunity Clustering
    |
    v
RICE Prioritisation
    |
    v
Product Roadmap
    |
    v
AI Product Strategy
    |
    v
Actionable Recommendations

## Getting Started

### Prerequisites

- Python 3.14
- Ollama

### Install dependencies

    pip install -r requirements.txt

### Download the local AI model

    ollama pull qwen2.5:1.5b

### Run the application

    streamlit run app.py

Open http://localhost:8501

## Sample Data

The project includes synthetic customer feedback. Users can upload their own CSV file with a column named feedback.

## Business Value

- Understand customer pain points.
- Identify recurring product issues.
- Discover product improvement opportunities.
- Support product prioritisation.
- Generate actionable product roadmaps.
- Support data-informed product decisions.

## Important Notes

This is a portfolio prototype, not a production application.

Rule-based analysis is used for sentiment, clustering and roadmap prioritisation. Local Qwen AI is used for individual feedback analysis and product strategy generation.

No paid AI API or subscription is required. AI recommendations should be reviewed by humans.

## Future Improvements

- Advanced product opportunity scoring.
- Customer feedback trend analysis.
- Configurable RICE scoring.
- Executive report exports.
- Human review workflows.

## Author

AI Product Management | Customer Insights | Business Analysis | Product Strategy
