具体脚本查看[cron_ctrl](./cron_ctrl)
因为我通常是保存一个cronfile，然后在执行crontab cronfile，这样可以有个备份，所以我的思路是：
1. 如果是执行list选项，就直接执行crontab -l将任务列出来
2. 如果是执行stop或者start选项，先检查目前处于的状态，然后根据判断自动修改cronfile，在对应的job前加#或者去掉#，然后再crontab cronfile

这样做的缺陷是可能会对不需要改变状态的其他任务会造成影响。脚本中的两个if判断就是为了尽量减少这种影响，当在cronfile中找不到相应的任务时，不执行crontab的任何命令。