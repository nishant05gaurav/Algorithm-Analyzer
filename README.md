# Algorithm Performance Analyzer

A benchmarking engine that empirically evaluates standard sorting and searching algorithms using high-precision timing. It bridges theoretical Data Structures and Algorithms (DSA) with practical data-driven visualization to reveal how algorithms actually behave in the real world across varying input sizes and distributions.

## Quick Start

```bash
git clone [https://github.com/nishantgaurav/algorithm-analyzer.git](https://github.com/nishantgaurav/algorithm-analyzer.git)
cd algorithm-analyzer
pip install pandas matplotlib seaborn
python src/main.py
```

## Demo / Preview

This project is split into two parts:

### 1. Experiment Engine (CLI)
- Runs multiple benchmarks on sorting & searching algorithms  
- Generates structured CSV results  

### 2. Analysis Notebook (Visualization)
Produces:
- Line plots (normal + log scale)  
- Boxplots (performance distribution)  
- Heatmaps (algorithm vs input size)  
- Comparative graphs (Linear vs Binary Search)  

### Observations from the Notebook

- Bubble Sort clearly explodes with input size *(O(n²))*  
- Quick Sort and Merge Sort remain stable and efficient  
- Log scale reveals performance gaps that normal scale hides  
- Binary Search dominates Linear Search for large datasets  
- Sorting + Binary Search outperforms Linear Search at scale  

## Problem & Purpose

Most algorithm learning stops at **Big-O notation**.
But in reality:
- Input type matters *(sorted, reverse, random)*  
- Constant factors matter  
- Stability and variance matter  
- Visualization matters  

This project was built to bridge that gap. Instead of memorizing complexity, you observe behavior:
- How algorithms degrade  
- When simple algorithms outperform advanced ones  
- When preprocessing *(sorting)* is worth it  

### Designed For
- Students preparing for DSA interviews  
- Anyone who wants intuition beyond theory  
- Developers curious about real-world performance  
 

## Highlights

* **Precision Benchmarking:** Utilizes `time.perf_counter()` to capture highly accurate fractional second execution times, mitigating the noise of basic system clocks.
* **Distribution-Aware Testing:** Doesn't just test random arrays. The input generator creates Random, Sorted, Reverse, and Nearly Sorted datasets to test algorithmic edge cases (like Insertion Sort's efficiency on nearly sorted data).
* **Statistical Stability:** Runs multiple iterations (default 5 runs per size/type) to average out CPU spikes and OS background tasks, ensuring the resulting data is statistically sound.
* **Log-Scale Visual Analysis:** Implements logarithmic scaling in Matplotlib to properly inspect the performance gap between highly efficient algorithms (like Quick Sort vs. Merge Sort) that would otherwise be visually crushed at the bottom of a standard linear chart.

## Features

* **Sorting Analysis:** Benchmarks Bubble, Insertion, Merge, and Quick Sort.
* **Searching Analysis:** Benchmarks Linear vs. Binary Search.
* **Automated Data Logging:** Automatically structures benchmark results and saves them directly to `results.csv` and `search_results.csv` for decoupling data collection from visualization.
* **Rich Visualizations:** A dedicated Jupyter Notebook leveraging Seaborn for heatmaps, boxplots, and standard line charts.

## Tech Stack

* **Core Language:** Python 3
* **Benchmarking & Logic:** Standard Library (`time`, `random`)
* **Data Manipulation:** Pandas
* **Visualization:** Matplotlib, Seaborn, Jupyter Notebook

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/nishantgaurav/algorithm-analyzer.git](https://github.com/nishantgaurav/algorithm-analyzer.git)
   cd algorithm-analyzer
   ```
2. **Set up a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt 
   # Alternatively: pip install pandas matplotlib seaborn jupyter
   ```

## Usage

The project is split into two phases: data generation and visual analysis.

**1. Generate the Benchmark Data**
Run the core experiments to test the algorithms and generate the CSV files.
```bash
python src/main.py
```
*Note: This will execute the functions defined in `experiments.py` and output `results.csv` and `search_results.csv` into the `data/` directory.*

**2. Analyze the Results**
Launch Jupyter Notebook to view and interact with the visualizations.
```bash
jupyter notebook notebooks/analysis.ipynb
```
Run the cells sequentially to read the generated CSVs and render the Matplotlib/Seaborn charts.

## Project Structure

```text
algorithm-analyzer/
├── data/
│   ├── results.csv            # Generated sorting benchmark data
│   └── search_results.csv     # Generated searching benchmark data
├── notebooks/
│   └── analysis.ipynb         # Data visualization and statistical breakdown
├── src/
│   ├── __init__.py
│   ├── experiments.py         # Test runners and CSV formatting logic
│   ├── input_generator.py     # Generates varied array distributions
│   ├── searching.py           # Search algorithm implementations
│   ├── sorting.py             # Sort algorithm implementations
│   └── main.py                # Entry point to trigger experiments
└── README.md
```

## Contributing

If you want to add new algorithms (e.g., Heap Sort, Radix Sort), simply create the implementation in `src/sorting.py`, add the timing wrapper in `src/experiments.py`, and submit a pull request.


## License

MIT License: Use it, Fork it, Build on it.


## Author

Built by [Nishant Gaurav](https://github.com/nishant05gaurav)  
[LinkedIn](https://linkedin.com/in/nishant05gaurav) · [Portfolio](https://nishant05gaurav.github.io/)