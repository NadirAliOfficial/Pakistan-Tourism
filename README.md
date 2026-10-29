# Pakistan Tourism Data Analysis

Exploratory data analysis (EDA) of Pakistan tourism statistics — visitor arrivals, top destinations, revenue trends, and provincial breakdowns using Python and Jupyter Notebooks.

## Contents

| File | Description |
|------|-------------|
| `data.ipynb` | Main EDA notebook |
| `project.ipynb` | Full analysis with visualizations |
| `script.py` | Standalone analysis script |
| `gui.py` | Tkinter GUI for interactive exploration |
| `pakistan_tourism_data.csv` | Source dataset |

## Key Findings

- Visitor arrivals trend 2010–2023
- Top 5 most visited destinations by province
- Revenue vs visitor count correlation
- Seasonal patterns in tourism activity
- COVID-19 impact on tourism recovery

## Setup

```bash
git clone https://github.com/NadirAliOfficial/Pakistan-Tourism
cd Pakistan-Tourism
pip install pandas numpy matplotlib seaborn jupyter
jupyter notebook
```

## Visualizations

- Line charts: yearly visitor trends
- Bar charts: top destinations
- Heatmap: provincial activity
- Pie charts: revenue distribution

## Dataset

CSV sourced from Pakistan Tourism Development Corporation (PTDC) public data.

## License

MIT

## Description

This project performs exploratory data analysis on Pakistan tourism statistics, generating visual insights such as visitor trends, top destinations, revenue distribution, and seasonal patterns. It provides both a Jupyter notebook for detailed analysis and a Streamlit GUI for interactive exploration.

## Features

- Load and clean tourism dataset
- Generate multiple visualizations (bar, line, pie, heatmap)
- Identify top destinations and revenue contributors
- Analyze seasonal and yearly trends
- Interactive dashboard via Streamlit GUI

## Requirements

- pandas
- numpy
- matplotlib
- seaborn
- streamlit (for the GUI)
- jupyter (for notebooks)

## Installation

```bash
pip install pandas numpy matplotlib seaborn streamlit jupyter
```

## Usage

- Run the analysis script:
  ```bash
  python script.py
  ```
- Launch the interactive GUI:
  ```bash
  streamlit run gui.py
  ```
- Open the notebooks (`data.ipynb` or `project.ipynb`) in Jupyter to explore the full analysis.

## Project Structure

- `README.md` – Project overview and documentation
- `Readme.md` – Alternate README with extended description
- `script.py` – Standalone analysis script generating plots
- `gui.py` – Streamlit application for interactive visualizations
- `style.css` – CSS styling for the GUI
- `pakistan_tourism_data.csv` – Dataset source file
- `data.ipynb` – Main EDA notebook
- `project.ipynb` – Full analysis notebook with visualizations
- `LICENSE` – MIT license file
