datetime: 2017/1/14 13:48
Author: shaoyan

## 需求说明
#### 问题情景
服务器上，有几百个网站。现在是每个域名对应的配置、网站目录是没有规律的。

#### 需求只有三点：
- 1.是创建目录结构为：主域名/子域名前缀，用来存放对应子域名的网站文件
- 2.给每个域名构造一个虚拟主机配置，该配置文件包含该域名所有的子域名配置。
- 3.复制原来的网站文件，到相应的子域名目录下。

假设有域名：
```
xsy.me
www.xsy.me
www.abc.xsy.me
```

则需要生成目录为：
```
xsy.me/aite
xsy.me/www
xsy.me/www.abc
```

域名配置为：`xsy.me.conf`
```
server {
    listen       80;
    server_name xsy.me;
    root /server/www/xsy.me/aite;
    index index.html index.htm index.php;
    
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   html;
    }
    include enable-php.conf;
}
server {
    listen       80;
    server_name www.xsy.me;
    root /server/www/xsy.me/www;
    index index.html index.htm index.php;
    
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   html;
    }
    include enable-php.conf;
}
server {
    listen       80;
    server_name www.abc.xsy.me;
    root /server/www/xsy.me/www.abc;
    index index.html index.htm index.php;
    
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   html;
    }
    include enable-php.conf;
}
```

还有需要复制原有的文件到，新的目录路径下。

## 思路
- 使用 grep 命令，过滤出域名行，存到 domain.md 文件。使用查找替换的方法，去掉多余的，仅留域名，像下面：
```
yaqsm.com
www.yaqsm.com
www.fs.yaqsm.com
www.yaqdddsm.com
www.fs.yaaasm.com
```

- 使用 grep 命令，过滤出网站目录行,使用查找替换的方法，去掉多余的，仅留目录行。注意不要弄乱了，域名和目录行是刚好对上的。
```
www/jianfei2_v2
www/jjtutou
www/ganfa5.com/zf1
www/jjtutou
www/ganfa5.com/zf1
```

- 将域名、目录文件，通过字符串拆分，存成列表、字典。方便操作

#### 文件说明：
- 当前目录下的`www`目录是测试用的：原有网站目录文件
- `domain.md`是测试域名
- `root_path.md`是测试用的路径