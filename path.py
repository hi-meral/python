from pathlib import Path

path = Path()


for file in path.glob('pattern*'):
    print(file)
