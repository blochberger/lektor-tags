from setuptools import setup

setup(
    name='lektor-tags',
    version='0.1',
    author=u'A. Jesse Jiryu Davis',
    author_email='jesse@emptysquare.net',
    license='MIT',
    py_modules=['lektor_tags'],
    install_requires=['Lektor'],
    tests_require=['pytest'],
    url='https://github.com/ajdavis/lektor-tags',
    entry_points={
        'lektor.plugins': [
            'tags = lektor_tags:TagsPlugin',
        ]
    }
)
