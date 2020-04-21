# daixijun.php

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/aa8233b02123488a88257f76908967f4)](https://app.codacy.com/app/daixijun/ansible-role-php?utm_source=github.com&utm_medium=referral&utm_content=daixijun/ansible-role-php&utm_campaign=Badge_Grade_Settings)
[![Build Status](https://github.com/daixijun/ansible-role-php/workflows/build/badge.svg)](https://github.com/daixijun/ansible-role-php/actions)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-daixijun.php-660198.svg?style=flat)](https://galaxy.ansible.com/daixijun/ansible-role-php/)
[![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/daixijun/ansible-role-php?sort=semver)](https://github.com/daixijun/ansible-role-php/tags)

Ansible 源码安装php

## 环境要求

* RHEL/Centos 7.x
* Ansible 2.9+
* php 7.1+

## 变量

[default vars](defaults/main.yml)

## 依赖

无依赖

## 使用示例

```yaml
- hosts: servers
  roles:
    - role: daixijun.php
      php_version: 7.2.17
```

## 已知问题

* libzip 1.4以上版本需要 CMake 3.0以上才能编译，Centos7 默认CMake版本为2.8，暂时最高支持 libzip 版本为1.3.2
* php 7.4 以上的版本暂时不支持

## License

BSD

## 维护者

* Xijun Dai <daixijun1990@gmail.com>
