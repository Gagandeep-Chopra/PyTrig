from setuptools import setup, find_packages

setup(
    name="pytrig",
    version="1.0.0",
    author="Your Name",
    description="A custom Python module focused on trigonometric and mathematical functions.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Gagandeep-Chopra/PyTrig",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
