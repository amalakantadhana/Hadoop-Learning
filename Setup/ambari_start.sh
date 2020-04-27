#!/bin/bash
echo "Attempting to start the Mysqlserver"
/etc/init.d/mysqld start
if [ $?==0 ]
then
  ambari-server start
else
    echo " start of mysql server failed "
    exit 1
fi