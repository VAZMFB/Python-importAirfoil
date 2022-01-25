from distutils.core import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
print(long_description)

setup(
    name='importAirfoil',
    version='1.3.0',
    packages=['importAirfoil'],
    url='https://github.com/VAZMFB/Python-importAirfoil',
    download_url = 'https://github.com/VAZMFB/Python-importAirfoil/archive/refs/tags/1.3.0.tar.gz',
    keywords = ['airfoil', 'import-airfoil'],
    license='GPL-3.0-or-later',
    author='Miloš Petrašinović',
    author_email='mpetrasinovic@mas.bg.ac.rs',
    description='Airfoil coordinates import function',
    classifiers = [],
    long_description=long_description,
    long_description_content_type='text/markdown'
)