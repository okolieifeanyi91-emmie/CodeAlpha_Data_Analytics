# CodeAlpha Data Analytics Internship

## Project Overview
This repository contains my work for the CodeAlpha Data Analytics Internship.  
It currently covers:

- **Task 1: Web Scraping**
- **Task 2: Exploratory Data Analysis (EDA)**
- **Task 3: Data Visualization**
- **Task 4: Sentiment Analysis**
I scraped book data from an online bookstore, performed exploratory analysis, and created clear visualizations.

---

## Tools & Technologies Used
- Python
- BeautifulSoup4
- Requests
- Pandas
- Matplotlib
- Seaborn

---

## Task 1: Web Scraping

**Website scraped:** https://books.toscrape.com/

**Data collected:**
- Book Title
- Price
- Rating (1–5)
- Availability

**Files:**
- `scrape_books.py` → Web scraping script
- `books_data_cleaned.csv` → Cleaned dataset (100 books)

---

## Task 2: Exploratory Data Analysis (EDA)

**Key Findings:**
- The dataset contains **100 books**.
- Columns available: Title, Price, Rating, and Availability.
- **Rating Distribution**:
  - Rating 1: 22 books
  - Rating 2: 19 books
  - Rating 3: 22 books
  - Rating 4: 18 books
  - Rating 5: 19 books
- All 100 books are **In Stock**.
- No missing values were found.
- The data is clean and ready for visualization.

---

## Task 3: Data Visualization

I created the following visualizations using Matplotlib and Seaborn:

1. Number of Books by Rating
2. Average Book Price by Rating
3. Distribution of Book Prices
4. Box Plot of Price by Rating

**Files:**
- `visualization.py`
- `chart1_books_by_rating.png`
- `chart2_avg_price_by_rating.png`
- `chart3_price_distribution.png`
- `chart4_price_boxplot.png`
- 
## Task 4: Sentiment Analysis
I performed Sentiment Analysis on book reviews using the **TextBlob** library.

**What I did:**
- Analyzed multiple book reviews
- Calculated polarity scores
- Classified each review as **Positive**, **Negative**, or **Neutral**
- Generated a summary of the sentiment results
---

## How to Run the Project

1. Install the required libraries:

   pip install requests beautifulsoup4 lxml pandas matplotlib seaborn

2. Run the script:

    python scrape_books.py

## Author
Okolie Ifeanyi Emmanuel

CodeAlpha Intern





