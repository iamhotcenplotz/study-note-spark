import pyspark
import utilis

if __name__ == '__main__':
    source = utilis.create_connection()

    data = source.parallelize([('a', 1), ('b', 1), ('c', 1), ('b', 1), ('a', 1), ('a', 1)])

    rst = data.groupBy(lambda t: t[0]).map(lambda k:(k[0],list(k[1])))
    print(rst.collect())
