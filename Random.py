from pathlib import Path

path=Path("Random_p") # to check file exist in system.
print(path.exists())

#path = Path("PC") # To create a directory
#print(path.mkdir())

#Path("PC")# To delete directory
#print(path.rmdir())

#To find all files in all direectories.

path = Path()
for file in path.glob('*.py'):
    print(file)