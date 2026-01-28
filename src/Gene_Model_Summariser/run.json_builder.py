# functions for .json file builder
# writing the run.json file

import json
from pathlib import Path
from datetime import datetime

TOOL_NAME = "gene_model_summariser"
TOOL_VERSION = "0.1.0"  # bump when you release

#Uses the runner's local timezone automatically
def whats_the_time_mr_wolf() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")

