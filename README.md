Here’s a clear, PEP 8-aligned naming guide for Python projects — both for code inside the project and for the overall repo/package layout.

⸻

🏷️ 1. Project & Package Structure

my_project/
│
├── pyproject.toml      # or setup.cfg / setup.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── src/                # optional if you follow “src layout”
│   └── my_project/     # package folder
│       ├── __init__.py
│       ├── core.py
│       ├── utils.py
│       └── models/
│           ├── __init__.py
│           └── base_model.py
│
└── tests/
    └── test_core.py

	•	Top-level repo name:
	•	Use lowercase-with-hyphens for GitHub repo (my-project)
	•	Use snake_case for the Python package (my_project).

⸻

🐍 2. Files & Modules

Element	Convention	Example
Packages (folders with __init__.py)	snake_case	my_project, data_utils
Modules (single .py file)	snake_case	helpers.py, data_loader.py
Private modules	leading underscore	_internal_utils.py


⸻

🔧 3. Classes, Functions, Variables

Item	Style	Example
Classes	PascalCase	class TradeProcessor:
Exceptions	PascalCase, end with Error	class ConfigError(Exception):
Functions	snake_case	def load_data():
Variables	snake_case	trade_count = 0
Constants	UPPER_CASE_WITH_UNDERSCORES	MAX_RETRY = 3
Private (internal)	leading underscore	_calculate_price()


⸻

⚙️ 4. Configuration & Scripts
	•	Config files: settings.json, .env, config.yaml
	•	CLI entry script: cli.py or __main__.py
	•	If packaging, use an entry point in pyproject.toml or setup.cfg.

⸻

🧪 5. Tests
	•	Put tests in a top-level tests/ directory.
	•	Files: test_<module>.py → test_core.py.
	•	Functions: def test_functionality():.

⸻

🧭 6. Naming Tips
	•	Be descriptive but concise: price_feed_handler.py is better than pfh.py.
	•	Avoid reserved keywords: don’t name a module email.py or json.py (it can shadow stdlib).
	•	Keep consistency: If you pick snake_case for packages, stick to it everywhere.

⸻

✅ Quick Summary
	•	Project repo: my-project
	•	Package/module: my_project
	•	Classes: PascalCase
	•	Functions & vars: snake_case
	•	Constants: UPPER_CASE
	•	Private: _leading_underscore

⸻


 ## the *.egg-info folder
 is **metadata** automatically created by Python packaging tools such as `setuptools` or `pip`.  

Let’s break it down 👇

---

## 🥚 What is an `.egg-info` Folder?

When you run commands like:
```bash
python setup.py install
# or
pip install -e .

# you can safely delete it and reinstall:
rm -rf src/python_school.egg-info
pip install -e .3

----

