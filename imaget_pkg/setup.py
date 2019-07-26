import setuptools

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
        name='imaget',
        version='0.1',
        scripts=['imaget'],
        author="Levent Kaya",
        author_email='leventkayadev@gmail.com',
        description='Image Processor for command line.',
        long_description_content_type="text/markdown",
        url="https://github.com/lvntky/imaget",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT Lıcense",
            "Operating System:: OS Independent",
            ],

    )
