from setuptools import setup, find_packages


entry_points = [
    'k-server = koenig.utils.console:server',
    'k-client = koenig.utils.console:client',
]

requires = []

setup(
    name='koenig',
    version='0.1',
    description='Koenig Service',
    author='YUCHI',
    author_email='wei.chensh@ele.me',
    packages=find_packages(),
    url='https://github.com/streethacker/koenig',
    include_package_data=True,
    entry_points={
        'console_scripts': entry_points
    },
    zip_safe=False,
    install_requires=requires,
)
