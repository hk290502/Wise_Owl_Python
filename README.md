# WiseOwl: Python for Data

A personal drill-and-practice repo for building fluency in Python, with a focus on the data space. Each folder targets a specific skill area, working through exercises from the ground up.

## Structure

| Folder | What's covered |
|---|---|
| `basic_coding/` | Core syntax — variables, conditionals, basic logic |
| `ranges_and_loops/` | `for`/`while` loops, `range()`, loop patterns (prime numbers, square roots, etc.) |
| `sequences/` | Lists, tuples, iteration, and sequence manipulation |
| `slicing/` | String and list slicing, word frequency analysis |
| `comprehensions/` | List and dict comprehensions |
| `dictionaries/` | Dict creation, access patterns, real-world examples |
| `functions/` | Defining functions, arguments, return values |
| `files_and_folders/` | Reading/writing files, working with the filesystem |
| `working_with_sets/` | Set operations and use cases |
| `csv_and_excel/` | Reading CSVs and Excel files with `openpyxl` |
| `overview_of_numpy/` | Array operations, numerical analysis with NumPy |
| `overview_of_pandas/` | DataFrames, sorting, filtering, reading Excel — core Pandas workflows |
| `matplotlib/` | Bar charts, pie charts, multi-panel figures, styling |
| `linking_to_sql_server/` | Connecting to SQL Server via `pyodbc`, running queries |
| `scraping_websites/` | Basic web scraping with `requests` and `BeautifulSoup` |
| `miscellaneous/` | Ad-hoc scripts combining multiple skills (PostgreSQL + Pandas, CSV exports, etc.) |

## Libraries practised

- **Data wrangling:** `pandas`, `numpy`
- **Visualisation:** `matplotlib`
- **Databases:** `pyodbc` (SQL Server), `psycopg2` (PostgreSQL)
- **Files:** `openpyxl`, built-in `csv`
- **Web:** `requests`, `beautifulsoup4`
- **Utilities:** `python-dotenv`

## Notes

- This is a learning repo and not production code.
- Database exercises assume local SQL Server (`.\sql2019`) or a PostgreSQL instance configured via a `.env` file.
- Excel/CSV data files are stored alongside the scripts that use them.
