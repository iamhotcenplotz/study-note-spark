import pyspark
import utilis
import os

os.environ['HADOOP_CONF_DIR'] = '/opt/modules/hadoop-3.2.2/etc/hadoop'
if __name__ == '__main__':
    conf = pyspark.SparkConf().setAppName('test-yarn-test').setMaster('local[1]')
    source = pyspark.SparkContext(conf=conf)

    data = source.wholeTextFiles("hdfs:///spark_study/")
    datas = data.map(lambda x: x[1]) \
        .map(lambda x: x.replace('\n', ' ')) \
        .flatMap(lambda x: x.split(' ')) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(lambda a, b: a + b) \
        .sortByKey(ascending=True)

    print(datas.collect())
