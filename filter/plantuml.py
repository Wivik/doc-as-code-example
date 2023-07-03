#!/usr/bin/env python3
import os
import sys
from pandocfilters import toJSONFilter, Para, Image
from subprocess import call
from hashlib import sha1

def plantuml(key, value, format, _):
    if key == 'CodeBlock':
        [[ident, classes, keyvals], code] = value
        if "plantuml" in classes:
            filename = sha1(code.encode(sys.getfilesystemencoding())).hexdigest() + ".png"
            if not os.path.isfile(filename):
                with open(filename[:-4], "w") as f:  # create a .uml file
                    f.write("@startuml\n")
                    f.write(code)
                    f.write("\n@enduml")
                call(["plantuml", filename[:-4]])  # convert the .uml file into a .png file
            return Para([Image([ident, [], keyvals], [], [filename, ""])])

if __name__ == "__main__":
    toJSONFilter(plantuml)
