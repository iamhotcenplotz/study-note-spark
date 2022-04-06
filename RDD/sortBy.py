import utilis

if __name__ == '__main__':
    source = utilis.create_connection()

    data = source.parallelize([('a', 1), ('b', 1), ('c', 1), ('b', 1), ('a', 1), ('a', 1)])
    rst = data.reduceByKey(lambda a, b: a + b) \
        .sortByKey(ascending=True)

    print(rst.collect())
