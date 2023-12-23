from setuptools import setup, find_packages

setup(
    name='PyRussianPost',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=[''],
    package_dir={'': 'pyrussianpost'},
    url='https://github.com/schubarkrsk/PyRussianPost',
    license='Apache-2.0',
    author='Stanislav Chubar',
    author_email='stas-chubar@yandex.ru',
    description='Library for easy use Russian Post tracking API',
    install_requires=[
       "requests>=2.31.0",
        "zeep>=4.2.1",
    ],
)
