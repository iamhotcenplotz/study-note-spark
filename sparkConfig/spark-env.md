# spark-env.sh Setup

```shell
JAVA_HOME=/opt/modules/jdk1.8.0_211
HADOOP_CONF_DIR=/opt/modules/hadoop-3.2.2/etc/hadoop
YARN_CONF_DIR=/opt/modules/hadoop-3.2.2/etc/hadoop
export SPARK_MASRER_HOST=server1
export SPARK_MASTER_PORT=7077
SPARK_MASTER_WEBUI_PORT=8080
SPARK_WORKER_CORES=1
SPARK_WORKER_MEMORY=1g
SPARK_WORKER_PORT=7078
SPARK_WORKER_WEBUI_PORT=8081
SPARK_HISTORY_OPTS="-Dspark.history.fs.logDirectory=hdfs://server1:8020/sparklog/  -Dspark.history.fs.cleaner.enabled=true"
```