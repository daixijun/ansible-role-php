daixijun.php
=========

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/aa8233b02123488a88257f76908967f4)](https://app.codacy.com/app/daixijun/ansible-role-php?utm_source=github.com&utm_medium=referral&utm_content=daixijun/ansible-role-php&utm_campaign=Badge_Grade_Settings)
[![Build Status](https://github.com/daixijun/ansible-role-php/workflows/ci/badge.svg)](https://github.com/daixijun/ansible-role-php/actions)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-daixijun.php-660198.svg?style=flat)](https://galaxy.ansible.com/daixijun/ansible-role-php/)
[![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/daixijun/ansible-role-php?sort=semver)](https://github.com/daixijun/ansible-role-php/tags)

Ansible 源码安装php

Requirements
------------

* RHEL/Centos 7
* Ansible 2.5+
* php 7.1+

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
