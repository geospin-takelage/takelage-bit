import pytest
import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_image_meta_env_exists(image_meta_data):
    assert image_meta_data['Config']['Env'] is not None


@pytest.mark.parametrize('env, value', [(0, 'DEBIAN_FRONTEND=noninteractive'),
                                        (1, 'LANG=en_US.UTF-8'),
                                        (2, 'PATH='
                                            '/usr/local/sbin:'
                                            '/usr/local/bin:'
                                            '/usr/sbin:'
                                            '/usr/bin:'
                                            '/sbin:'
                                            '/bin')])
def test_image_meta_env_values(image_meta_data, env, value):
    assert value == image_meta_data['Config']['Env'][env]


def test_image_meta_cmd(image_meta_data):
    cmd = ["/lib/systemd/systemd"]
    assert cmd == image_meta_data['Config']['Cmd']


def test_image_meta_work_dir(image_meta_data):
    assert '/root' == image_meta_data['Config']['WorkingDir']
