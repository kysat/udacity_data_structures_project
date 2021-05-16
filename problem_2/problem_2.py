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
    return sorted(walk_and_find_files(suffix, path, list()))


def walk_and_find_files(suffix, path, found_file_list):
    file_list = os.listdir(path)
    parent = path
    for file_or_directory in file_list:
        if os.path.isdir(os.path.join(parent, file_or_directory)):
            walk_and_find_files(suffix, os.path.join(parent, file_or_directory), found_file_list)
        elif file_or_directory.endswith(suffix):
            found_file_list.append(os.path.join(parent, file_or_directory))
    return found_file_list

print(find_files('.c', '.'))
