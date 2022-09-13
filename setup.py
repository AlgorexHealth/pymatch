from setuptools import setup

dependencies = [
    'seaborn',
    'statsmodels',
    'scipy',
    'patsy',
    'matplotlib',
    'pandas',
    'numpy'
  ]

VERSION = "0.3.4.2"

setup(
    name='pymatch',
    packages=['pymatch'],
    version=VERSION,
    description='Matching techniques for Observational Studies',
    author='Ben Miroglio',
    author_email='benmiroglio@gmail.com',
    url='https://github.com/AlgorexHealth/pymatch',
    download_url='git@github.com:AlgorexHealth/pymatch.git',
    keywords=['logistic', 'regression', 'matching', 'observational', 'study', 'causal', 'inference'],
    include_package_data=True,
    install_requires=dependencies
)
