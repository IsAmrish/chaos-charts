import re
import sys

# semantic version regex
regex = "^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
result = re.search(regex, sys.argv[1])

if result:
    print("version validation successful")
    sys.exit(0) # on success
else:
    print("version validation failed")
    sys.exit(1) #on failure