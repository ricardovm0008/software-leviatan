import sphinx_rtd_theme

# -- Información del Proyecto ------------------------------------------------
project = 'Cluster Leviatán BUAP'
copyright = '2026, Laboratorio Nacional de Supercómputo del Sureste de México'
author = 'Laboratorio Nacional de Supercómputo del Sureste de México'
release = '1.0'
version = '1.0'

# -- Configuración General ---------------------------------------------------
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'es'

# Prevenir duplicados en etiquetas de sección
autosectionlabel_prefix_document = True

# -- Opciones de Salida HTML -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'style_nav_header_background': '#003b5c',  # Azul institucional BUAP
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

# Logo y favicon
html_logo = "_static/image.png"
# html_favicon = "_static/favicon.ico"  # Descomenta si tienes un favicon

# Título en la pestaña del navegador
html_title = f"{project} v{version}"

# Pie de página personalizado
html_show_sphinx = False
html_show_copyright = True

# -- Opciones de Salida LaTeX (PDF) ------------------------------------------
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'preamble': r'''
        \usepackage[spanish]{babel}
    ''',
}

latex_documents = [
    ('index', 'ClusterLeviatan.tex', 
     'Catálogo del Cluster Leviatán',
     'Laboratorio Nacional de Supercómputo', 'manual'),
]

def setup(app):
    app.add_css_file('custom.css')