from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in hr_extras/__init__.py
from hr_extras import __version__ as version

setup(
	name='hr_extras',
	version=version,
	description='App That Extend the hr doctypes',
	author='Ebkar Technology & Management Solutions',
	author_email='support@ebkarco.ly',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	include_package_data=True,
	install_requires=install_requires
)
