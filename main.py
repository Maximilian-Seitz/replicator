from pathlib import Path
import os

def main():
    Path('out/').mkdir(parents = True, exist_ok = True)

    codeString = """from pathlib import Path
import os

def main():
    Path('out/').mkdir(parents = True, exist_ok = True)

    codeString = \"""{}\"""

    fullCodeString = codeString.format(codeString.replace('\\\\', '\\\\\\\\').replace('\"""', '\\\\\"""'))

    outFile = open('out/main.py', 'w')
    outFile.write(fullCodeString)
    outFile.close()

if __name__ == '__main__':
    main()"""

    fullCodeString = codeString.format(codeString.replace('\\', '\\\\').replace('"""', '\\"""'))

    outFile = open('out/main.py', 'w')
    outFile.write(fullCodeString)
    outFile.close()

if __name__ == '__main__':
    main()