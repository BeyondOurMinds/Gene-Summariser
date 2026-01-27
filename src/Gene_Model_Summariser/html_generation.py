#pillar 3 - HTML Report Generation

from multiprocessing import context
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape


def generate_html_report(tsv_output: dict) -> str: #tsv_output will be renamed once Pillar 1 tsv_output dict is finished
    pillar3_folder = Path(__file__).resolve().parent # Get the directory of the current file and set as template folder for Jinja2

    # Set up Jinja2 environment from the folder
    env = Environment( 
        loader=FileSystemLoader(str(pillar3_folder)),
        autoescape=select_autoescape(["html", "xml"]),
    )

    template = env.get_template("groupB.html.j2") # Load the HTML template file from the pillar3 folder

    # tsv_output will be available in Jinja as {{ data }}
    html_output = template.render(data=tsv_output)
    return html_output






