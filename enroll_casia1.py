# -----------------------------------------------------------------------------
# Import
# -----------------------------------------------------------------------------

#!/bin/sh
import os
from fnc.extractFeature import extractFeature
from multiprocessing import cpu_count, Pool
from scipy.io import savemat
from time import time
from tqdm import tqdm
from glob import glob

import argparse


# ------------------------------------------------------------------------------
#	Argument parsing
# # ------------------------------------------------------------------------------
# parser = argparse.ArgumentParser()

# parser.add_argument("--data_dir", type=str, default="../CASIA1/",
#                     help="Path to the directory containing CASIA1 images.")

# parser.add_argument("--temp_dir", type=str, default="./templates/CASIA1/",
#                     help="Path to the directory containing templates.")

# parser.add_argument("--n_cores", type=int, default=cpu_count(),
#                     help="Number of cores used for enrolling template.")

# args = parser.parse_args()

arguments = {}
arguments["data_dir"] = "./CASIA1/"
arguments["temp_dir"] = "./templates/CASIA1/"
arguments["n_cores"] = cpu_count()
# -----------------------------------------------------------------------------
# Pool function
# -----------------------------------------------------------------------------


def pool_func(file):
    template, mask, _ = extractFeature(file, use_multiprocess=False)
    basename = os.path.basename(file)
    out_file = os.path.join(arguments["temp_dir"], "%s.mat" % (basename))
    savemat(out_file, mdict={'template': template, 'mask': mask})


def main():
    # -----------------------------------------------------------------------------
    # Execution
    # -----------------------------------------------------------------------------
    start = time()

    # Check the existence of temp_dir
    if not os.path.exists(arguments["temp_dir"]):
        print("makedirs", arguments["temp_dir"])
        os.makedirs(arguments["temp_dir"])

    # Get list of files for enrolling template, just "xxx_1_x.jpg" files are selected
    files = glob(os.path.join(arguments["data_dir"],
                              "**/*/*_1_*.jpg"), recursive=True)
    files = files
    n_files = len(files)
    # print("Number of files for enrolling:", n_files)

    # Parallel pools to enroll templates
    print("Start enrolling...")
    pools = Pool(processes=arguments["n_cores"])
    for _ in tqdm(pools.imap_unordered(pool_func, files), total=n_files):
        pass

    end = time()
    print('\n>>> Enrollment time: {} [s]\n'.format(end-start))
    return n_files, end - start


if __name__ == '__main__':
    import django

    django.setup()
    from gui.models import EnrollModel

    name = "CASIA1"
    no_files, execution_time = main()
    new_model = EnrollModel(name=name, no_files=no_files,
                            enrollment_time=execution_time)
    new_model.save()
