import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wapl",
    version="0.0.3",
    author="Changyun Lee",
    author_email="brownbearpower@gmail.com",
    description="TMAX WAPL testing package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZeroStrength/wapl",
    packages=setuptools.find_packages(),
    install_requires=['selenium'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)