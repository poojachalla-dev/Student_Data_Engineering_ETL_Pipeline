# 🎓 Student Data Engineering Pipeline

> **End-to-end data pipeline project** built on the UCI Machine Learning Repository's *Student Alcohol Consumption* dataset. Covers ingestion, SQL storage, transformation, streaming simulation, and analytical visualization — designed as a showcase of real-world data engineering practices.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Pipeline Architecture](#pipeline-architecture)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Visualizations](#visualizations)
- [Key Insights](#key-insights)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Overview

This project implements a **complete data pipeline** for student performance data sourced from the UCI Machine Learning Repository. The pipeline ingests raw CSV data, loads it into a **MySQL** relational database, applies SQL-based transformations, simulates real-time streaming, and generates analytical plots using **Matplotlib** and **Seaborn**.

**This project demonstrates**:

- Raw data ingestion from flat files into a relational database
- Schema design and normalized SQL table structure
- Python-driven ETL using `pandas` and `mysql-connector-python`
- Streaming simulation of row-by-row data arrival
- Exploratory data analysis (EDA) and visualization
- Clean, modular project architecture ready for production extension

---

## Dataset

**Source:** [UCI Machine Learning Repository — Student Performance Dataset](https://archive.ics.uci.edu/ml/datasets/Student+Performance)  
**Also available on:** [Kaggle — Student Alcohol Consumption](https://www.kaggle.com/datasets/uciml/student-alcohol-consumption)

| File | Description |
|------|-------------|
| `students.csv` | Demographic and social background of students |
| `scores.csv` | Academic performance (G1, G2, G3 grades) |
| `attendance.csv` | Absences and study time records |

---

## Tech Stack

| Tool / Library | Role |
|----------------|------|
| **Python 3.13+** | Core scripting and pipeline orchestration |
| **MySQL** | Relational database for structured storage |
| **pandas** | Data manipulation and transformation |
| **mysql-connector-python** | Python ↔ MySQL bridge |
| **Matplotlib** | Data visualization and chart generation |
| **Seaborn** |  Advanced statistical visualizations like correlation heatmap relationships between attendance and academic performance |
| **Jupyter Notebook** | Exploratory data analysis |
| **VS Code** | Development environment |
| **Git & GitHub** | Version control and project hosting |
| **pip** | Python package management |

---

## Project Structure

```
student-data-pipeline/
│
├── data/
│   ├── kaggle_dataset_students.csv          # Kaggle source student data
│   ├── students.csv                         # Raw student demographic data
│   ├── scores.csv                           # Academic scores (G1, G2, G3)
│   └── attendance.csv                       # Attendance and study habits
│
├── sql/
│   └── create_database.sql            # MySQL table creations
│
├── src/
│   ├── db_connection.py      # MySQL connection handler
│   ├── extract.py            # extract data from MYSQL Table
│   ├── load.py               # load transformed data into MYSQL Table
│   ├── ingestion.py          # CSV → MySQL ingestion logic
│   ├── transform.py          # SQL-based transformations & feature engineering
│   ├── visualize.py          # Matplotlib chart generation
│   ├── pipeline.py           # Master pipeline orchestrator
│  
├── outputs/
│   └──Attendance_distribution.png
│   └──Average_Marks_distribution.png
│   └──Correlation_Heatmap.png
│   └──Improvement_Statistics.png
│   └──Performance_distribution.png
│   └──TOP_10_Students.png
│
├── notebooks/
│   └── analysis.ipynb        # EDA and insights notebook
│
├── requirements.txt          # Python dependencies
└── README.md
```

---

## Pipeline Architecture

```
## 🏗️ Pipeline Architecture

```
                ┌────────────────────────────┐
                │        Source Layer        │
                │  (MySQL Database Tables)  │
                │                            │
                │  • students                │
                │  • scores                  │
                │  • attendance              │
                └────────────┬───────────────┘
                             │
                             ▼
                ┌────────────────────────────┐
                │       Extract Layer        │
                │      (extract.py)          │
                │                            │
                │  • Read tables using SQL   │
                │  • Load into Pandas DF     │
                └────────────┬───────────────┘
                             │
                             ▼
                ┌────────────────────────────┐
                │      Transform Layer       │
                │     (transform.py)         │
                │                            │
                │  • Merge datasets          │
                │  • Feature Engineering     │
                │    - average_marks         │
                │    - attendance_percentage│
                │    - performance           │
                │    - improvement           │
                │    - attendance_bucket     │
                │                            │
                │  • Create Aggregations     │
                │    - performance_dist      │
                │    - attendance_dist       │
                │    - top_students          │
                │    - correlation_matrix    │
                └────────────┬───────────────┘
                             │
                             ▼
                ┌────────────────────────────┐
                │        Load Layer          │
                │        (load.py)           │
                │                            │
                │  • Create tables           │
                │  • Truncate old data       │
                │  • Insert new data         │
                │                            │
                │  Tables Created:           │
                │  • performance_summary     │
                │  • performance_distribution│
                │  • attendance_distribution │
                │  • top_students            │
                │  • improvement_stats       │
                │  • correlation_matrix      │
                └────────────┬───────────────┘
                             │
                             ▼
                ┌────────────────────────────┐
                │   Visualization Layer      │
                │   (visualization.py)       │
                │                            │
                │  • Histograms              │
                │  • Bar Charts              │
                │  • Scatter Plots           │
                │  • Heatmaps (Seaborn)      │
                └────────────┬───────────────┘
                             │
                             ▼
                ┌────────────────────────────┐
                │       Insight Layer        │
                │                            │
                │  • Performance trends      │
                │  • Attendance impact       │
                │  • Top performers          │
                │  • Correlation analysis    │
                └────────────────────────────┘
```

---

## Setup & Installation

### Prerequisites

- Python 3.10+
- MySQL Server running locally (or remotely)
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Student_Data_Engineering_ETL_Pipeline
.git
cd Student_Data_Engineering_ETL_Pipeline

```

### 2. Create a Virtual Environment (Recommended)

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate


### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**`requirements.txt` includes:**

```
pandas
mysql-connector-python
matplotlib
notebook
```

### 4. Configure MySQL

Start your MySQL server, then create the database:

```sql
CREATE DATABASE student_pipeline;
```

Update your credentials in `src/db_connection.py`:

```python
config = {
    "host": "localhost",
    "user": "your_mysql_user",
    "password": "your_password",
    "database": "student_pipeline"
}
```

### 5. Create Tables

```bash
mysql -u your_user -p student_pipeline < sql/schema.sql
```

---

## Usage

### Run the Full Pipeline

```bash
python src/pipeline.py
```

This will:
1. Connect to MySQL
2. Ingest all CSV files into their respective tables
3. Apply transformations (feature engineering, joins, aggregations)
4. Generate visualizations and save them to `/outputs/`
5. Log all activity to `pipeline.log`

### Run Individual Modules

```bash
# Ingest data only
python src/ingestion.py

# Run Extract only
python src/extract.py

# Run transformations only
python src/transform.py

# Run Load only
python src/load.py

# Generate visualizations only
python src/run_visualization.py

```

### Launch the Notebook

```bash
jupyter notebook notebooks/analysis.ipynb
```
---

## Key Insights
-- The majority of students perform at an average level, with fewer students in the “Excellent” and “Needs Improvement” categories, indicating a moderate overall academic performance.
-- Student scores are concentrated within a mid-range band, suggesting consistent performance with limited extreme high or low outliers.
-- Students with higher attendance percentages tend to achieve better average marks, indicating a positive relationship between attendance and academic performance.
-- Early academic performance (G1, G2) is a strong predictor of final grades (G3), while increased absences negatively impact student performance.
Most students fall into the medium-to-high attendance category, with a smaller group exhibiting low attendance, which may require intervention.
-- Top-performing students consistently maintain high average marks, indicating stable academic performance across all grading periods.
-- While some students show positive improvement over time, others decline, highlighting the need for continuous performance monitoring and support.

> Full analysis available in [`notebooks/analysis.ipynb`](notebooks/analysis.ipynb)

---

## Future Improvements

- [ ] Migrate to **PostgreSQL** for production-scale storage
- [ ] Add **Apache Airflow** for scheduled pipeline orchestration
- [ ] Build a **Streamlit dashboard** for interactive EDA
- [ ] Integrate **Docker** for containerized deployment
- [ ] Add **unit tests** with `pytest` for each pipeline stage
- [ ] Connect to **Kaggle API** for automated dataset refresh

---

## Author

**Pooja Challa**  
 
🔗 [LinkedIn](www.linkedin.com/in/poojachalla) | [GitHub](https://github.com/poojachalla-dev) | 
---

## License

Dataset credit: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Student+Performance) — P. Cortez and A. Silva, 2008.

---

> *Built as a portfolio project to demonstrate end-to-end data engineering skills across ingestion, storage, transformation, streaming, and visualization.*
