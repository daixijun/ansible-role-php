# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

### [0.2.2](https://github.com/daixijun/ansible-role-php/compare/v0.2.1...v0.2.2) (2020-04-21)


### Features

* 添加 php 安装包 checksum 支持 ([e5528d0](https://github.com/daixijun/ansible-role-php/commit/e5528d048603db7aca28db325a0c2f33379f3e9d))


### Bug Fixes

* 修复目录权限幂等性问题 ([14ac388](https://github.com/daixijun/ansible-role-php/commit/14ac38874d6ea3ed08f7e4681fbc97cc6ee68273))
* **php:** 添加 pm.max_children 默认值计算公式 ([75ab907](https://github.com/daixijun/ansible-role-php/commit/75ab9079c6474d7581e1c3a25f99029de361f324))
* 修复 libzip 目录权限 ([ab4125c](https://github.com/daixijun/ansible-role-php/commit/ab4125cffc724c27919840d70adc33b6b555fde7))
* 修改安装包存放路径 ([f0db6e1](https://github.com/daixijun/ansible-role-php/commit/f0db6e11857b8421bb1ed905e133334088163918))

### [0.2.1](https://github.com/daixijun/ansible-role-php/compare/v0.2.0...v0.2.1) (2020-03-30)


### Bug Fixes

* refresh ansible_local facts ([7090c34](https://github.com/daixijun/ansible-role-php/commit/7090c34ca2aab122487adeb05f4a9f49c8343c81))

## [0.2.0](https://github.com/daixijun/ansible-role-php/compare/v0.1.22...v0.2.0) (2020-03-30)


### ⚠ BREAKING CHANGES

* 不会再移除安装失败的版本

### Features

* 升级默认php版本为 7.3.13, 升级默认 libzip 版本为 1.6.1 ([bc9aadc](https://github.com/daixijun/ansible-role-php/commit/bc9aadcee748a09eb5992e49b412d48e31280bce))
* 添加本地facts ([308addc](https://github.com/daixijun/ansible-role-php/commit/308addc658de9480e38b7640d677332daad7c6ce))


### Bug Fixes

* 不再移除安装失败的版本 ([b648a71](https://github.com/daixijun/ansible-role-php/commit/b648a71ca243104f029d5a0ec28481c700d5adce))
* 修复php安装包下载地址为sohu镜像站 ([29cd333](https://github.com/daixijun/ansible-role-php/commit/29cd3334e62451b539ea2d55a5f8261d241e256c))
* 修改local facts格式为json ([d4b79b9](https://github.com/daixijun/ansible-role-php/commit/d4b79b9775fd5b72205016719461dd9cac354546))
* 修改local facts格式为json ([4999516](https://github.com/daixijun/ansible-role-php/commit/49995165de1c9ff23ac502e1143c03e0e36f4b01))

### [0.1.22](https://github.com/daixijun/ansible-role-php/compare/v0.1.21...v0.1.22) (2020-01-05)


### Bug Fixes

* 修改下载逻辑 ([20dff53](https://github.com/daixijun/ansible-role-php/commit/20dff538b6137418a2ae71a93db8883b8a2323eb))

### [0.1.21](https://github.com/daixijun/ansible-role-php/compare/v0.1.20...v0.1.21) (2020-01-04)


### Features

* 延长依赖安装时间 ([2606ff4](https://github.com/daixijun/ansible-role-php/commit/2606ff4ef93c51a0cfb56a28397beb42f4c05584))

### [0.1.20](https://github.com/daixijun/ansible-role-php/compare/v0.1.19...v0.1.20) (2020-01-04)


### Bug Fixes

* 安装包不存在且php未安装时才下载 ([8f27320](https://github.com/daixijun/ansible-role-php/commit/8f27320dcedfbeb93ebf92d30fce89fa801438be))

### [0.1.19](https://github.com/daixijun/ansible-role-php/compare/v0.1.18...v0.1.19) (2020-01-04)


### Features

* 修改安装包下载逻辑 ([fb941b1](https://github.com/daixijun/ansible-role-php/commit/fb941b10ed95bf1c8d2ca06c8ee5425b95872423))

### [0.1.18](https://github.com/daixijun/ansible-role-php/compare/v0.1.17...v0.1.18) (2019-11-28)


### Bug Fixes

* 修改 php_fpm_pid 默认路径为 /var/run/php-fpm.pid ([bf18b35](https://github.com/daixijun/ansible-role-php/commit/bf18b355396bc55746557955753304c8f624f847))

### [0.1.17](https://github.com/daixijun/ansible-role-php/compare/v0.1.16...v0.1.17) (2019-11-27)


### Features

* 添加 --enable-pcntl 参数 ([b6ac07b](https://github.com/daixijun/ansible-role-php/commit/b6ac07bc20e5826316fab904d5c14e35488e4d49))

### [0.1.16](https://github.com/daixijun/ansible-role-php/compare/v0.1.15...v0.1.16) (2019-11-20)


### Bug Fixes

* 为 session.save_path 添加引号,防止变量解析错误 ([d76b0e5](https://github.com/daixijun/ansible-role-php/commit/d76b0e515458dc556e3f5d5a5e05d8be466166a6))

### [0.1.15](https://github.com/daixijun/ansible-role-php/compare/v0.1.14...v0.1.15) (2019-11-20)


### Bug Fixes

* 修复libzip判断逻辑 ([48155aa](https://github.com/daixijun/ansible-role-php/commit/48155aae9ef6ea106f9b5e16f60ee6a7ff62df86))

### [0.1.14](https://github.com/daixijun/ansible-role-php/compare/v0.1.13...v0.1.14) (2019-11-20)


### Bug Fixes

* 添加libzip安装状态检查 ([fc153fd](https://github.com/daixijun/ansible-role-php/commit/fc153fd5a3844b465278a3f27cfdafc5fa5187c0))

### [0.1.13](https://github.com/daixijun/ansible-role-php/compare/v0.1.12...v0.1.13) (2019-09-14)

### [0.1.12](https://github.com/daixijun/ansible-role-php/compare/v0.1.11...v0.1.12) (2019-08-28)


### Bug Fixes

* 修复配置文件路径错误 ([e647654](https://github.com/daixijun/ansible-role-php/commit/e647654))
