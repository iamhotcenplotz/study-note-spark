# Spark Study Note 
- Using Python as Programming Language

- Install PySpark
  ```shell
  pip install pyspark - i https://pypi.tuna.tsinghua.edu.cn/simple    
  ```
- Setup Python Virtual Environment
  - Specify working directory
    ```shell
     mkdir sparkPython
    ```
  - Setup virtual environment
    - call specified python version (3.9.9)
    ```shell
    /opt/modules/Python-3.9.9/python -m venv sparkPython 
    ```
    - setup pip using Tsinghua source
    ```shell
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
    ```
- Spark StandAlone Setup
  - [env](./sparkConfig/env.md)
  - [spark-defaults.conf](./sparkConfig/spark-defaults.md)
  - [workers](./sparkConfig/workers.md)
  - [spark-env.sh](./sparkConfig/spark-env.md)
  - [start up script](./sparkConfig/myspark.md)

- PySpark
  - [RDD](./RDD)
