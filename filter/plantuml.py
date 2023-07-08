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
            base_filename = sha1(code.encode(sys.getfilesystemencoding())).hexdigest()
            plantuml_filename = base_filename + ".puml"
            png_filename = base_filename + ".png"
            if not os.path.isfile(png_filename):
                with open(plantuml_filename, "w") as f:  # create a .uml file
                    f.write("@startuml\n")
                    f.write(code)
                    f.write("\n@enduml")
                call(["plantuml", plantuml_filename])  # convert the .uml file into a .png file
            return Para([Image([ident, [], keyvals], [], [png_filename, ""])])

if __name__ == "__main__":
    toJSONFilter(plantuml)
