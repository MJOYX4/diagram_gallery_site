
"""
Generate diagrams from CSV data into static/plots/ for the Flask site.

- Reads "travel_reviews.csv" by default (put it in the repo root)
- Saves multiple example charts into static/plots/
- Only uses matplotlib (no seaborn), one figure per chart, no custom colors

If your IPYNB already creates images, you can skip this and just copy your
generated PNGs into static/plots/ before pushing to Git.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

CSV_PATH = "travel_reviews.csv"
OUTPUT_DIR = os.path.join("static", "plots")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_fig(name):
    out = os.path.join(OUTPUT_DIR, name)
    plt.savefig(out, bbox_inches="tight", dpi=160)
    plt.close()

def main():
    # Read CSV
    df = pd.read_csv(CSV_PATH)
    # Try to be robust to column names commonly used in "Travel Reviews" datasets
    # Adjust these to your actual column names if different
    col_cat2 = "Category 2" if "Category 2" in df.columns else df.columns[1]
    col_cat5 = "Category 5" if "Category 5" in df.columns else df.columns[min(4, len(df.columns)-1)]
    col_cat6 = "Category 6" if "Category 6" in df.columns else df.columns[min(5, len(df.columns)-1)]

    # 1) Histogram
    plt.figure()
    df[col_cat5].plot(kind="hist", bins=20)
    plt.title(f"Histogram of {col_cat5}")
    plt.xlabel(col_cat5)
    plt.ylabel("Frequency")
    save_fig("hist_category5.png")

    # 2) Scatter
    plt.figure()
    plt.scatter(df[col_cat2], df[col_cat6], alpha=0.7)
    plt.title(f"Scatter: {col_cat2} vs {col_cat6}")
    plt.xlabel(col_cat2)
    plt.ylabel(col_cat6)
    save_fig("scatter_cat2_vs_cat6.png")

    # 3) Line plot (if data looks numeric/indexed)
    plt.figure()
    df[col_cat5].reset_index(drop=True).plot(kind="line")
    plt.title(f"Line plot of {col_cat5}")
    plt.xlabel("Index")
    plt.ylabel(col_cat5)
    save_fig("line_category5.png")

    print(f"Saved images to {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
