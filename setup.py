from setuptools import setup, find_packages

setup (
    name='lighthouse',
    version = '1.0',
    author='Clint Ecker',
    author_email='clint@arstechnica.com',
    url='http://github.com/clintecker/python-lighthouse-api',
    description="""A Python Lighthouse API Library""",
    packages=find_packages(),
    namespace_packages = [],
    include_package_data = True,
    zip_safe=False,
    license=''
)
