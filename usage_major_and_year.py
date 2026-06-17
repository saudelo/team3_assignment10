"""
Questions being answered:
1. How does AI usage differ by Year of Study?
2. How does AI usage differ by Major?
"""
# libraries
import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load data
def load_data(path: str = "data/cleaned_data.csv"):
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        print(f"Error: could not find the data file at '{path}'.")
    except pd.errors.EmptyDataError:
        print(f"Error: the file '{path}' is empty.")
    return None

# create usage by year of study
def plot_by_year(df: pd.DataFrame, out_path: str = "graphs/usage_by_year.png"):
    # histograms of Weekly_GenAI_Hours for each Year_of_Study value
    years = ["freshman", "sophomore", "junior", "senior", "graduate"]

    # shared bins (2-hour width) so distributions are comparable across years
    max_hours = df["Weekly_GenAI_Hours"].max()
    bins = np.arange(0, np.ceil(max_hours) + 2, 2)  # pyright: ignore[reportCallIssue, reportArgumentType]

    fig, axes = plt.subplots(2, 3, figsize=(16, 9), sharex=True, sharey=True)
    axes = axes.flatten()

    for ax, year in zip(axes, years):
        subset = df.loc[df["Year_of_Study"] == year, "Weekly_GenAI_Hours"]
        ax.hist(subset, bins=bins, color="steelblue", edgecolor="black")
        ax.set_title(f"{year} ({subset.shape[0]} Students)")
        ax.set_xlabel("Weekly GenAI Hours")
        ax.set_ylabel("Number of Students")
        # force x tick labels on every subplot (sharex hides them on the top rows)
        ax.tick_params(labelbottom=True)

    # hide any unused subplot axes
    for ax in axes[len(years):]:
        ax.set_visible(False)

    fig.suptitle("Distribution of Weekly GenAI Hours by Year of Study", fontsize=16)
    fig.tight_layout()
    plt.savefig(out_path)
    print(f"Distribution of AI Usage by Year of Study exported to: {out_path}")
    return None

# create usage by major
def plot_by_major(df: pd.DataFrame, out_path: str = "graphs/usage_by_major.png"):
    # histograms of Weekly_GenAI_Hours for each Major_Category value
    majors = ["stem", "business", "humanities", "medical", "arts"]

    # shared bins (2-hour width) so distributions are comparable across majors
    max_hours = df["Weekly_GenAI_Hours"].max()
    bins = np.arange(0, np.ceil(max_hours) + 2, 2)  # pyright: ignore[reportCallIssue, reportArgumentType]

    fig, axes = plt.subplots(2, 3, figsize=(16, 9), sharex=True, sharey=True)
    axes = axes.flatten()

    for ax, major in zip(axes, majors):
        subset = df.loc[df["Major_Category"] == major, "Weekly_GenAI_Hours"]
        ax.hist(subset, bins=bins, color="seagreen", edgecolor="black")
        ax.set_title(f"{major} ({subset.shape[0]} Students)")
        ax.set_xlabel("Weekly GenAI Hours")
        ax.set_ylabel("Number of Students")
        # force x tick labels on every subplot (sharex hides them on the top rows)
        ax.tick_params(labelbottom=True)

    # hide any unused subplot axes
    for ax in axes[len(majors):]:
        ax.set_visible(False)

    fig.suptitle("Distribution of Weekly GenAI Hours by Major Category", fontsize=16)
    fig.tight_layout()
    plt.savefig(out_path)
    print(f"Distribution of AI Usage by Major exported to: {out_path}")
    return None

# block to run file
if __name__ == "__main__":
    df = load_data() # load
    plot_by_year(df)  # pyright: ignore[reportArgumentType]
    plot_by_major(df) # pyright: ignore[reportArgumentType]
    # print(df.head())
    # print("=" * 50)
    # print(df.columns)
    
