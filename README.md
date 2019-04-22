Role Name
=========

[![Build Status](https://travis-ci.org/daixijun/ansible-role-php.svg?branch=master)](https://travis-ci.org/daixijun/ansible-role-php)

Ansible 源码安装php

Requirements
------------

* RHEL/Centos 7
* Ansible 2.5+

Role Variables
--------------

[default vars](defaults/main.yml)

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: daixijun.php
      php_version: 7.2.17
```

License
-------

BSD

Author Information
------------------

Xijun Dai <daixijun1990@gmail.com>
