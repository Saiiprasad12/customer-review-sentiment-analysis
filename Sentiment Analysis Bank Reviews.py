# nlp_sentiment_bank_reviews.py

import pandas as pd
from transformers import pipeline

# 1. Load Data
df = pd.read_csv("bank_reviews.csv")  # change path if needed

# 2. Basic Cleaning
df.dropna(subset=['review'], inplace=True)
df.drop_duplicates(subset=['review'], inplace=True)

# Optional: strip and lowercase bank names
df['bank'] = df['bank'].astype(str).str.strip().str.title()
df['review'] = df['review'].astype(str).str.strip()

# Optional: parse date if needed
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# 3. Load Sentiment Analysis Model
print("🔍 Loading sentiment model...")
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

# 4. Truncate Review (model input limit: 512 tokens)
df['review_short'] = df['review'].str[:512]

# 5. Apply Sentiment Model
print("⚙️ Running sentiment analysis...")
df['nlp_sentiment_result'] = df['review_short'].apply(sentiment_pipeline)

# 6. Extract sentiment + score
df['nlp_sentiment'] = df['nlp_sentiment_result'].apply(lambda x: x[0]['label'].capitalize())
df['nlp_score'] = df['nlp_sentiment_result'].apply(lambda x: x[0]['score'])

# 7. Drop temp column but keep all others
df_final = df.drop(columns=['nlp_sentiment_result'], errors='ignore')

# 8. Export Clean CSV
df_final.to_csv("tableau_ready_reviews.csv", index=False)
print("✅ Exported successfully: tableau_ready_reviews.csv")
