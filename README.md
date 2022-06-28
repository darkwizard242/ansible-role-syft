[![build-test](https://github.com/darkwizard242/ansible-role-syft/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-syft/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-syft/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-syft/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/57359?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/57359?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/57359?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-syft&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-syft) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-syft&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-syft) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-syft&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-syft) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-syft&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-syft) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-syft?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-syft?color=orange&style=flat-square)

# Ansible Role: syft

Role to install (_by default_) [syft](https://github.com/anchore/syft) on **Debian/Ubuntu** and **EL** systems. A CLI tool and Go library for generating a Software Bill of Materials (SBOM) from container images and filesystems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
syft_app: syft
syft_desired_state: present
syft_version: 0.49.0
syft_os: linux
syft_arch: amd64

# For Debian/Ubuntu Family
syft_debian_url: "https://github.com/anchore/{{ syft_app }}/releases/download/v{{ syft_version }}/{{ syft_app }}_{{ syft_version }}_{{ syft_os }}_{{ syft_arch }}.deb"

# For EL Family
syft_el_url: "https://github.com/anchore/{{ syft_app }}/releases/download/v{{ syft_version }}/{{ syft_app }}_{{ syft_version }}_{{ syft_os }}_{{ syft_arch }}.rpm"
```

### Variables table:

Variable           | Description
------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------
syft_app           | Defines the app to install i.e. **syft**
syft_desired_state | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`.
syft_version       | Defined to dynamically fetch the desired version to install. Defaults to: **0.49.0**
syft_os            | Defines os type. Used for obtaining the correct type of binaries based on OS type. Defaults to: **linux**
syft_arch          | Defines os architecture. Used for obtaining the correct type of binaries based on OS System Architecture. Defaults to: **amd64**
syft_debian_url    | Defines URL to download the 'deb' package from for Debian/Ubuntu family systems.
syft_el_url        | Defines URL to download the 'rpm' package from for EL family systems.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **syft**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.syft
```

For customizing behavior of role (i.e. specifying the desired **syft** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.syft
  vars:
    syft_version: 0.32.2
```

For customizing behavior of role (i.e. different os architecture of **syft** package like arm64) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.syft
  vars:
    syft_arch: "arm64"
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-syft/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev)
