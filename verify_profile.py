# -----------------------------------------------------------------------------
# Import
# -----------------------------------------------------------------------------

import re
import os
import sys
from pathlib import Path
from time import time

from fnc.extractFeature import extractFeature
from fnc.matching import matching



arguments = {}
arguments["file"] = sys.argv[1]
arguments["temp_dir"] = "./templates/Profile_Iris/"
arguments["thres"] = 0.38


def main():
    # -----------------------------------------------------------------------------
    # Execution
    # -----------------------------------------------------------------------------
    # Extract feature

    template, mask, file = extractFeature(arguments["file"])

    # Matching
    result = matching(
        template, mask, arguments["temp_dir"], arguments["thres"])

    if result == -1:

        return "No registered sample"

    elif result == 0:
        
        return "No sample matched"

    else:

        result = result[0]
        return result[:3]



if __name__ == '__main__':
    print(main())
