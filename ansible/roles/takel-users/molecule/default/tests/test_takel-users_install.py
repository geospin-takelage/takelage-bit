import testaid

testinfra_hosts = testaid.hosts()


def test_takel_users_install_deb_packages_installed(host, testvars):
    install_packages = testvars['takel_users_deb_install_packages']

    for install_package in install_packages:
        package = host.package(install_package)

        assert package.is_installed
