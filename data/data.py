import pandas as pd

dex = pd.read_csv("data/datasources/Pokedex_Ver_SV2 filtered.csv", sep=",")
champs = pd.read_csv("data/datasources/All VGC Pokémon Champions - Data.csv", sep=",")

#for now using only masters
#masters = champs[champs["Division"] == "Masters"].copy()
masters = champs.copy()

team_cols = [c for c in masters.columns if c.startswith("Pokémon")]

vgc_long = masters.melt(
    id_vars=["Year", "Player", "Country","Division"],
    value_vars=team_cols,
    var_name="slot",
    value_name="pokemon"
)

vgc_long = vgc_long.dropna(subset=["pokemon"])
vgc_long["pokemon"] = vgc_long["pokemon"].str.strip()

dex = dex.drop(columns=["No", "Branch_Code", "Ability1", "Ability2", "Ability_Hidden"], errors="ignore")

dex_long = pd.concat([ dex.rename(columns={"Name": "display_name",
                                           "Name2": "pokemon_name"})])

dex_long["pokemon_name"] = dex_long["pokemon_name"].fillna(dex_long["display_name"])
dex_long["pokemon_name"] = dex_long["pokemon_name"].str.strip()

vgc_merged = vgc_long.merge(
    dex_long,
    left_on="pokemon",
    right_on="pokemon_name",
    how="left"
)

print(vgc_merged)

print(vgc_merged.columns)

vgc_merged.to_csv('data/secondary.csv', sep=';')