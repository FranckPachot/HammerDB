#!/bin/tclsh
# maintainer: Pooja Jain
import os
tmpdir = os.getenv('TMP')

print("SETTING CONFIGURATION")
dbset('db','mssqls')
dbset('bm','TPC-C')


diset('connection','mssqls_server','(local)')
diset('connection','mssqls_authentication','windows')
diset('connection','mssqls_odbc_driver','"ODBC Driver 18 for SQL Server"')
diset('connection','mssqls_encrypt_connection','true')
diset('connection','mssqls_trust_server_cert','true')

diset('tpcc','mssqls_dbase','tpcc')
diset('tpcc','mssqls_driver','timed')
diset('tpcc','mssqls_total_iterations','10000000')
diset('tpcc','mssqls_rampup','2')
diset('tpcc','mssqls_duration','5')
diset('tpcc','mssqls_allwarehouse','true')
diset('tpcc','mssqls_timeprofile','true')
diset('tpcc','mssqls_checkpoint','true')

loadscript()
print("TEST STARTED")
vuset('vu','vcpu')
vucreate()
tcstart()
tcstatus()
jobid = tclpy.eval('vurun')
vudestroy()
tcstop()
print("TEST COMPLETE")
file_path = os.path.join(tmpdir , "mssqls_tprocc" )
fd = open(file_path, "w")
fd.write(jobid)
fd.close()
exit()
