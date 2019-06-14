#how to work with directories in python
from pathlib import Path
#absolute Path
#relative Path
path=Path()
#below line is used to check all the py files in directory
#print(path.glob('*.py'))
for file in path.glob('*.py'):
    print(file)
#below line is used to check all the files in directory
for file in path.glob('*'):
    print(file)