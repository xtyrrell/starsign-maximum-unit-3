from pathlib import Path

print("Runing Python script")

mydir = Path("/Users/ruby/Documents/2022/VideoGame/code/layout-and-printing-2/printing/watched-files-to-print")
for file in mydir.glob('*.pdf'):
    print(file.name)
