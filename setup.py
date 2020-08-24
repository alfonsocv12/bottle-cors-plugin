import setuptools, sys


with open("readme.md", 'r') as fh:
    long_description = fh.read()


if sys.version_info < (3, 0):
     raise NotImplementedError("Sorry, you need at least Python 2.7 or Python 3.4+ to use bottle.")

setuptools.setup(
    name='bottle-cors-plugin',
    version='0.1.3',
    author="Alfonso Villalobos",
    author_email="alfonso@codepeat.com",
    license='MIT',
    description="The easiest way to use cors on bottle",
    long_description=long_description,
    packages=setuptools.find_packages(),
    py_modules=['bottle-cors-plugin'],
    scripts=['bottle-cors-plugin.py'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        "bottle>=0.12",
    ],
    python_requires='>=3.6'
)
