from genericpath import exists
from multiprocessing.dummy import current_process
import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    # initialize a list for storing paths
    path_list_local = []

    # does path exist
    if os.path.exists(path) == False:
        print('Negative Ghostrider - file doesn\'t appear to exist')
    if os.path.isdir(path):
        for sub_path in os.listdir(path):
            cur_dir = os.path.join(path, sub_path)
            if os.path.isfile(cur_dir):
                # determine if file ends in .c
                if os.path.splitext(sub_path)[1] == '.c':
                    path_list_local.append(cur_dir)
            else:
                # if the item is a subdirectory continue down the rabbithole
                sov = find_files(suffix, cur_dir)
                if sov:
                    for element in sov:
                        path_list_local.append(element)
    return path_list_local

path_list = find_files('.c','C:\\Users\\jtjohns1\\Desktop\\testdir')
a = 1
# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

# Test Case 2

# Test Case 3
