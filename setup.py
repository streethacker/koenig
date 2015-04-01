from setuptools import setup, find_packages


requires = [
]

setup(
    name='koenig',
    version='0.1',
    description='Koenig Service',
    author='YUCHI',
    author_email='wei.chensh@ele.me',
    packages=find_packages(),
    url='https://github.com/streethacker/koenig',
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
)
