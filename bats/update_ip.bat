@ECHO OFF

:loop

curl --connect-timeout 2 -s -d "system_identifier={}" http://www.proxy-pool.com/proxies/

ping -n 2 127.0.0.1 >nul

goto loop
