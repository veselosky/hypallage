from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys
import os.path
from hypallage import __version__


class PyTest(TestCommand):
    """Command class to allow `setup.py test` to run py.test.

    http://pytest.org/latest/goodpractises.html#integration-with-setuptools-distribute-test-commands
    """
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

readme = os.path.join(os.path.dirname(__file__), 'README.rst')
with open(readme) as thefile:
    README = thefile.read()

setup(
    name="hypallage",
    version=__version__,
    packages=find_packages(),
    author="Vince Veselosky",
    author_email="vince@veselosky.com",
    description="",
    long_description=README,
    license="MIT",
    url="",
    # could also include download_url, classifiers, etc.

    install_requires=[
        'beautifulsoup4',
    ],
    tests_require=[
        'pytest',
    ],
    cmdclass={'test': PyTest},
)
