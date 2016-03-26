命令行执行
ifconfig | awk '{if ($0 ~ ": ") printf $1;if ($0 ~ "inet ") print $2}'
执行结果为 ![ifconfig_result.png](./ifconfig_result.png)![shell_result.png](./shell_result.png)