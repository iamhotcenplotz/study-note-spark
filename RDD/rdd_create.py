import random
import pyspark


def create_connection():
    conf = pyspark.SparkConf().setAppName('test').setMaster('local[1]')
    sc = pyspark.SparkContext(conf=conf)
    return sc


def random_data(size):
    rst = list()
    for i in range(size):
        rst.append(random.randint(i, i + 100))
    return rst


if __name__ == '__main__':
    # Step 1 : Initialization
    source = create_connection()

    # Step 2 : create rdd dataset
    data1 = random_data(12)
    rdd = source.parallelize(data1, numSlices=3)
    print(rdd.getNumPartitions())
    print(rdd.collect())

    # load hdfs file
    data2 = source.textFile("hdfs:///spark_study/txt1.txt",minPartitions=3)
    print(data2.getNumPartitions())
    print(data2.collect())

    # load local file

    data3 = source.textFile('file:/home/hadoop/spark_study/txt1.txt',minPartitions=3)



