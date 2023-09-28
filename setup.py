from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tea/__init__.py
from tea import __version__ as version

setup(
	name="tea",
	version=version,
	description="test",
	author="naveen",
	author_email="naveen",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
