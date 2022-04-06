import utilis

if __name__ == '__main__':
    source = utilis.create_connection()

    data1 = source.parallelize([(1001,'zs'),(1002,'ls'),(1003,'ww'),(1004,'zl'),(1005,'lq')])
    data2 = source.parallelize([(1003,'devOps'),(1002,'BigData'),(1001,'Algorithm')])

    data_j = data1.join(data2)
    data_lj = data1.leftOuterJoin(data2)
    data_rj = data1.rightOuterJoin(data2)

    print(data_j.collect())
    print(data_lj.collect())
    print(data_rj.collect())
