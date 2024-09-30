# docs/conf.py

# -- Project information -----------------------------------------------------
project = 'live speech translator'
author = 'Hosung Park'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',  # 자동으로 docstring에서 문서 생성
    'sphinx.ext.napoleon', # Google 스타일과 NumPy 스타일 docstring 지원
    'sphinx.ext.viewcode', # 코드 뷰어 기능 추가
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # Read the Docs 기본 테마 사용
html_static_path = ['_static']

# -- Napoleon settings -------------------------------------------------------
# Google style과 NumPy style의 docstring을 Sphinx에서 지원하게 하는 설정
napoleon_google_docstring = True
napoleon_numpy_docstring = True
