import utilis

if __name__ == '__main__':
    source = utilis.create_connection()

    data1 = source.parallelize([(101,'1'),(102,'2'),(103,'3'),(104,'4'),(105,'5')])
    data2 = source.parallelize([(101,'1'),(102,'2'),(106,'6'),(107,'7'),(108,'8')])

    data = data1.intersection(data2)

    print(data.collect())