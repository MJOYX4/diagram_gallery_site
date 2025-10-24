
# Diagram Gallery (PythonAnywhere + Git)

A minimal Flask site that shows your diagram images in a **2-column** grid.
Place your generated images under `static/plots/` and they will appear on the home page.

## Local usage

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python generate_plots.py    # generates example images from travel_reviews.csv
flask --app app run         # open http://127.0.0.1:5000
```

## Deploy to PythonAnywhere (free plan friendly)

1. Push this repo to GitHub (or GitLab/Bitbucket).
2. On PythonAnywhere, open a Bash console and clone your repo:
   ```bash
   git clone https://github.com/<you>/<repo>.git
   cd <repo>
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Create a **new Web app** → **Flask** → **Manual config** (Python 3.x).
4. In the Web app settings:
   - **WSGI file**: point it to your repo's `app.py` (see the WSGI example they provide; usually you set `from app import app as application`).
   - **Virtualenv**: set to the full path of `.venv` inside your repo.
5. Reload the web app. Your images in `static/plots/` will be served automatically.

> Note: Free accounts have **restricted outbound internet**. Generate your PNGs locally first, then commit them to the repo (or upload via PythonAnywhere file browser) so they show up without external downloads.
