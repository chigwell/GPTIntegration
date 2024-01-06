from setuptools import setup, find_packages

# Reading long description from README.md
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='GPTIntegration',
    version='0.0.1',
    description='A module for integrating various GPT models for diverse tasks.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Eugene Evstafev',
    author_email='chigwel@gmail.com',
    url='https://github.com/chigwell/GPTIntegration',
    packages=find_packages(),
    install_requires=[
        'openai',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
