# Financial Peer Group Analytics Pipeline

This project combines data extraction notebooks, a modular machine-learning workflow, and a Streamlit dashboard to explore how publicly listed companies cluster into peer groups and how those groups rank across fundamental performance dimensions. The deliverables were prepared and collected here so the entire workflow can be rerun.

## What's Included
- **Data extraction** (`final_bda_data_extraction.ipynb`): pulls company fundamentals with `yfinance`, handles cleaning, and stores the curated panel that feeds later stages.
- **Modelling pipeline** (`bda_ml (4).ipynb`): engineers ratios, applies multiple clustering algorithms (K-Means, Agglomerative, DBSCAN, Spectral, Birch, Gaussian Mixture), builds a composite score from profitability, liquidity, leverage, efficiency, and growth signals, and keeps hooks for text-embedding fusion.
- **Interactive dashboard** (`bda_dashboard/dashboard.py`): Streamlit app that loads the exported dataset, visualises clustering results (via PCA and t-SNE projections), and lets users inspect top companies per metric by year.
- **Derived data** (`bda_dashboard/analysis_outputs_full.csv`, `bda_dashboard/cluster_summary.csv`): merged company-year panel with cluster labels, sub-scores, and summary statistics used by the dashboard.
- **Supporting artefacts** (`Modeling_Artifacts.pdf`, `Source_&_CoverageProof.pdf`, `fda-4_dataset.csv`): documentation, audit trail, and the seed dataset used when bootstrapping the process.

## End-to-End Workflow
1. **Collect and clean fundamentals** - run the extraction notebook to download raw metrics, harmonise tickers/CIKs, and persist tidy CSVs.
2. **Engineer features** - impute missing values, scale numeric features, and optionally enrich the panel with text embeddings or TF-IDF vectors when 10-K narrative sections are available.
3. **Cluster peer groups** - experiment with several clustering algorithms, compare silhouette scores, and persist selected labels (for example, the repository stores K-Means with `k=3` and DBSCAN outputs).
4. **Rank industries** - aggregate normalised sub-scores to generate a `composite_score` per company-year; scoring blocks are written so alternative weighting schemes can be dropped in easily.
5. **Inspect results** - launch the Streamlit app to review projections, cluster health, and the top entities per metric for any selected year.

## Quick Start
1. Create a fresh environment (Python 3.10+ recommended):
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate      # Windows
   pip install --upgrade pip
   pip install pandas numpy scikit-learn seaborn matplotlib streamlit yfinance tqdm
   ```
2. Open the notebooks in Jupyter or VS Code to regenerate the datasets if needed. The default configuration expects the raw CSVs in the repository root and writes enriched outputs to `bda_dashboard/`.
3. Start the dashboard once `analysis_outputs_full.csv` is available:
   ```bash
   cd bda_dashboard
   streamlit run dashboard.py
   ```

## Repository Map
- `final_bda_data_extraction.ipynb` - end-to-end data ingestion, covering ticker selection, API calls, cleaning, and persistence.
- `bda_ml (4).ipynb` - clustering and ranking pipeline with dimensionality reduction (PCA, t-SNE) and model evaluation helpers.
- `bda_dashboard/analysis_outputs_full.csv` - final modelling table (company, year, financial ratios, cluster IDs, composite and component scores).
- `bda_dashboard/cluster_summary.csv` - convenience summary per cluster for quick inspection.
- `bda_dashboard/dashboard.py` - Streamlit UI used in demos, including static projections saved as PNGs.
- `fda-4_dataset.csv` - original reference dataset before enrichment.
- `Modeling_Artifacts.pdf`, `Source_&_CoverageProof.pdf` - supplementary documentation submitted with the project.

<!-- ## Customisation Tips
- **Bring in alternative features** by modifying the feature-engineering cell in `bda_ml (4).ipynb`; the scoring dictionary makes it straightforward to append new metrics.
- **Swap clustering algorithms** by enabling or disabling blocks in the modelling notebook; each algorithm logs the silhouette score so you can compare options quickly.
- **Embed textual signals** by adding transformer-based embeddings (FinBERT, Sentence-BERT, etc.) in the optional text-fusion section; fall back to TF-IDF if GPU resources are limited.
- **Extend the dashboard** by adding additional Streamlit tabs (for example, historical trend charts or cluster drill-down tables) so stakeholders can explore beyond the provided snapshots. -->

<!-- ## Reproducibility Notes
- All output CSVs are deterministic given the same raw data and the random seeds configured in the notebooks.
- The repository does not pin package versions; when reproducing past results, capture the environment with `pip freeze > requirements.txt` before re-running the notebooks.
- Some API queries in the extraction notebook rely on external services that may rate-limit or change schema; retain local CSV backups to guarantee offline reproducibility.

## Next Steps
Planned enhancements include wiring an automated evaluation report (currently manual in the PDFs), adding unit tests for the scoring pipeline, and packaging the Streamlit app for one-click deployment. -->
