import pandas as pd
import matplotlib.pyplot as plt

def analyze():
    df = pd.read_csv("data/cleaned.csv")

    team_runs = df.groupby("team")["runs"].mean()

    team_runs.plot(kind="bar")

    plt.title("Average Runs by Team")
    plt.xlabel("Teams")
    plt.ylabel("Runs")

    plt.tight_layout()
    plt.savefig("team_runs.png")

    print("Analysis Complete")
