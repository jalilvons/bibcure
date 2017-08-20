from setuptools import setup, find_packages

readme = open('README','r')
README_TEXT = readme.read()
readme.close()

setup(
    name="bibcure",
    version="0.2.4",
    packages = find_packages(exclude=["build",]),
    scripts=["bibcure/bin/bibcure"],
    long_description = README_TEXT,
    install_requires = ["bibtexparser", "future",
                      "doitobib", "titletobib", "arxivcheck"],
    include_package_data=True,
    package_data={
        "data":["data/db_abbrev.json", "data/teste"]
    },
    license="GPLv3",
    description=" Helps you to have a better bibtex file",
    author="Bruno Messias",
    author_email="messias.physics@gmail.com",
    download_url="https://github.com/bibcure/bibcure/archive/0.2.4.tar.gz",
    keywords=["bibtex", "arxiv", "doi", "abbreviate", "science","scientific-journals"],

    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Topic :: Text Processing :: Markup :: LaTeX",
    ],
    url="https://github.com/bibcure/bibcure"
)
