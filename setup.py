import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="consistent_sampler",
    version="0.0.1",
    author="Ronald L. Rivest",
    author_email="author@example.com",
    description="Provides consistent sampling --- sampling that is consistent across subsets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ron-rivest/consistent_sampler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)