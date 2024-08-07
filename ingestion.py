"""
This script ingest data from directory.
"""

import os
from embedchain import App
from dotenv import load_dotenv

load_dotenv()

# load chroma configuration from yaml file
app = App.from_config(config_path="ingestion.yaml")
app.add("files/", data_type="directory")
