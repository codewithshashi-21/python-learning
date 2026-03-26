# Day 27 – Simple data analysis using pandas

import pandas as pd


FILE = "students_data.csv"


def create_sample_data():
    data = {
        "Name": ["Sunny", "Ravi", "Anita", "Kiran"],
        "Math": [85, 70, 90, 60],
        "Science": [88, 65, 92, 58],
        "English": [80, 75, 85, 62]
    }

    df = pd.DataFrame(data)
    df.to_csv(FILE, index=False)


def analyze_data():
    df = pd.read_csv(FILE)

    print("\nFull Data:")
    print(df)

    print("\nAverage marks per student:")
    df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)
    print(df[["Name", "Average"]])

    print("\nTop student:")
    top = df.loc[df["Average"].idxmax()]
    print(top["Name"], "| Average:", round(top["Average"], 2))


if __name__ == "__main__":
    create_sample_data()
    analyze_data()