from setuptools import setup, find_packages

setup(
  name="terminal_game_MI0",
  version="1.0.3",
  description="Terminal-scape is a terminal-based game.",
  long_description="Terminal-scape is a terminal-based game that engages programmers or any command line user during leisure time.",
  long_description_content_type="text/markdown",
  url="https://github.com/ImaledoShalom101/Terminal-scape",
  author="Imaledo David",
  author_email="shalomimaledo@gmail.com",
  packages=find_packages(),
  install_requires=[],
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  entry_points={
    'console_scripts': [
      'tgmi = terminal-scape.Terminal_game:commence',
    ]
  },
)
