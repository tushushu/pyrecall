"""
@Author: tushushu
@Date: 2019-06-20 14:34:24
"""

"""
结论：函数list2vector_1更快。

***************************************************************************
对比list2vector_1函数和list2vector_2函数的性能...

---------------------------------------------------------------------------
长度为100的数组!

函数list2vector_1运行--10000次!
累计运行时间为--0.030 s!

函数list2vector_2运行--10000次!
累计运行时间为--0.035 s!

---------------------------------------------------------------------------
---------------------------------------------------------------------------
长度为1000的数组!

函数list2vector_1运行--10000次!
累计运行时间为--0.090 s!

函数list2vector_2运行--10000次!
累计运行时间为--0.227 s!

---------------------------------------------------------------------------
---------------------------------------------------------------------------
长度为10000的数组!

函数list2vector_1运行--10000次!
累计运行时间为--0.664 s!

函数list2vector_2运行--10000次!
累计运行时间为--2.086 s!

---------------------------------------------------------------------------
***************************************************************************
"""

import os
os.chdir(os.path.split(os.path.realpath(__file__))[0])

import sys
sys.path.append(os.path.abspath("."))

from _list2vector import list2vector_1, list2vector_2
import array


def test(n_elements: int):
    """对比list2vector_1函数和list2vector_2函数的性能。

    Arguments:
        n_elements {int} -- 数组的长度。
    """
    print("---------------------------------------------------------------------------")
    print("长度为%d的数组!\n" % n_elements)

    arr1 = list(range(n_elements))
    arr2 = array.array('i', arr1)

    list2vector_1(arr1)
    list2vector_2(arr2)
    print("---------------------------------------------------------------------------")

if __name__ == "__main__":
    print("***************************************************************************")
    print("对比list2vector_1函数和list2vector_2函数的性能...\n")
    test(100)
    test(1000)
    test(10000)
    print("***************************************************************************")
