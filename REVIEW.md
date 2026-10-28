# Assignment review

The notebook, Word document, and PDF contain Parts A, B, and C and source references.
Any one of these three formats satisfies the submission-format requirement.

| Requirement | Verified location |
|---|---|
| Part A under 500 words | Part A: 401 words using whitespace counting, including its heading |
| Enable tqdm in pandas | B.1: `tqdm.pandas()` |
| Use train.csv, test.csv, and classes.txt | B.2 and B.9 |
| Load, examine, and describe training data | B.3: dimensions, examples, types, class counts, lengths, and noise checks |
| Replace backslashes using pandas replace | B.4: `Series.replace` with a regular expression |
| Tokenize title and description with NLTK | B.5: joined text, `word_tokenize`, and a new `tokens` column |
| Build the vocabulary from training data | B.6: fitting split only, frequency threshold, and unknown-token feature |
| Initialize model, loss, optimizer, and loaders | B.7 |
| Train the model | B.8: five epochs with training and development metrics |
| Evaluate on test data | B.9: report, confusion matrices, and error examples |
| Explain commands and evaluation results | C.1 and C.2 |
| Cite external sources | In-text citations and References |

All 28 code cells completed successfully in a fresh Python kernel. The run reproduced the
previously reported metrics and raw confusion matrix. Independent checks confirmed the
accuracy, per-class precision, and recall against the raw matrix, and verified the input-file
hashes saved in `artifacts/metrics.json`.

- Training/development/test examples: 96,000 / 24,000 / 7,600.
- Vocabulary: 17,369 features; model: 868,704 parameters.
- Correct test predictions: 6,982; errors: 618.
- Test accuracy: 91.8684%; macro F1: 0.918506.
- Final development accuracy: 92.1583%.
- Execution time recorded inside the notebook: approximately 16 minutes 49 seconds on CPU.

The review corrected overstatements about reproducibility, overfitting, exact agreement
with rounded reference scores, and the causes of classification errors. It also made the
required pandas replacement explicit, documented integer label types, clarified the memory
estimate, and connected quantitative observations to printed evidence.

Comparison with the original AG News archive confirmed identical labels and class names.
Text differs in 26 training rows and 2 test rows; details are in
`artifacts/data_comparison.json`. Corrupted local text is handled consistently across splits.

No watermark objects or visible watermark overlays were found in the original Word/PDF
files. Both exports were regenerated from the reviewed notebook using clean layouts.
Author information, page numbers, and required source attribution remain part of the report.
The exports include the three plots and the numerical outputs.
