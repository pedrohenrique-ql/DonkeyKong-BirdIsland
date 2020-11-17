from setuptools import setup, find_packages
 
setup(
    name="dk-birdisland",
    version="0.1",
    author="Murilo Castro",
    author_email="murilo.castro@ccc.ufcg.edu.br",
    description="DK, T-rex style",
    url="https://github.com/Murilo-Gruppi/DonkeyKong-BirdIsland",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=['pygame>=2.0'],
    entry_points={
        'console_scripts': [
            'dk-birdisland=dk-birdisland.main:game'
            ]
        }
)

