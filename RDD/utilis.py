import random
import pyspark


def create_connection():
    conf = pyspark.SparkConf().setAppName('test').setMaster('local[*]')
    sc = pyspark.SparkContext(conf=conf)
    return sc


def random_data(size):
    rst = list()
    for i in range(size):
        rst.append(random.randint(i, i + 100))
    return rst
