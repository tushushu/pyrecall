"""
@Author: tushushu
@Date: 2019-06-20 10:32:30
"""

from distutils.core import setup
from Cython.Build import cythonize


def compile_cpp11_file(file_name: str):
    """通过c++将.pyx文件编译为.so文件。

    Arguments:
        file_name {str}
    """

    ext_modules = cythonize(file_name)
    ext_modules[0].extra_compile_args.append("-std=c++11")
    ext_modules[0].extra_link_args.append("-std=c++11")
    name = file_name.split(".")[0] if "." in file_name else file_name
    setup(name=name, ext_modules=ext_modules)


def compile_file(file_name: str):
    """将.pyx文件编译为.so文件。

    Arguments:
        file_name {str}
    """

    ext_modules = cythonize(file_name)
    name = file_name.split(".")[0] if "." in file_name else file_name
    setup(name=name, ext_modules=ext_modules)


if __name__ == "__main__":
    compile_cpp11_file("_list2vector.pyx")
    compile_file("_common_elements.pyx")
    compile_cpp11_file("_common_elements_cpp.pyx")

# source activate py36
# python setup.py build_ext --inplace
