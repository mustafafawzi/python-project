from setuptools import setup, find_packages

setup(
    name='mydatabaseapp',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mydatabaseapp = mydatabaseapp.main.main:main',
        ],
    },
    install_requires=[
        'colorama==0.4.6',
        'et-xmlfile==1.1.0',
        'numpy==1.24.4',
        'pandas==2.0.3',
        'python-dateutil==2.8.2',
        'pytz==2023.3.post1',
        'six==1.16.0',
        'tzdata==2023.3',
        'XlsxWriter==3.1.9',
        'openpyxl==3.1.2', 
    ],
)
