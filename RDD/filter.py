import utilis
import os
import pyspark

os.environ['HADOOP_CONF_DIR'] = '/opt/modules/hadoop-3.2.2/etc/hadoop'

if __name__ == '__main__':
    conf = pyspark.SparkConf().setAppName('test-yarn').setMaster('yarn')
    source = pyspark.SparkContext(conf=conf)

    data = source.parallelize([1, 2, 3, 4, 5, 6])

    rst = data.filter(lambda x: x % 2 == 1)

    print(rst.collect())
