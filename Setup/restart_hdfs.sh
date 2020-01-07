echo "Restarting hdfs compponents"
echo "restarting journal mode"
su -l hdfs -c "/usr/hdp/current/hadoop-hdfs-journalnode/../hadoop/sbin/hadoop-daemon.sh stop journalnode"
echo "journal node started successfully"

echo "Restarting the Namenode Service"
su -l hdfs -c "/usr/hdp/current/hadoop-hdfs-namenode/../hadoop/sbin/hadoop-daemon.sh start namenode"
echo "namenode started successfully"

echo "Restarting secondary node"
su -l hdfs -c "/usr/hdp/current/hadoop-hdfs-namenode/../hadoop/sbin/hadoop-daemon.sh start secondarynamenode"
echo "Secondary name node started successfully"

echo "restarting all datanodes"
su -l hdfs -c "/usr/hdp/current/hadoop-hdfs-datanode/../hadoop/sbin/hadoop-daemon.sh start datanode"
echo "All datanodes started successfully"
echo "hdfs restarted successfully"
