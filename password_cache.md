### password_cache
利用ssh-keygen -t rsa生成密钥对，执行scp ~/.ssh/id_rsa.pub user@remotehost:~/.ssh/,然后ssh连接到远程主机,cat ~/.ssh/id_rsa.pub >> authorized_keys,这样以后就可以免密码登录

修改/etc/sudoers文件，添加username ALL=(ALL)NOPASSWD:ALL,这样以后进行操作时，只需要输入sudo而不用输入密码
