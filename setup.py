from setuptools import setup, find_packages
import versioneer

setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "canalyse=canalyse.cli:cli",
        ]
    },
)
