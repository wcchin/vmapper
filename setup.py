from setuptools import setup

setup(
    name="vmapper",

    version="0.0.2",
    
    author="Benny Chin",
    author_email="wcchin.88@gmal.com",

    packages=['vmapper', 'vmapper.geometry', 'vmapper.geometry.templates', 'vmapper.map_element', 'vmapper.templates', 'vmapper.utils'],

    include_package_data=True,

    url="https://github.com/wcchin/vmapper",

    license="LICENSE.txt",
    description="Vector MAP ProducER - a simple python library for creating SVG map in python",

    long_description=open("README.md").read(),
    
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Scientific/Engineering :: Visualization',

         'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
    ],

    keywords='map, geography, catography, svg, ',

    install_requires=[
        "jinja2",
        "pandas",
        "geopandas",
    ],
)
