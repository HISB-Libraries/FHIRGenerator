'''Setup file for fhir-generator package'''
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = ["fhir.resources>=6.2.2", "Faker>=13.3.4", "orjson>=3.6.8"]

setuptools.setup(
    name="fhir-generator",
    version="0.0.1",
    author="Andrew Stevens",
    author_email="andrew.stevens@gtri.gatech.edu",
    description="A package to generate FHIR Resources",
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gt-health/FHIRGenerator",
    project_urls={
        "Bug Tracker": "https://github.com/gt-health/FHIRGenerator/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "fhirgenerator"},
    packages=setuptools.find_packages(where="fhirgenerator"),
    python_requires=">=3.6",
)
