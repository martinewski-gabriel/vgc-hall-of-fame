# VGC Hall of Fame

A static web dashboard celebrating every Pokémon VGC World Cha: [martinewski-gabriel.github.io/vgc-hall-of-fame](https://martinewski-gabriel.github.io/vgc-hall-of-fame/)mpionship champions. Browse champion teams, explore Pokémon usage statistics, and filter by year, type, country, or age division.
Access at: [martinewski-gabriel.github.io/vgc-hall-of-fame](https://martinewski-gabriel.github.io/vgc-hall-of-fame/)


# Information
## Features

- **Hall of Fame** — championship cards for every World title, with player sprites, country flags, and type pips. Searchable and filterable by year, type, country, and division.
- **Pokémon tier board** — ranked grid of every Pokémon used in a winning team, grouped by number of titles. Optionally collapses alternate forms (Megas, Primals, etc.) into their base species.
- **Stats & Charts** — type distribution, generation spread, cumulative generation contribution, and category breakdown powered by Chart.js.
- **By Country** — leaderboard of World Championship titles grouped by nation.
- **Detail modals** — click any champion card to see the full team with type coverage and generations used; click any Pokémon to see its base stats and every champion who used it.

## Tech stack

| Layer | Tool |
|---|---|
| Frontend | Vanilla HTML/CSS/JS |
| Charts | [Chart.js 4.4](https://www.chartjs.org/) |
| Fonts | Google Fonts (Cinzel, Outfit) |
| Sprites | [PokémonDB](https://pokemondb.net/) |
| Data pipeline | Python 3 + pandas |

No build step, no framework, no dependencies to install for the frontend — just open `index.html` in a browser (or serve it statically).

## Project structure

```
vgc/
├── index.html              # entire frontend (HTML + JS)
├── style.css               # styles
├── data/
│   ├── champs.json         # processed champion data consumed by the frontend
│   ├── data.py             # pipeline: merges champion CSV with Pokédex CSV
│   ├── datasources/
│   │   ├── All VGC Pokémon Champions - Data.csv
│   │   └── Pokedex_Ver_SV2 filtered.csv
│   ├── primary.csv         # intermediate output
│   └── secondary.csv       # intermediate output
└── requirements.txt        # pandas
```

## Running locally

The frontend is a single static file — no server required for most browsers. If you run into CORS issues fetching `data/champs.json`, serve with any static file server:

```bash
# Python
python -m http.server 8000

# Node
npx serve .
```

Then open `http://localhost:8000`.

## Regenerating the data

If you update the source CSVs, re-run the pipeline to rebuild `champs.json`:

```bash
pip install -r requirements.txt
python data/data.py
```

The script merges `All VGC Pokémon Champions - Data.csv` with the Pokédex to attach types, generation, base stats, and sprite slugs to each team member, then outputs the result that the frontend loads at runtime.

## Data sources

Champion results are sourced from public VGC records. Pokédex data (types, stats, generations) is from a filtered Scarlet/Violet Pokédex snapshot.
