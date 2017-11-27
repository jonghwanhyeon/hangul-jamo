from setuptools import setup, find_packages

setup(
    name='hangul-jamo',
    version='1.0.0',
    description='A library to compose and decompose Hangul syllables using Hangul jamo characters',
    url='https://github.com/jonghwanhyeon/hangul-jamo',
    author='Jonghwan Hyeon',
    author_email='hyeon0145@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Korean',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis'
    ],
    keywords='korean hangul syllable jamo composition decomposition',
    packages=find_packages(),
)
