from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in testnjyadu/__init__.py
from testnjyadu import __version__ as version

setup(
	name="testnjyadu",
	version=version,
	description="NA",
	author="NA",
	author_email="NA",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
