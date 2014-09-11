from setuptools import setup, find_packages

setup(
    name = 'go',
    version = '0.0.1',
    description = 'GO URL Shortening Service',
    long_description = open('README.md').read(),
    url = 'https://github.com/andrewvaughan/go',
    author = 'Andrew Vaughan',
    author_email = 'andrew@vaughanstudios.com',
    license = 'MIT',
    packages = find_packages(),
    include_package_data = True,
    install_requires = [
        'bottle == 0.12.7',
        'redis == 2.10.3'
    ],
    scripts = ['bin/go'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ],
    zip_safe = False
)
