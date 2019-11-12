import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GitPy",
    version="0.1.0",
    author="Alexandru Berbecaru",
    author_email="berbecaru.alex.ionut@gmail.com",
    maintainer="Alexandru Berbecaru",
    maintainer_email="berbecaru.alex.ionut@gmail.com",
    description="Small python library that downloads data from Github API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/berbecarualexionut/GitPy",
    packages=setuptools.find_packages(),
    install_requires=["setuptools,"
                      "requests>=2.22.0"],
)