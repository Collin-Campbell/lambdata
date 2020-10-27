import setuptools

REQUIRED = ["numpy", "pandas"]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata-collin-campbell", # Replace with your own username
<<<<<<< HEAD
    version="0.0.3",
=======
    version="0.0.2",
>>>>>>> 4ef46b43cfe76cd92cc91152d7835e93e6befe06
    author="collin-campbell",
    description="A collection of data science functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Collin-Campbell/lambdata",
    packages=setuptools.find_packages(),
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
<<<<<<< HEAD
)
=======
)
>>>>>>> 4ef46b43cfe76cd92cc91152d7835e93e6befe06
