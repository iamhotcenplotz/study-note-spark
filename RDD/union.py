import utilis

if __name__ == '__main__':
    source = utilis.create_connection()

    data1 = source.parallelize([1,2,3,4,5])

    data2 = source.parallelize([6,7,8,9,10])

    data = data1.union(data2)

    print(data.collect())