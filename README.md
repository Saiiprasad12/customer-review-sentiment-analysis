#  Bank Customer Sentiment Analysis

This project analyzes 10,000+ customer reviews from various banks to identify sentiment patterns using NLP techniques and visualize insights in Tableau.

---

##  Objective

To extract actionable insights from bank customer feedback using sentiment analysis and present them through a clear, interactive dashboard.

---

##  Dataset

- Source: `bank_reviews.csv`
- Columns: `bank`, `review`, `date`
- Contains anonymized customer feedback from multiple banks

---

##  Tools & Technologies

| Area                        | Tools / Libraries Used                                   |
|----------------------------|-----------------------------------------------------------|
| Programming Language       | Python                                                    |
| Data Manipulation          | Pandas                                                    |
| Natural Language Processing| Hugging Face Transformers (`DistilBERT` model)           |
| Visualization              | Tableau                                                   |
| Output Format              | CSV (`tableau_ready_reviews.csv`)                         |
| Version Control            | Git, GitHub                                               |

---

##  Steps & Workflow

1. **Data Loading & Cleaning**
   - Read CSV file using `pandas`
   - Removed null and duplicate reviews
   - Normalized bank names and parsed dates

2. **Sentiment Analysis using NLP**
   - Used Hugging Face `pipeline()` with the `distilbert-base-uncased-finetuned-sst-2-english` model
   - Limited review length to 512 characters to avoid token limit issues
   - Extracted `label` (Positive/Negative) and `score` for each review

3. **Data Export**
   - Saved the final output as a clean CSV (`tableau_ready_reviews.csv`)

4. **Visualization in Tableau**
   - Designed an interactive dashboard with:
     - Sentiment distribution by bank (stacked bar)
     - Sentiment trends over time (line chart)
     - Heatmaps comparing sentiment intensity

---

##  Sample Visualizations

> [ View Tableau Dashboard](#)  
 https://public.tableau.com/app/profile/sai.prasad2349/vizzes 

---

##  Skills Demonstrated

- Data Cleaning & Preprocessing
- Natural Language Processing (NLP)
- Sentiment Analysis with Transformers
- Data Visualization in Tableau
- End-to-End Project Execution

---

##  Output

Final CSV: `tableau_ready_reviews.csv`  
Use this file directly in Tableau to build your dashboard.

---

##  Author

**Sai Prasad**  
Data Analyst | Python | Tableau | NLP  
Chennai, India  
saiprasadvj12@gmail.com  
[LinkedIn]( https://www.linkedin.com/in/sai-prasad-2056aa182/ ) | [GitHub](#)

