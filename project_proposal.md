# Project Proposal: Student Performance Intelligence System

## 1) Problem Statement
Educational institutions want to identify students who may need academic support and understand factors affecting performance. Manual analysis is slow and often misses hidden patterns.

## 2) Project Goal
Build a beginner-friendly AI/ML system that:
- predicts student exam score (regression),
- classifies student performance category (classification),
- groups students into learning profiles (clustering),
- visualizes trends for decision-making.

## 3) Objectives Mapped to Lab Topics

| Lab Topic | In this project |
|---|---|
| Basic Python programs | Data handling, custom functions, reusable modules |
| Symbolic/problem-solving practice | Optional graph search (BFS/DFS) mini-task |
| BFS/DFS analysis | Student friendship/interaction graph traversal (NetworkX) |
| Data visualization | Histogram, scatter plot, box plot, heatmap |
| KNN | Classify performance level (Low/Medium/High) |
| K-Means | Cluster similar students into profiles |
| Decision Trees, Random Forest | Compare with KNN for classification |
| Linear Regression | Predict numerical final score |

## 4) Dataset Options
### Recommended (easy)
- **UCI Student Performance Dataset** (Math/Portuguese)
- Features include study time, absences, family support, previous grades.

### Alternative
- Any campus internal CSV with columns like attendance, assignment marks, quiz score, study hours.

## 5) Methodology

### Step A: Data Collection
- Download CSV dataset
- Inspect shape, data types, and missing values

### Step B: Data Preprocessing
- Handle missing values
- Encode categorical variables
- Feature scaling where required
- Create target labels for classification:
  - Low (score < 40)
  - Medium (40–70)
  - High (> 70)

### Step C: Exploratory Data Analysis (EDA)
- Histogram: distribution of scores
- Scatter plot: study time vs score
- Box plot: score by family support
- Correlation heatmap: relationships among features

### Step D: Regression Task
- Train/test split
- Linear Regression model
- Metrics: MAE, RMSE, R²

### Step E: Classification Task
- Models: KNN, Decision Tree, Random Forest
- Metrics: Accuracy, precision, recall, F1-score, confusion matrix
- Compare models and choose best

### Step F: Clustering Task
- Use K-Means with elbow method to choose K
- Interpret clusters as student learning profiles

### Step G (Optional but syllabus-aligned): BFS/DFS Mini Analysis
- Build graph where nodes are students and edges denote interaction/similarity
- Run BFS and DFS from a selected node
- Compare traversal order and interpretation

## 6) Expected Outputs
- Best regression model for score prediction
- Best classification model for performance category
- Cluster interpretations (e.g., “high effort-high performance”, “at-risk group”)
- Visual evidence from plots
- Practical recommendations for teachers/students

## 7) Tools and Libraries
- Python 3.x
- pandas, numpy
- matplotlib, seaborn
- scikit-learn
- networkx (for BFS/DFS extension)

## 8) Evaluation Plan
- Use train-test split (80-20)
- Set random seed for reproducibility
- Compare multiple models fairly using same split

## 9) Report Format (Short Report as requested)
1. Title and Abstract
2. Problem and Motivation
3. Dataset Description
4. Methodology
5. Results (tables + plots)
6. Discussion (what worked / what didn’t)
7. Conclusion and Future Work
8. Individual Contribution

## 10) Presentation Outline (5–8 slides)
1. Problem statement
2. Dataset and preprocessing
3. EDA visuals
4. Models used
5. Results comparison
6. Conclusion + future enhancements

## 11) Future Enhancements
- Add NLP sentiment from student feedback text
- Build a small Streamlit web app
- Try XGBoost for performance comparison

---

## Viva-ready explanation (short)
"I selected a student performance problem because it allows me to apply multiple AIML concepts from our lab in one project. I performed EDA, built regression and classification models, used clustering to identify student groups, and optionally demonstrated BFS/DFS on a student graph. I compared algorithms and interpreted results in a practical educational context."
