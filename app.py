
from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route("/")
def index():
    # Find all .png/.jpg diagrams in static/plots
    plots_path = os.path.join(app.static_folder, "plots")
    image_files = []
    if os.path.isdir(plots_path):
        for name in sorted(os.listdir(plots_path)):
            if name.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg")):
                image_files.append(("plots/" + name))
    return render_template("index.html", image_files=image_files)

if __name__ == "__main__":
    app.run(debug=True)
