from mmap import mmap
from pathlib import Path
from argparse import ArgumentParser, Namespace
from typing import Tuple

def replace_occurrences(f: Path | str, search: bytes, replacement: bytes) -> Tuple[bool, int, list]:
    if len(search) != len(replacement):
        raise ValueError("search and replacement must be the same length")

    found = False
    times = 0
    positions = []

    with open(f, "r+b") as fd:
        mm = mmap(fd.fileno(), 0)
        while (pos := mm.find(search)) > -1:
            found = True
            times += 1
            positions.append(pos)
            
            fd.seek(pos)
            fd.write(replacement)
    
    return found, times, positions
            
def main(args: Namespace) -> None:
    p = Path(args.path)
    
    if args.unpatch:
        search = b"<exclude> 39 76    </exclude>"
        replace = b"<exclude> 39 76 77 </exclude>"
    else:
        search = b"<exclude> 39 76 77 </exclude>"
        replace = b"<exclude> 39 76    </exclude>"
    
    try:
        found, times, positions = replace_occurrences(p, search, replace)
        if found:
            print(f"Found {times} occurrences at {positions}")
        else:
            print("Did not find any occurrences. Is this patched already?")
    except:
        print("Failed to patch file. Was it dumped correctly?")
    
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-p', '--path', type=str, required=True,
                        help="path to modem.img")
    parser.add_argument('-u', '--unpatch', action="store_true",
                        help="unpatch modem")
    args = parser.parse_args()

    main(args)    
