import setuptools, sys


with open("readme.rst", 'r') as fh:
    long_description = fh.read()


if sys.version_info < (3, 0):
     raise NotImplementedError("Sorry, you need at least Python 2.7 or Python 3.4+ to use bottle.")

setuptools.setup(
    name='bottle-cors-plugin',
    version='0.1.8',
    author="Alfonso Villalobos",
    author_email="alfonso@codepeat.com",
    license='MIT',
    description="The easiest way to use cors on bottle",
    long_description=long_description,
    long_description_content_type='text/x-rst',
    packages=setuptools.find_packages(),
    py_modules=['bottle_cors_plugin'],
    scripts=['bottle_cors_plugin.py'],
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
