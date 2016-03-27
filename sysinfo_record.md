具体脚本内容查看[sysinfo_record](./sysinfo_record)
* 查看CPU占用命令`top|grep "Cpu"`

> eg.  `%Cpu(s):  0.7 us,  0.3 sy,  0.0 ni, 99.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st`

>us：用户态使用的cpu时间比

>sy：系统态使用的cpu时间比

>ni：用做nice加权的进程分配的用户态cpu时间比

>id：空闲的cpu时间比

>wa：cpu等待磁盘写入完成时间

>hi：硬中断消耗时间

>si：软中断消耗时间

>st：虚拟机偷取时间

* 定时任务使用 `crontab`

* 存储在`/tmp`并定时清除