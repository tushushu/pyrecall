#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author: tushushu
@Date: 2019-07-26 17:39:47
"""

import os
os.chdir(os.path.split(os.path.realpath(__file__))[0])

import sys
sys.path.append(os.path.abspath(".."))

import pandas as pd
from src.item_cf.jaccard import JaccardItemCF
from src.preprocessing.load_data import MovieRatingsData
from src.utils.utils import run_time


@run_time
def run(sparse_matrix: str):
    """读取电影评分数据，并推荐用户喜欢的电影。"""
    print("Using %s version implementation!\n" % sparse_matrix)
    # 读取数据
    movie_ratings = MovieRatingsData()
    user_col = movie_ratings.user_col
    item_col = movie_ratings.item_col
    data = movie_ratings.data
    # 训练模型
    mat_size = 20  # 用户可自定义该参数
    model = JaccardItemCF(sparse_matrix)
    model.fit(data, user_col, item_col, mat_size)
    # 生成推荐
    n_recommend = 20  # 用户可自定义该参数
    recommendation = model.predict(data, user_col, item_col, n_recommend)
    # 展示推荐结果
    print("Show recommend result (UserID, [(MovieID, Score)]):")
    pd.set_option('display.max_colwidth', 80)
    samples = recommendation.iloc[:3, :].copy()
    samples.recommendations = samples.recommendations\
        .apply(lambda x: [(y[0], round(y[1], 3))for y in x])
    print(samples.head())
    print()


def main():
    """展示推荐的性能和结果。"""
    run("python")
    run("cython")


if __name__ == "__main__":
    main()
