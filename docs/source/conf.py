# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
import os
import sys

from recommonmark.transform import AutoStructify

sys.path.insert(0, os.path.abspath("../../"))


# -- Project information -----------------------------------------------------
project = "poetry-sample"
copyright = "Shogo Okajimaa 2022, testname"
author = "Shogo Okajima"

# The full version, including alpha/beta/rc tags
release = "0.1.0"


# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.duration",
    "nbsphinx",
    "sphinx.ext.mathjax",
    "sphinx_markdown_tables",
    "myst_parser",
    "sphinxcontrib.blockdiag",
    "sphinxcontrib.seqdiag",
    "sphinxcontrib.actdiag",
    "sphinxcontrib.nwdiag",
    "sphinxcontrib.rackdiag",
    "sphinxcontrib.packetdiag",
]

# ----- blockdiag settings
blockdiag_html_image_format = "PNG"
blockdiag_transparency = False
seqdiag_html_image_format = "PNG"
seqdiag_transparency = False
actdiag_html_image_format = "PNG"
actdiag_transparency = False
nwdiag_html_image_format = "PNG"
nwdiag_transparency = False
rackdiag_html_image_format = "PNG"
rackdiag_transparency = False
packetdiag_html_image_format = "PNG"
packetdiag_transparency = False

# ----- CommonMark
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}
github_doc_root = "https://github.com/rtfd/recommonmark/tree/master/doc/"


def setup(app):
    app.add_config_value(
        "recommonmark_config",
        {
            "url_resolver": lambda url: github_doc_root + url,
            "auto_toc_tree_section": "Contents",
        },
        True,
    )
    app.add_transform(AutoStructify)


templates_path = ["_templates"]
exclude_patterns = ["_build", "**.ipynb_checkpoints", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
language = "ja"
html_theme = "furo"
html_search_language = "ja"
html_static_path = ["_static"]

# furo settings
html_title = "○○プロジェクト"
html_logo = "logo.png"
html_theme_options = {
    "sidebar_hide_name": False,
}
