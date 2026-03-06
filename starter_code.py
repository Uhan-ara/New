"""Beginner-friendly AIML lab project starter code.

This script demonstrates:
- Data loading/preprocessing
- Visualizations
- Linear Regression
- KNN / Decision Tree / Random Forest classification
- K-Means clustering
- Optional BFS/DFS graph traversal

It uses sklearn's built-in California housing dataset for demo convenience.
Replace with your real student dataset for final submission.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


def load_data() -> pd.DataFrame:
    housing = fetch_california_housing(as_frame=True)
    df = housing.frame.copy()
    # Make a 0-100 style score proxy for beginner demonstration
    df["score"] = np.clip((df["MedHouseVal"] / df["MedHouseVal"].max()) * 100, 0, 100)
    return df


def create_class_label(df: pd.DataFrame) -> pd.DataFrame:
    bins = [-1, 40, 70, 100]
    labels = ["Low", "Medium", "High"]
    df = df.copy()
    df["performance_label"] = pd.cut(df["score"], bins=bins, labels=labels)
    return df


def run_eda(df: pd.DataFrame) -> None:
    sns.set(style="whitegrid")

    plt.figure(figsize=(8, 5))
    sns.histplot(df["score"], kde=True)
    plt.title("Histogram of Score")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "hist_score.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=df["MedInc"], y=df["score"], s=10)
    plt.title("Scatter: Median Income vs Score")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "scatter_income_score.png")
    plt.close()

    plt.figure(figsize=(10, 8))
    corr = df.select_dtypes(include=[np.number]).corr()
    sns.heatmap(corr, cmap="coolwarm", annot=False)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "heatmap_corr.png")
    plt.close()


def run_regression(df: pd.DataFrame) -> None:
    features = [c for c in df.columns if c not in ["score", "performance_label"]]
    X = df[features]
    y = df["score"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    r2 = r2_score(y_test, preds)

    print("\n=== Linear Regression Results ===")
    print(f"MAE:  {mae:.3f}")
    print(f"RMSE: {rmse:.3f}")
    print(f"R2:   {r2:.3f}")


def run_classification(df: pd.DataFrame) -> None:
    features = [c for c in df.columns if c not in ["score", "performance_label"]]
    X = df[features]
    y = df["performance_label"].astype(str)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    models = {
        "KNN": KNeighborsClassifier(n_neighbors=7),
        "DecisionTree": DecisionTreeClassifier(random_state=42),
        "RandomForest": RandomForestClassifier(random_state=42, n_estimators=150),
    }

    print("\n=== Classification Results ===")
    for name, model in models.items():
        if name == "KNN":
            model.fit(X_train_scaled, y_train)
            preds = model.predict(X_test_scaled)
        else:
            model.fit(X_train, y_train)
            preds = model.predict(X_test)

        acc = accuracy_score(y_test, preds)
        print(f"\n{name} Accuracy: {acc:.3f}")
        print(classification_report(y_test, preds))


def run_clustering(df: pd.DataFrame) -> None:
    features = ["MedInc", "AveRooms", "AveOccup", "score"]
    X = df[features].copy()

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    inertias = []
    for k in range(2, 8):
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        km.fit(X_scaled)
        inertias.append(km.inertia_)

    plt.figure(figsize=(7, 4))
    plt.plot(range(2, 8), inertias, marker="o")
    plt.title("Elbow Method")
    plt.xlabel("k")
    plt.ylabel("Inertia")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "kmeans_elbow.png")
    plt.close()

    final_km = KMeans(n_clusters=3, random_state=42, n_init=10)
    clusters = final_km.fit_predict(X_scaled)
    df["cluster"] = clusters

    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="MedInc", y="score", hue="cluster", palette="Set2", s=14)
    plt.title("K-Means Clusters")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "kmeans_clusters.png")
    plt.close()

    print("\n=== K-Means Cluster Counts ===")
    print(df["cluster"].value_counts().sort_index())


def run_bfs_dfs_demo() -> None:
    # Small optional graph demo aligned with lab BFS/DFS topic
    g = nx.Graph()
    edges = [
        ("S1", "S2"),
        ("S1", "S3"),
        ("S2", "S4"),
        ("S2", "S5"),
        ("S3", "S6"),
    ]
    g.add_edges_from(edges)

    bfs_order = list(nx.bfs_tree(g, source="S1").nodes())
    dfs_order = list(nx.dfs_tree(g, source="S1").nodes())

    print("\n=== BFS / DFS Demo ===")
    print("BFS order:", bfs_order)
    print("DFS order:", dfs_order)


def main() -> None:
    print("Starting AIML project workflow...")
    df = load_data()
    df = create_class_label(df)
    run_eda(df)
    run_regression(df)
    run_classification(df)
    run_clustering(df)
    run_bfs_dfs_demo()
    print(f"\nDone. Check plots in: {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    main()
