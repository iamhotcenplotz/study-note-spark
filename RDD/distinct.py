import utilis

if __name__ == '__main__':
    source = utilis.create_connection()

    data = source.parallelize([1,2,3,4,5,6,7,7,7,8])

    rst = data.distinct().collect()

    print(rst)