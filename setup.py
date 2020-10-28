from setuptools import setup

with open("requirements.txt") as f:
    install_requires = [line.strip() for line in f]

try:
    import pypandoc
    long_description = pypandoc.convert('README_PKG_INFO.md', 'rst')
except(IOError, ImportError):
    long_description = open('README_PKG_INFO.md').read()


setup(
    name="Sendinblue",
    description = "Official SendinBlue provided Python API Package.",
    long_description = long_description,
    version="2.0.5.1",
    py_modules=["mailin"],
    install_requires=install_requires
)
