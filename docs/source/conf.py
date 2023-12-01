# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os
import sys
from pathlib import Path
import importlib
from datetime import date

current_file_path = Path(os.getcwd())
project_root_path = current_file_path.parent.parent
sys.path.insert(0, os.path.abspath(str(project_root_path)))

package_name = "path_utils"
version = importlib.import_module(f"{package_name}._version")
todays_date = date.today()



def setup(app):
    app.add_css_file("_static/custom.css")


# -- Project information -----------------------------------------------------

project = "path_utils"
copyright = f"{todays_date.year} Marc Anglisano Roca - Spain."

# The full version, including alpha/beta/rc tags
release = version.__version__
version = version.__version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_copybutton",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx_rtd_theme",
    "sphinx_multiversion",
]

numfig = True
numfig_format = {
    "figure": "Figure %s",
    "table": "Table %s",
    "code-block": "Code Block %s",
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Whitelist pattern for tags (set to None to ignore all tags)
# This configuration maybe is overriden during command invocation
smv_tag_whitelist = r"^.*$"

# Whitelist pattern for branches (set to None to ignore all branches)
# This configuration maybe is overriden during command invocation
smv_branch_whitelist = r"^.*main|^.*develop|^latest.*$"

# Whitelist pattern for remotes (set to None to use local branches only)
smv_remote_whitelist = r"^.*$"

# Pattern for released versions
smv_released_pattern = r"^tags/.*$"

# Format for versioned output directories inside the build directory
smv_outputdir_format = "{ref.name}"

# Determines whether remote or local git branches/tags are preferred if their output dirs conflict
smv_prefer_remote_refs = True
smv_rename_latest_version = "latest"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_show_sourcelink = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


html_logo = "_static/minion.jpg"
html_theme_options = {
    "display_version": True,
    "style_nav_header_background": "linear-gradient(125deg, hsl(193deg 47% 4%) 0%, hsl(193deg 33% 9%) 9%, hsl(193deg 42% 12%) 16%, hsl(192deg 49% 15%) 23%, hsl(192deg 57% 18%) 29%, hsl(191deg 65% 21%) 36%, hsl(191deg 65% 24%) 44%, hsl(191deg 64% 28%) 53%, hsl(191deg 64% 31%) 63%, hsl(190deg 64% 34%) 76%, hsl(190deg 65% 38%) 100%);",
}


latex_elements = {
    "preamble": r"""
\usepackage{draftwatermark}
\SetWatermarkText{Confidential}
\SetWatermarkScale{1}
\makeatletter
\fancypagestyle{normal}{
\fancyhf{}
\fancyfoot[LE,RO]{{\py@HeaderFamily\thepage}}
\fancyfoot[LO]{{\py@HeaderFamily\nouppercase{\rightmark}}}
\fancyfoot[RE]{{\py@HeaderFamily\nouppercase{\leftmark}}}
\fancyfoot[C]{\copyright Copyright 2022 Servihabitat - Spain}
\fancyhead[LE,RO]{{\py@HeaderFamily \@title}}}} % here's the change
}
\fancypagestyle{plain}{
\fancyhf{}
\fancyfoot[RO]{{\py@HeaderFamily\thepage}}}}
\fancyfoot[C]{\copyright Copyright 2022 Servihabitat - Spain}
\if@twoside\fancyfoot[LE]{{\py@HeaderFamily\thepage}}}}\fi
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0.4pt}
}
\makeatother
""",
}
