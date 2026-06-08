# 📽️ Decoding 3 Idiots — What 1,113 Viewers Really Said

*A descriptive statistical analysis of real IMDb audience reviews,*
*built from scratch — from web scraping to visual storytelling.*

---

## 🔍 The Story Behind This Project

Numbers don't lie — but they do need someone to explain them.

This project started with a simple question: *Does the audience love 3 Idiots
as much as everyone claims?* To answer that scientifically, I scraped 1,113
real IMDb reviews using a custom Python script, cleaned the data, ran
descriptive statistics on every rating, and visualized the results in multiple
ways — all inside a single Jupyter notebook.

The answer? The data speaks loudly.

---

## ⚙️ How the Data Was Collected

Most projects use pre-made datasets. This one didn't.

A custom scraper (`parsing.py`) was written using **Playwright** and
**BeautifulSoup** to dynamically scroll through IMDb's review pages,
load all reviews, and extract ratings, usernames, and review text in real time.

```
IMDb Review Page
        ↓
Playwright (headless Chrome, stealth mode)
        ↓
Dynamic scroll → Load more → Grab full HTML
        ↓
BeautifulSoup → Parse all review cards
        ↓
3idiots_reviews.csv (1,113 clean rows)
```
**Libraries used for scraping:**
`playwright` · `playwright-stealth` · `beautifulsoup4` · `pandas`

---

## 📊 Statistical Results at a Glance

| Metric | Result | Plain English Meaning |
|--------|--------|-----------------------|
| Mean | **8.52 / 10** | The average viewer rated it exceptionally high |
| Median | **9.0** | Half the audience gave 9 or above |
| Mode | **10.0** | Perfect score — the most common single rating |
| Range | **9** (1 to 10) | Some critics exist, but they are a minority |
| Standard Deviation | **2.15** | Viewers largely agreed — not a controversial film |
| Skewness | **−1.853** | Ratings crowd the top of the scale |
| Positive Reviews | **85.0%** (946 / 1,113) | 9 in every 10 viewers left satisfied |
| Top Rating Interval | **9–10** — 751 reviews (67.5%) | Two-thirds gave near-perfect scores |

---

## 🧩 A Finding Nobody Expected

Reviewers who gave **moderate ratings (5–7)** wrote the **longest reviews**
(avg. 864 characters) — longer than both extreme fans and critics.

When viewers are torn, they explain themselves more.
When they love or hate something, certainty makes them brief.

This behavioral insight emerged from the review-length analysis and
was one of the most interesting patterns in the entire dataset.

---
## 🎯 Project Presentation

The full analysis was compiled into a professional presentation
covering four analytical modules:

| Module | Coverage |
|--------|----------|
| 01. Scope & Data Prep | Case study parameters, scraping pipeline, preprocessing |
| 02. Central Tendency | Mean (8.52), Median (9.0), Mode (10.0) |
| 03. Dispersion & Curves | Range (9), Std. deviation (2.15), Skewness (−1.853) |
| 04. Behavioral Dynamics | Sentiment breakdown, review length insight |

> 📄 **[View Full Presentation (PDF)](./3idiots_statistical_analysis_presentation.pdf)**

---
## 📁 What's Inside This Repo
```
├── parsing.py                          → IMDb scraper (Playwright + BS4)
├── 3idiots_audience_analysis.ipynb     → Full statistical analysis notebook
├── 3_idiots_presentation.pdf           → Full project presentation (13 slides)
├── 3idiots_reviews.csv                 → Dataset — 1,113 verified IMDb reviews
├── outputs/
│   ├── rating_distribution_skewness.png
│   ├── rating_density.png
│   ├── interval frequency distribution.png
│   ├── sentiment_distribution.png
│   ├── audience_effort_dynamics.png
│   ├── wordcloud.png
│   └── top20_words.png
└── README.md
```
---

## 🛠️ Full Tech Stack

| Purpose | Tools |
|---------|-------|
| Web Scraping | `playwright`, `playwright-stealth`, `beautifulsoup4` |
| Data Handling | `pandas`, `numpy` |
| Statistics | `scipy` |
| Visualization | `matplotlib`, `seaborn`, `wordcloud` |
| Environment | Jupyter Notebook |

---

## ▶️ Run It Yourself

```bash
# Step 1 — Clone the repo
git clone https://github.com/YOUR-USERNAME/3idiots-audience-analysis

# Step 2 — Install dependencies
pip install pandas numpy matplotlib seaborn scipy wordcloud
pip install playwright beautifulsoup4 playwright-stealth
playwright install chromium

# Step 3 — (Optional) Re-scrape fresh data
python parsing.py

# Step 4 — Open the notebook
jupyter notebook 3idiots_audience_analysis.ipynb
```

> **Note:** `parsing.py` opens a real Chrome browser window for IMDb login.
> Once you log in manually, the session is saved and scraping runs automatically.

---

## 🎓 Project Context

Built as part of a **Statistics and Python** academic project.
The objective was not just to calculate — but to *interpret* every result
in plain language, connecting mathematical output to real human behavior.

> *"Good analysts calculate data.*
> *Great analysts explain data beautifully."*

**Author: Bidisha Garai**
**Date: June 2026**
