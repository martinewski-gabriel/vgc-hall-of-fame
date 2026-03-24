import pandas as pd
import json

df = pd.read_csv("data/primary.csv", sep=';')


# Filter only Masters (just in case)
df = df[df["Division"] == "Masters"]

# Group by Year + Player (each champion)
grouped = df.groupby(["Year", "Player"])

champs = []

for (year, player), group in grouped:
    team = []

    for _, row in group.iterrows():
        team.append({
            "name": row["pokemon"],
            "base": row['Original_Name'],
            "t1": row["Type1"],
            "t2": row["Type2"] if pd.notna(row["Type2"]) else "",
            "gen": int(row["Generation"]),
            "category": row["Category"],
            "slug": row["pokemon"].lower().replace(" ", "-"),
            "base_slug": row["Original_Name"].lower().replace(" ", "-"),
            "image": row["image_url"] # simple slug
        })

    champs.append({
        "year": int(year),
        "player": player,
        "country": "UNKNOWN",  # we'll fix this next
        "team": team
    })

# sort by year descending (like your UI expects)
champs = sorted(champs, key=lambda x: x["year"], reverse=True)

with open("data/champs.json", "w") as f:
    json.dump(champs, f, indent=2)