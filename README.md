# Ansible Role: Teku

### Description
Ansible role that will install, configure and runs [Teku](https://github.com/PegaSysEng/teku): an enterprise Java Ethereum 2 Client

### Table of Contents
  - [Supported Platforms](#supported-platforms)
  - [Dependencies](#dependencies)
  - [Role Variables](#role-variables)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

### Supported Platforms
```
* MacOS
* Debian
* Ubuntu
* Redhat(CentOS/Fedora)
* Amazon
```

### Dependencies

* JDK 11 or greater

### Role Variables:

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file. By and large these variables are configuration options. Please refer to the teku [docs](https://teku.hyperledger.org/en/stable/) for more information

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `teku_version` | ___unset___ |  __REQUIRED__ Version of teku to install and run. All available versions are listed on our teku [releases](https://github.com/PegaSysEng/teku/releases) page |
| `teku_user` | teku | teku user |
| `teku_group` | teku | teku group |
| `teku_download_url` | https://bintray.com/consensys/pegasys-repo/download_file?file_path=teku-{{ teku_version }}.tar.gz | The download tar.gz file used. You can use this if you need to retrieve teku from a custom location such as an internal repository. |
| `teku_install_dir` | /opt/teku | Path to install to  |
| `teku_config_dir` | /etc/teku | Path for default configuration |
| `teku_data_dir` | /opt/teku/data | Path for data directory|
| `teku_log_dir` | /var/log/teku | Path for logs |
| `teku_log4j_config_file` | "" | Absolute path for a custom log4j config file |
| `teku_profile_file` | /etc/profile.d/teku-path.sh | Path to allow loading teku into the system PATH |
| `teku_managed_service` | true | Enables a systemd service (or launchd if on Darwin) |
| `teku_launchd_dir` | /Library/LaunchAgents | The default launchd directory  |
| `teku_systemd_dir` | /etc/systemd/system/ | The default systemd directory |
| `teku_systemd_state` | restarted | The default option for the systemd service state |


### Example Playbook

1. Default setup:
Install the role from galaxy
```
ansible-galaxy install pegasyseng.teku
```

Create a requirements.yml with the following:
Replace `x.y.z` below with the version you would like to use from the teku [releases](https://github.com/PegaSysEng/teku/releases) page
```
---
- hosts: localhost
  connection: local
  force_handlers: True

  roles:
  - role: pegasyseng.teku
    vars:
      teku_version: x.y.z

```

Run with ansible-playbook:
```
ansible-playbook -v /path/to/requirements.yml
```


2. Install via github

```
ansible-galaxy install git+https://github.com/pegasyseng/ansible-role-teku.git
```

Create a requirements.yml with the following:
Replace `x.y.z` below with the version you would like to use from the teku [releases](https://github.com/PegaSysEng/teku/releases) page
```
---
- hosts: localhost
  connection: local
  force_handlers: True

  roles:
  - role: ansible-role-teku
    vars:
      teku_version: x.y.z

```

Run with ansible-playbook:
```
ansible-playbook -v /path/to/requirements.yml
```


### License

Apache


### Author Information

PegaSysEng, 2020
