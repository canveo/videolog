from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = ''.join(f.readlines())

setup(
    name = 'videolog',
    version = '0.1',
    description = 'Video watch history tracker and archiver. Developed with YouTube.',
    long_description = long_description,
    author = 'Petr Schmied',
    author_email = 'contact@petrschmied.com',
    keywords = 'watch history log track random archive YouTube',
    license = 'MIT',
    url = 'https://github.com/JBlackN/videolog',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Programming Language :: JavaScript',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Video',
        'Topic :: Multimedia :: Video :: Display',
        'Topic :: Software Development',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: System :: Archiving',
        'Topic :: System :: Archiving :: Backup',
        'Topic :: System :: Archiving :: Compression',
        'Topic :: System :: Archiving :: Mirroring',
        'Topic :: System :: Archiving :: Packaging',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Markup',
        'Topic :: Utilities',
    ],
    zip_safe = False,

    packages = find_packages(),
    package_data = {
        'videolog': ['static/css/*.css', 'static/js/*.js', 'templates/*.html']
    },

    entry_points = {
        'console_scripts': [
            'videolog = videolog.cli:main'
        ]
    },

    install_requires = [
        'click', 'requests', 'flask', 'google-api-python-client',
        'google-auth-httplib2', 'google-auth-oauthlib', 'google-auth'
    ],
    setup_requires = ['pytest-runner'],
    tests_require = ['pytest', 'flexmock']
)
