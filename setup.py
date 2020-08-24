import setuptools, sys


if sys.version_info < (3, 0):
     raise NotImplementedError("Sorry, you need at least Python 2.7 or Python 3.4+ to use bottle.")

setuptools.setup(
    name='bottle-cors-plugin',
    version='0.1.0',
    author="Alfonso Villalobos",
    description="The easiest way to use cors on bottle",
    packages=setuptools.find_packages(),
    py_modules=['bottle-cors-plugin'],
    scripts=['bottle-cors-plugin.py'],
    classifiers=[
        'Development Status :: test 1'
    ],
    install_requires=[
        "bottle>=0.12",
    ],
    python_requires='>=3.6'
)
