from pathlib import Path

input = Path(input("Enter the file path to the to be searched folder: "))

if not input.is_dir():
    raise RuntimeError(f"The given path is not a directory and therefor can't be searched.")

for file in input.iterdir():
    if file.name[0:-4] not in ".py":
        print(file.name)