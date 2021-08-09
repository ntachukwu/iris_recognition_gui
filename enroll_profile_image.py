#!/bin/sh
import os, sys
from fnc.extractFeature import extractFeature
from multiprocessing import cpu_count, Pool
from scipy.io import savemat
from time import time
from tqdm import tqdm
from glob import glob

import argparse



arguments = {}
arguments["data_file"] = sys.argv[1]
arguments["temp_dir"] = "./templates/Profile_Iris/"
arguments["n_cores"] = cpu_count()



def pool_func(file):
    template, mask, _ = extractFeature(file, use_multiprocess=False)
    basename = os.path.basename(file)
    out_file = os.path.join(arguments["temp_dir"], "%s.mat" % (basename))
    savemat(out_file, mdict={'template': template, 'mask': mask})
    return basename


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
    # files = glob(os.path.join(arguments["data_file"],
    #                           "**/*/*_1_*.jpg"), recursive=True)
    file = arguments["data_file"]
    # print("Number of files for enrolling:", n_files)

    # Parallel pools to enroll templates
    # print("Start enrolling...")
    # pools = Pool(processes=arguments["n_cores"])
    # for _ in tqdm(pools.imap_unordered(pool_func, files), total=n_files):
    #     pass

    pool_return = pool_func(file)
    return pool_return


if __name__ == '__main__':

    print(main())
