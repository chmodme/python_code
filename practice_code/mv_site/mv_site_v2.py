#!/usr/bin/env python3
# author: shaoyan

import os
import shutil


def mv_site():
    """
    复制文件，创建目录，构造配置参数
    :return:
    """
    with open('root_path.md', 'r') as p:    # 打开老的路径配置
        p_data = p.read()
        p_list = p_data.split('\n')

    with open('domain.md','r') as d:    # 打开域名文件
        d_list = []
        for line in d:
            d_list_tmp = line.split('\n')
            d_list_tmp2 = d_list_tmp[0].split('.')
            d_list.append(d_list_tmp2)      # 拆分域名
    count = 0
    for item in d_list:
        i = len(item)
        if i < 3 :
            qian_zhui = 'aite'
            domain_name = '.'.join(item[0:i])
        else:
            qian_zhui = '.'.join(item[0:i - 2])
            domain_name = '.'.join(item[i - 2:i])
        # 复制文件，会创建指定目录
        mk_path = domain_name + '/' + qian_zhui
        old_root_path = p_list[count]
        shutil.copytree(old_root_path, mk_path)
        count += 1
        # 构建配置 ，{域名：前缀列表}
        domain_list_name = []  # [域名列表]
        domain_dict = {}
        if domain_name not in domain_list_name:
            domain_list_name.append(domain_name)
            domain_dict[domain_name] = []
        domain_dict_value_temp = domain_dict[domain_name]
        domain_dict_value_temp.append(qian_zhui)
        domain_dict[domain_name] = domain_dict_value_temp
        vhost_conf(domain_dict)


def vhost_conf(domain_dict):
    """
    遍历字典，二层遍历字典值列表，将列表元素，构造成子域名，生成配置
    追加写入配置文件
    """
    for key in domain_dict:
        for qian_zhui_new in domain_dict[key]:
            domain_name_new = qian_zhui_new + '.' + key
            root_path = key + '/' + qian_zhui_new
            conf_tmp = """server {
    listen       80;
    server_name %s;
    root /server/www/%s;
    index index.html index.htm index.php;

    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   html;
    }
    include enable-php.conf;
}
""" % (domain_name_new, root_path)
            print(key)
            domain_conf = key + '.conf'
            print(os.path.exists(domain_conf))
            if os.path.exists(domain_conf):     # 配置文件存在，则追加
                with open(domain_conf, 'a+') as v:
                    v.write(conf_tmp)
            else:
                with open(domain_conf, 'w+') as v:      # 配置文件不存在，则创建并添加
                    v.write(conf_tmp)

mv_site()