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


# ------------------------------------------------------------------------------
#	Argument parsing
# ------------------------------------------------------------------------------
# parser = argparse.ArgumentParser()

# parser.add_argument("--file", type=str,
#                     help="Path to the file that you want to verify.")

# parser.add_argument("--temp_dir", type=str, default="./templates/",
#                     help="Path to the directory containing templates.")

# parser.add_argument("--thres", type=float, default=0.38,
#                     help="Threshold for matching.")

# args = parser.parse_args()
arguments = {}
arguments["file"] = sys.argv[1]
arguments["temp_dir"] = "./templates/CASIA1/"
arguments["thres"] = 0.38


def main():
    # -----------------------------------------------------------------------------
    # Execution
    # -----------------------------------------------------------------------------
    # Extract feature
    return_value = {}
    start = time()
    # print('>>> Start verifying {}\n'.format(arguments["file"]))
    template, mask, file = extractFeature(arguments["file"])

    # Matching
    result = matching(template, mask, arguments["temp_dir"], arguments["thres"])


    if result == -1:
        # print('>>> No registered sample.')
        return_value["error"] = "No registered sample"
        return return_value

    elif result == 0:
        # print('>>> No sample matched.')
        return_value["error"] = "No sample matched"
        return return_value

    else:
        # print('>>> {} samples matched (descending reliability):'.format(len(result)))
        positive_results=[]
        positive_results_path=[]
        for res in result:
            # print("\t", res)
            positive_results.append(res)



            # To return the path to the original file
            reg_pattern=re.compile(res[:-4] + '$')
            for root, dirs, files in os.walk(os.path.abspath("./")):
                for file in files:
                    if reg_pattern.match(file):
                        filepath=os.path.join(root, file)
                        # print("\t", "Path to original Image: ",
                            # filepath)
                        positive_results_path.append(filepath)



    # Time measure
    end=time()
    # print('\n>>> Verification time: {} [s]\n'.format(end - start))
    return_value["number_of_results"]=len(result)
    return_value["positive_results"]=positive_results
    return_value["positive_results_path"]=positive_results_path
    return_value["verification_time"]= end - start
    return return_value

if __name__ == '__main__':
    print(main())
