# coding=utf-8
import re
import ast
from setuptools import setup, find_packages
from os.path import dirname, join, abspath

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('seldom/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


setup(
    name='seldom',
    version=version,
    url='https://github.com/seldomQA/seldom/',
    license='BSD',
    author='bugmaster',
    author_email='fnngj@126.com',
    description='WebUI/HTTP automation testing framework based on unittest.',
    long_description=open(join(abspath(dirname(__file__)), "description.rst"), encoding='utf8').read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'selenium>=4.0.0',
        'parameterized==0.8.1',
        'colorama>=0.4.3',
        'openpyxl>=3.0.3',
        'pyyaml>=5.1',
        'unittest-xml-reporting==3.0.4',
        'jinja2>=2.11.2',
        'requests>=2.22.0',
        'jsonschema>=3.2.0',
        'jmespath>=0.10.0',
        'webdriver-manager>=3.5.0',
        'pymysql>=1.0.0'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        "Topic :: Software Development :: Testing",
    ],
    entry_points='''
        [console_scripts]
        seldom=seldom.cli:main
    ''',
    py_modules=['whyteboard'],
    scripts=[
        'seldom/running/html/charts_script.html',
        'seldom/running/html/heading.html',
        'seldom/running/html/mail.html',
        'seldom/running/html/report.html',
        'seldom/running/html/stylesheet.html',
        'seldom/running/html/template.html',
    ],
)
