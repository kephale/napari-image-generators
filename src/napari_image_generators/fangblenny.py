import tempfile
import webbrowser

# because https://en.wikipedia.org/wiki/Bluestriped_fangblenny


def visualize_task_in_browser(task, html_blob=""):
    """Visualize a dask task in the browser"""

    content = task.dask._repr_html_()

    html = f"<html>{html_blob}{content}</html>"

    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".html") as f:
        url = "file://" + f.name
        f.write(html)
    webbrowser.open(url)
