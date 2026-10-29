# Agentic AI Pharma Innovation Tool

A Streamlit prototype that turns a molecule name or research question into a PDF
"Product Story". A **master agent** asks six specialised agents for their view,
joins their answers, and renders the result with ReportLab. Every agent uses a local
**Llama 3 model through Ollama**, so no data leaves your machine.

> **Prototype notice:** all data in `data/` is mock data and several agents have no
> data source of their own (see *Known limitations*). Do not use the output for
> medical, regulatory or investment decisions.

## How it works

```
Streamlit UI (app.py)
        │ query
        ▼
  MasterAgent ──► IQVIAAgent      market size, CAGR, competition   (data/mock_market_data.json)
        │    ├─► ClinicalAgent   active/completed trials          (data/mock_clinical_data.json)
        │    ├─► PatentAgent     expiry, FTO risk, innovation     (data/mock_patent_data.json)
        │    ├─► EXIMAgent       API sourcing and trade risk      (data/mock_exim_data.json)
        │    ├─► InternalAgent   internal-document takeaways      (LLM only)
        │    └─► WebAgent        guidelines/news summary          (LLM only, "simulated web")
        ▼
 combine_summaries() ──► create_pdf_report() ──► reports/<query>_report.pdf
```

## Project structure

| Path | Purpose |
| ---- | ------- |
| `app.py` | Streamlit front end |
| `master_agent.py` | Runs all agents and builds the report |
| `agents/` | The six agents |
| `tools/` | Small mock lookup functions (`get_clinical_trials`, `get_patents`, `get_trade_data`, `get_market_data`) |
| `utils/` | `data_loader` (path-safe JSON loading), `logger`, `summarizer`, `report_generator` |
| `data/` | Mock JSON datasets and a sample internal report |
| `reports/` | Generated PDFs (two samples included) |
| `config/settings.yaml` | Model/temperature/path settings (not read by the code yet) |
| `tests/` | Unit tests that run without Ollama |

## Requirements

- Python 3.10 or newer
- [Ollama](https://ollama.com) running locally with the Llama 3 model: `ollama pull llama3`

## Setup and run

```sh
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
ollama serve                        # if Ollama is not already running
streamlit run app.py
```

Open the URL Streamlit prints, enter e.g. `Paracetamol`, click **Run Analysis**, then
download the PDF. A report takes a while because six model calls run one after another.

## Tests

```sh
python -m unittest discover -s tests -v
```

The agent tests replace the LLM with a stub, so they need neither Ollama nor LangChain.

## Verification status

Checked in an offline sandbox:

- 8 unit tests pass, also with `-W error::ResourceWarning`.
- The report generator is verified with awkward input (slashes, newlines, `?`, a 300-character query, and `<`/`&` in model text).
- **Not run here:** the Streamlit UI and real Ollama calls (the sandbox had no network, Streamlit, LangChain or Ollama). Run the steps above once to confirm end to end.

## Changes made during review

- `utils/report_generator.py`: a query such as `Ibuprofen/Aspirin` crashed with `FileNotFoundError` and a very long one with `OSError`. File names are now sanitised and shortened, and text is XML-escaped so model output cannot break ReportLab. Names for plain queries are unchanged.
- `app.py`: empty queries now show a warning instead of creating `_report.pdf`, and the report file handle is closed.
- `agents/*`: they now load data via `utils.data_loader`, so they work from any directory and no longer leak open files.
- Filled in files that were empty: `utils/data_loader.py`, `utils/logger.py`, the four `tools/mock_*_tool.py` modules, both test files, and `data/internal_reports/sample_report.pdf` (0 bytes before).

## Known limitations

- `config/settings.yaml` is not used; the model name `llama3` is hard-coded in each agent.
- `InternalAgent` does not read `data/internal_reports/`, and `WebAgent` does no web search. Both only prompt the LLM, so their output is not grounded in real documents or news.
- The `tools/` helpers are available but the agents still pass the whole dataset to the model.
- Agents run sequentially; `langchain` packages are unpinned in `requirements.txt`.
