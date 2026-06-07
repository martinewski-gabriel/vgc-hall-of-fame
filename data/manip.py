import pandas as pd
import json

df = pd.read_csv("data/secondary.csv", sep=';')

df["Country"] = df["Country"].fillna("")

# Group by Year + Player (each champion)
grouped = df.groupby(["Year", "Player", "Country", "Division"])

champs = []

SPRITE_OVERRIDES = {
    #calyrex
    "calyrex-s":"calyrex-shadow-rider",
    "calyrex-i":"calyrex-ice-rider",


    # Urshifu
    "urshifu-d": "urshifu-single-strike",
    "urshifu-w": "urshifu-rapid-strike",

    # Zacian / Zamazenta
    "zacian-cs": "zacian-crowned",
    "zamazenta-c-s":"zamazenta-crowned",

    # Ogerpon
    "ogerpon-f": "ogerpon-hearthflame",
    "ogerpon-w": "ogerpon-wellspring",
    "ogerpon-r": "ogerpon-cornerstone",

    # Rotom (usually fine but safe)
    "rotom-h": "rotom-heat",
    "rotom-w": "rotom-wash",
    "rotom-fr": "rotom-frost",
    "rotom-fan": "rotom-fan",
    "rotom-m": "rotom-mow",

    #genies
    "landorus-t":"landorus-therian",
    "thundurus-t":"thundurus-therian",
    "tornadus-t":"tornadus-therian",

    "landorus-i":"landorus-incarnate",
    "thundurus-i":"thundurus-incarnate",
    "tornadus-i":"tornadus-incarnate",

    #alola
    "marowak-a":"marowak-alolan",

    #hisui
    "arcanine-h":"arcanine-hisuian"


}

for (year, player, country, division), group in grouped:
    team = []

    for _, row in group.iterrows():
        slug_raw = row["pokemon"].lower().replace(" ", "-")
        slug = SPRITE_OVERRIDES.get(slug_raw, slug_raw)

        team.append({
            "name": row["display_name"],
            "code": row['pokemon'],
            "base": row['Original_Name'],
            "t1": row["Type1"],
            "t2": row["Type2"] if pd.notna(row["Type2"]) else "",
            "gen": int(row["Generation"]),
            "category": row["Category"],
            "slug": slug,
            "base_slug": row["Original_Name"].lower().replace(" ", "-"),
            "image": f"https://img.pokemondb.net/sprites/home/normal/{slug}.png",
            "stats": {
                "hp":  int(row["HP"]),
                "atk": int(row["Attack"]),
                "def": int(row["Defense"]),
                "spa": int(row["SP_Attack"]),
                "spd": int(row["SP_Defense"]),
                "spe": int(row["Speed"]),
            }
        })

    champs.append({
        "year": int(year),
        "player": player,
        "country": country, 
        "division": division,
        "team": team
    })

# sort by year descending (like your UI expects)
champs = sorted(champs, key=lambda x: x["year"], reverse=True)

with open("data/champs.json", "w") as f:
    json.dump(champs, f, indent=2)