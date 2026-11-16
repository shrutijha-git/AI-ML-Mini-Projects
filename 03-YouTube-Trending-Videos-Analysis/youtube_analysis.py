
from pathlib import Path
import json

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# STEP 1: Set up file paths
project_dir = Path(__file__).resolve().parent
data_dir = project_dir / "data"
output_dir = project_dir / "outputs"

output_dir.mkdir(parents=True, exist_ok=True)

csv_path = data_dir / "USvideos.csv"
json_path = data_dir / "US_category_id.json"

sns.set_theme(style="whitegrid")


# STEP 2: Load the YouTube dataset
print("Loading YouTube dataset...")

df = pd.read_csv(csv_path, encoding="utf-8")

print("\nDataset loaded successfully!")
print("Dataset shape:", df.shape)

print("\nFirst five rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())


# STEP 3: Check and clean the data
print("\n--- DATA CLEANING ---")

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

df = df.drop_duplicates().copy()

numeric_columns = ["views", "likes", "dislikes", "comment_count"]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column], errors="coerce"
    )

df[numeric_columns] = df[numeric_columns].fillna(0)

print("\nRows after removing exact duplicates:", len(df))


# STEP 4: Load YouTube category names
with open(json_path, "r", encoding="utf-8") as file:
    category_data = json.load(file)

category_mapping = {
    int(item["id"]): item["snippet"]["title"]
    for item in category_data["items"]
}

df["category_name"] = (
    df["category_id"]
    .map(category_mapping)
    .fillna("Unknown")
)

print("\nCategory names loaded successfully!")


# STEP 5: Basic statistics
print("\n--- YOUTUBE TRENDING VIDEO ANALYSIS ---")

print("\nTotal trending records:", len(df))
print("Unique videos:", df["video_id"].nunique())
print("Unique channels:", df["channel_title"].nunique())

print("\nAverage views:", round(df["views"].mean(), 2))
print("Average likes:", round(df["likes"].mean(), 2))
print("Average comments:", round(df["comment_count"].mean(), 2))


# STEP 6: Analyze video categories
category_counts = df["category_name"].value_counts()

print("\nTop 10 categories by trending appearances:")
print(category_counts.head(10))

plt.figure(figsize=(12, 6))

sns.barplot(
    x=category_counts.head(10).values,
    y=category_counts.head(10).index,
    color="steelblue"
)

plt.title("Top 10 YouTube Trending Categories")
plt.xlabel("Number of Trending Records")
plt.ylabel("Category")
plt.tight_layout()

plt.savefig(
    output_dir / "top_trending_categories.png",
    dpi=300
)
plt.close()

print("Saved: top_trending_categories.png")


# STEP 7: Most frequently trending channels
channel_counts = df["channel_title"].value_counts().head(10)

print("\nTop 10 channels by trending appearances:")
print(channel_counts)

plt.figure(figsize=(12, 6))

sns.barplot(
    x=channel_counts.values,
    y=channel_counts.index,
    color="coral"
)

plt.title("Top 10 Channels by Trending Appearances")
plt.xlabel("Number of Trending Records")
plt.ylabel("Channel")
plt.tight_layout()

plt.savefig(
    output_dir / "top_trending_channels.png",
    dpi=300
)
plt.close()

print("Saved: top_trending_channels.png")


# STEP 8: Relationship between views and likes
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="views",
    y="likes",
    alpha=0.3,
    s=20
)

plt.title("YouTube Views vs Likes")
plt.xlabel("Views")
plt.ylabel("Likes")
plt.tight_layout()

plt.savefig(
    output_dir / "views_vs_likes.png",
    dpi=300
)
plt.close()

print("Saved: views_vs_likes.png")


# STEP 9: Calculate engagement rate
# Engagement = (likes + dislikes + comments) / views
# This is a simple descriptive metric, not an official YouTube metric.

df["engagement_rate"] = np.where(
    df["views"] > 0,
    (
        df["likes"]
        + df["dislikes"]
        + df["comment_count"]
    ) / df["views"] * 100,
    np.nan
)

print("\nAverage engagement rate (%):")
print(round(df["engagement_rate"].mean(), 2))

category_engagement = (
    df.groupby("category_name")["engagement_rate"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))

sns.barplot(
    x=category_engagement.values,
    y=category_engagement.index,
    color="mediumseagreen"
)

plt.title("Top 10 Categories by Average Engagement Rate")
plt.xlabel("Average Engagement Rate (%)")
plt.ylabel("Category")
plt.tight_layout()

plt.savefig(
    output_dir / "category_engagement.png",
    dpi=300
)
plt.close()

print("Saved: category_engagement.png")


# STEP 10: Analyze correlations
correlation_columns = [
    "views", "likes", "dislikes", "comment_count"
]

correlation_matrix = df[correlation_columns].corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("YouTube Engagement Metrics Correlation")
plt.tight_layout()

plt.savefig(
    output_dir / "correlation_heatmap.png",
    dpi=300
)
plt.close()

print("Saved: correlation_heatmap.png")


# STEP 11: Save summary results
summary_path = output_dir / "analysis_summary.txt"

with open(summary_path, "w", encoding="utf-8") as file:
    file.write("YOUTUBE TRENDING VIDEOS ANALYSIS\n")
    file.write("=" * 40 + "\n\n")

    file.write(f"Total trending records: {len(df)}\n")
    file.write(f"Unique videos: {df['video_id'].nunique()}\n")
    file.write(
        f"Unique channels: {df['channel_title'].nunique()}\n"
    )

    file.write(
        f"Average views: {df['views'].mean():.2f}\n"
    )
    file.write(
        f"Average likes: {df['likes'].mean():.2f}\n"
    )
    file.write(
        f"Average comments: {df['comment_count'].mean():.2f}\n"
    )
    file.write(
        f"Average engagement rate: "
        f"{df['engagement_rate'].mean():.2f}%\n"
    )

    file.write("\nTOP 10 CATEGORIES\n")
    file.write(category_counts.head(10).to_string())

    file.write("\n\nTOP 10 CHANNELS\n")
    file.write(channel_counts.to_string())

print("\nSaved: analysis_summary.txt")

print("\nANALYSIS COMPLETED SUCCESSFULLY!")
print("All charts and results are saved in:", output_dir)
