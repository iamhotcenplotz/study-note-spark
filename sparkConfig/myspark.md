# Spark StandAlone Start Up Script

```shell
#!/bin/bash

if [$# -lt 1]
then
        echo "~ No Args Input ..."
        exit;
fi

case $1 in
"start")
        echo "==================== Start Spark StandAlone ===================="
        echo "-------------------- start master --------------------"
        ssh server1 "/opt/modules/spark-3.2.1/sbin/start-master.sh"
        echo "-------------------- start server1 worker --------------------"
        ssh server1 "/opt/modules/spark-3.2.1/sbin/start-worker.sh spark://server1:7077"
        echo "-------------------- start server2 worker --------------------"
        ssh server2 "/opt/modules/spark-3.2.1/sbin/start-worker.sh spark://server1:7077"
        echo "-------------------- start server3 worker--------------------"
        ssh server3 "/opt/modules/spark-3.2.1/sbin/start-worker.sh spark://server1:7077"
        echo "-------------------- start history server--------------------"    
        ssh server1 "/opt/modules/spark-3.2.1/sbin/start-history-server.sh"
;;
"stop")
        echo "==================== Stop Spark StandAlone===================="
        echo "-------------------- stop server3 worker --------------------"
        ssh server3 "/opt/modules/spark-3.2.1/sbin/stop-worker.sh"
        echo "-------------------- stop server2 worker --------------------"
        ssh server2 "/opt/modules/spark-3.2.1/sbin/stop-worker.sh"
        echo "-------------------- stop server1 worker --------------------"
        ssh server1 "/opt/modules/spark-3.2.1/sbin/stop-worker.sh"
        echo "-------------------- stop master --------------------"
        ssh server1 "/opt/modules/spark-3.2.1/sbin/stop-master.sh"
        echo "-------------------- stop history server--------------------"    
        ssh server1 "/opt/modules/spark-3.2.1/sbin/stop-history-server.sh"
;;
*)
        echo "Input Args Error"
;;
esac
```

## Note
- to start HistoryServer, hadoop cluster must be on.