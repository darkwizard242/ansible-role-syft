import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'syft'
PACKAGE_BINARY = "/usr/bin/syft"


def test_syft_package_installed(host):
    """
    Tests if syft package is in installed state.
    """
    assert host.package(PACKAGE).is_installed


def test_syft_binary_exists(host):
    """
    Tests if syft binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_syft_binary_file(host):
    """
    Tests if syft binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_syft_binary_which(host):
    """
    Tests the output to confirm syft's binary location.
    """
    assert host.check_output('which syft') == PACKAGE_BINARY
