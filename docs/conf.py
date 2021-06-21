# -- Project information -----------------------------------------------------

project = 'graph theory'
copyright = '2021, haritaku'
author = 'haritaku'


# -- General configuration ---------------------------------------------------

extensions = [
    'recommonmark',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.coverage',
    'sphinx.ext.autosummary'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://numpy.org/doc/stable', None),
    'matplotlib': ('https://matplotlib.org/stable', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
    'nx-guides': ('https://networkx.org/nx-guides/', None)  # 現状反映されない
}

# todo config
todo_include_todos = True

# napoleon config
napoleon_numpy_docstring = False
napoleon_use_ivar = True
napoleon_use_admonition_for_notes = True

# type hints config
autodoc_typehints = "description"
autodoc_member_order = 'bysource'

autosummary_generate = True

add_module_names = False

# recommonmark config
source_suffix = ['.rst', '.md']
source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}


templates_path = ['_templates']

language = 'en'

exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'style_nav_header_background': '#03AF7A'
}

html_static_path = ['_static']

# html_css_files = ['custom.css']
