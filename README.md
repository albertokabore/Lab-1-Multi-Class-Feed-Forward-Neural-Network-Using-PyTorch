# Lab 1: Multi-Class Feed-Forward Neural Network Using PyTorch

The completed lab contains all three assignment parts, executable commands, saved outputs,
plots, analysis, and references.

- `Lab1_FFNN_BoW_AG_News.ipynb`: complete Jupyter Notebook submission.
- `Lab1_FFNN_BoW_AG_News.docx`: Word submission generated from the executed notebook.
- `Lab1_FFNN_BoW_AG_News.pdf`: PDF submission generated from the same notebook.
- `Part_A_Feed_Forward_Neural_Networks.md`: the Part A explanation, under 500 words.
- `artifacts/metrics.json`: measured metrics, training history, versions, and input hashes.
- `artifacts/data_comparison.json`: comparison of local files with the original AG News release.
- `REVIEW.md`: requirement checklist, corrections, and verification results.

The assignment accepts any one of the notebook, Word, or PDF files.

Run commands from this repository's root using Python 3.11. The local files
`data/ag_news_csv/train.csv` and `test.csv` have headers; `classes.txt` supplies the label order.

```powershell
python -m pip install -r requirements.txt
python -u tools/execute_lab.py
```

Alternatively, open the notebook in VS Code, select the Python environment containing the
dependencies, and run all cells from the top. NLTK downloads `punkt_tab` on its first use if
the tokenizer data is absent. Later runs reuse that data. CPU execution takes several minutes.
The seed is fixed, but scores may vary with software versions and hardware.

To regenerate the Word and PDF files after a successful notebook run:

```powershell
python tools/export_lab.py
```

The export script uses the Windows Calibri and Consolas fonts. It includes saved numerical
outputs and all three plots, and creates documents without watermark objects or overlays.
Required source attribution is retained in the lab references.
