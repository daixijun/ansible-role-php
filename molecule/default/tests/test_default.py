import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_running_and_enabled(host):
    srv = host.service('php-fpm')

    assert srv.is_running
    assert srv.is_enabled


def test_listening(host):
    s = host.socket('tcp://127.0.0.1:9000')

    assert s.is_listening
