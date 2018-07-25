# academic_census
Supplementary data and code for:

> Morgan, A. C., Way, S. F., & Clauset, A. (2018). Automatically assembling a full census of an academic field. arXiv preprint arXiv:1804.02760.

##### `data`
- Confusion matrix with transition rates between faculty titles in 2011 and 2017 (`confusion.csv`, see Table 1).
- Faculty transitions between 2011 and 2017 (`faculty.csv`, see Figures 5 & 6 and Table 3). Includes the title and institution of the faculty member in 2011 (if new faculty, left blank), and title and institution in 2017 (if no longer present, left blank).
- Department rates of attrition between 2011 and 2017 (`attrition.csv`). Validation of these rates (`uni_correction.tsv`). 

##### `misc`
- Outlines necessary keyword lists (`helpers.py`, see Appendices S1-S5).
- Notebook `name_matching.ipynb` shows how we link faculty names between 2011 and 2017 using Levenshtein distance.

##### `network`
- Generates a network visualization and the GML for the two-hop hyperlink network from a department's homepage (see Figure 2).

##### `retention`
- Analysis of faculty retention rates (see Figures 5 & 6, and Table 3).
- Department level retention analysis (see Table 2).

##### `timing`
- Generates results of crawler timing (see Figure 4). The notebook `timing.ipynb` loads two JSON files -- `dijkstra_traversals.json` (shortest path) and `traversals.json` (actual path).
