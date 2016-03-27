具体脚本查看[socks_proxy](./socks_proxy)和[socks_proxy_secret](./socks_proxy_secret)

对[socks_proxy](./socks_proxy)执行 chmod +x socks_proxy 赋予可执行权限即可。

该脚本的缺陷是密码、帐号及主机名称都在脚本可以看到，缺乏一定的安全，为避免这样情况，可以使用[socks_proxy_secret](./socks_proxy_secret),不过这个脚本在每次执行时都需要需要密码、帐号以及主机IP
