try:
    # Try to do something.
except:
    # if anything fails in try, execute here
else:
    # if nothing fails in try, execute here.

from pathlib import Path
filepath = Path("rockyou.txt")

filecontents = file.read_text()
lines = filecontents.splitlines()
print(lines)
