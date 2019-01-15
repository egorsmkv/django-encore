import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme_file:
    readme = readme_file.read()

setup(
    name='django-encore',
    description='Django integration with Webpack Encore',
    long_description=readme,
    license='MIT',
    version='0.0.1',
    url='https://github.com/egorsmkv/django-encore',
    project_urls={
        'Source': 'https://github.com/egorsmkv/django-encore',
        'Tracker': 'https://github.com/egorsmkv/django-encore/issues',
    },
    author='Yehor Smoliakov',
    author_email='yehors@ukr.net',
    packages=find_packages(include=['encore', 'encore.templatetags']),
    include_package_data=True,
    install_requires=[
        'Django>=2.1.5',
    ],
    python_requires='>=3',
    keywords='django django-encore webpack-encore',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
