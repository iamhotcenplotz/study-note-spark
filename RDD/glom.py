import utilis

if __name__ == '__main__':
    source = utilis.create_connection()
    data = source.parallelize(utilis.random_data(15), 3)

    print(data.glom().collect())
    print(data.glom().flatMap(lambda x: x).collect())
