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
* Debian
* Ubuntu
* Redhat(CentOS/Fedora)
* Amazon
```

### Dependencies

* JDK 21 or greater

### Role Variables:

Teku has the following operating modes:

1. Combined = beacon + validator as a single unified process. This is generally used for dev / limited resources. This is the default option
      ```bash
      teku_combined_enabled: true 
      ```

2. Beacon + Validator = beacon + validator, each as a separate processes on the same machine. If you wish to run them seperately on different machines, use option 3 & 4 below
      ```bash
      teku_combined_enabled: false
      teku_beacon_enabled: true
      teku_valdiator_enabled: true
      ```

3. Beacon = only the beacon client 
      ```bash
      teku_combined_enabled: false
      teku_beacon_enabled: true
      ```

4. Validator = only the validator client
      ```bash
      teku_combined_enabled: false
      teku_valdiator_enabled: true
      ```

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file. By and large these variables are configuration options. Please refer to the teku [docs](https://docs.teku.consensys.net/en/latest) for more information

| Name                                       | Default Value                           | Description                                          |
|--------------------------------------------|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `teku_combined_enabled`                    | True     | Run beacon and validator (if any) as a single process     |
| `teku_validator_enabled`                   | False    | Run validator as a single process        |
| `teku_beacon_enabled`                      | False    | Run beacon as a single process       |
| `teku_version`                             | ___unset___                             | __REQUIRED__ Version of teku to install and run. All available versions are listed on our teku [releases](https://github.com/PegaSysEng/teku/releases) page. Can use `latest` to discover the latest released version |
| `teku_user`                                | teku                                    | teku user                               |
| `teku_group`                               | teku                                    | teku group                              |
| `teku_download_url`                        | https://artifacts.consensys.net/public/teku/raw/names/teku.tar.gz/versions/{{ teku_version }}/teku-{{ teku_version }}.tar.gz | The download tar.gz file used. You can use this if you need to retrieve teku from a custom location such as an internal repository.                         |
| `teku_install_dir`                         | /opt/teku                         | Path to install to                      |
| `teku_config_dir`                          | /etc/teku                         | Path for default configuration          |
| `teku_data_dir`                            | /opt/teku/data                    | Path for data directory                 |
| `teku_validator_data_dir`                  | /opt/teku/data                    | Path for data directory for a validator |
| `teku_log_dir`                             | /var/log/teku                     | Path for logs directory                 |
| `teku_log_filename`                        | {{ `teku_log_dir` }}/teku.log     | Path containing the location (relative or absolute) and the log filename  | 
| `teku_profile_file`                        | /etc/profile.d/teku-path.sh       | Path to allow loading teku into the system PATH                           |
| `teku_managed_service`                     | true                              | Enables a systemd service               |
| `teku_systemd_dir`                         | /etc/systemd/system/              | default systemd directory           |
| `teku_systemd_state`                       | restarted                         | The default option for the systemd service state |
| `teku_output_transition_dir`               | /tmp/teku|                                         |
| `teku_node_private_key_file`               | ""       | Path to store the private key           |
| `teku_network`                             | minimal  | Predefined network configuration        |
| `teku_host_ip`                             | ""       |                                         |
| `teku_p2p_enabled`                         | True     | Enables or disables all P2P communication                                          |
| `teku_p2p_interface`                       | 0.0.0.0  | Specifies the network interface on which the node listens for P2P communication    |
| `teku_p2p_port`                            | 9000     | Specifies the P2P listening ports (UDP and TCP)                                    |
| `teku_p2p_advertised_port`                 | 9000     | The advertised P2P port                 |
| `teku_p2p_discovery_enabled`               | True     | Enables or disables P2P peer discovery  |
| `teku_interop_genesis_time`                | 0        |                                         |
| `teku_interop_start_state`                 | ""       |                                         |
| `teku_interop_owned_validator_start_index` | 0        |                                         |
| `teku_interop_owned_validator_count`       | 64       |                                         |
| `teku_interop_number_of_validators`        | 64       |                                         |
| `teku_interop_enabled`                     | False    |                                         |
| `teku_deposit_mode`                        | normal   |                                         |
| `teku_deposit_input_file`                  | ""       |                                         |
| `teku_deposit_number_validators`           | 64       |                                         |
| `teku_deposit_contract_address`            | 0x       | Eth1 address of deposit contract        |
| `teku_deposit_eth1_endpoint`               | ""       | JSON-RPC URL of Eth1 node               |
| `teku_metrics_enabled`                     | True     | Set to true to enable the metrics exporter |
| `teku_metrics_interface`                   | 0.0.0.0  |                                         |
| `teku_metrics_port`                        | 8008     | Metric port when deployed as combined   |
| `teku_beacon_metrics_port`                 | 8008     | Beacon service metric port                            |
| `teku_validator_metrics_port`              | 8009     | Validator service metric port when deployed as validator single process            |
| `teku_metrics_categories`                  | [] (All categories enabled)                         | Categories for which to track metrics   |
| `teku_data_path`                           | /data    | Use same folder for both validator and beacon service in single process standalone mode           |
| `teku_data_storage_mode`                   | prune    | Set the strategy for handling historical chain data                                |
| `teku_beacon_rest_api_port`                | 5051     |                                         |
| `teku_beacon_rest_api_docs_enabled`        | False    |                                         |
| `teku_beacon_rest_api_enabled`             | True     | Enable the REST API service             |
| `teku_beacon_rest_api_interface`           | 127.0.0.1| Interface for the REST API service      |
| `teku_beacon_rest_api_host_allowlist`      | ["*"]    | Host allowlist for for the REST API service                                        |
| `teku_cmdline_args`                        | []       |                                         |
| `teku_cmdline_args_beacon`                 | []       | Only applicable in single process standalone mode. Allows setting beacon specific values          |
| `teku_cmdline_args_validator`              | []       | Only applicable in single process standalone mode. Allows setting validator specific values       |
| `teku_env_opts`                            | []       |                                         |
| `teku_env_opts_beacon`                     | []       | Only applicable in single process standalone mode. Allows setting beacon specific values          |
| `teku_env_opts_validator`                  | []       | Only applicable in single process standalone mode. Allows setting validator specific values       |

List of variables which are not defined with default values in ansible role. However if these variables set via command line those will configured in teku configuration file

| Name                                              | Configuration File Parameter                 | Description        |
|---------------------------------------------------|----------------------------------------------|---------------------------------------------------------------------------------------------|
| `teku_data_beacon_path`                           | `data-beacon-path`                           | Path to beacon data|
| `teku_data_storage_archive_frequency`             | `data-storage-archive-frequency`             | Sets the frequency, in slots, at which to store finalized states to disk                    |
| `teku_data_validator_path`                        | `data-validator-path`                        | Path to validator client data                                                               |
| `teku_ee_endpoint`                                | `ee-endpoint`                                | The execution engine endpoint URL                                                           |
| `teku_ee_jwt_secret_file`                         | `ee-jwt-secret-file`                         | File to read the execution engine JWT authentication secret from                            |
| `teku_log_level`                                  | `logging`                                    | Logging verbosity levels: OFF, FATAL, ERROR, WARN, INFO, DEBUG, TRACE, ALL                  |
| `teku_log_validator_duties`                       | `log-include-validator-duties-enabled`       | Whether events are logged when validators perform duties                                    |
| `teku_p2p_discovery_bootnodes`                    | `p2p-discovery-bootnodes`                    | List of ENRs of the bootnodes ex: ['enr:-enr-string','enr:-enr-string']                     |
| `teku_p2p_peer_lower_bound`                       | `p2p-peer-lower-bound`                       | Lower bound on the target number of peers                                                   |
| `teku_p2p_peer_upper_bound`                       | `p2p-peer-upper-bound`                       | Upper bound on the target number of peers                                                   |
| `teku_p2p_static_peers`                           | `p2p-static-peers`                           | Static peers. ex: ['peer1-address','peer2-address']                                         |
| `teku_p2p_subscribe_all_subnets_enabled`          | `p2p-subscribe-all-subnets-enabled`          | True/False         |
| `teku_validators_external_signer_public_keys`     | `validators-external-signer-public-keys`     | The list of external signer public keys ex: ['key1','key2']                                 |
| `teku_validators_external_signer_timeout`         | `validators-external-signer-timeout`         | Timeout (in milliseconds) for the external signing  service                                 |
| `teku_validators_external_signer_url`             | `validators-external-signer-url`             | URL for the external signing service                                                        |
| `teku_validators_proposer_default_fee_recipient`  | `validators-proposer-default-fee-recipient`  | Default fee recipient to use when proposing post-merge blocks                               |
| `teku_validators_proposer_config`                 | `validators-proposer-config`                 | Remote URL or local file path to load proposer configuration from                           |
| `teku_validators_proposer_config_refresh_enabled` | `validators-proposer-config-refresh-enabled` | Whether to periodically refresh the proposer config                                         |
| `teku_validators_graffiti`                        | `validators-graffiti`                        | Graffiti to include during block creation (gets converted to bytes and padded to Bytes32)   |
| `teku_validators_keystore_locking_enabled`        | `validators-keystore-locking-enabled`        | Enable locking validator keystore files (Valid values True, False)                          |
| `teku_validators_performance_tracking_enabled`    | `validators-performance-tracking-enabled`    | Enable validator performance tracking and logging (Valid values True, False)                |
| `teku_validators_early_attestations_enabled`      | `validators-early-attestations-enabled`      | Enable early attestation production (Valid values True, False)                              |
| `teku_ws_checkpoint`                              | `ws-checkpoint`                              | A recent checkpoint within the weak subjectivity period. Format <BLOCK_ROOT>:<EPOCH_NUMBER> |
| `teku_beacon_node_api_endpoints`                  | `beacon-node-api-endpoints`                  | Array. The beacon node API endpoints the validator client should connect to.                |


### Single Process Standalone Mode 

It is possible to configure Teku to run in either combined mode (both beacon and validator run in same process) or standalone mode(beacon and validator run in its own process respectively).
Standalone mode runs beacon service its own process and validator service in its own process. Systemd service name `teku-beacon` is used for beacon service
and `teku-validator` is used for validator service when run in standalone mode. 

### Example Playbook

1. Default setup:
Install the role from galaxy
```
ansible-galaxy install consensys.teku
```

Create a requirements.yml with the following:
Replace `x.y.z` below with the version you would like to use from the teku [releases](https://github.com/PegaSysEng/teku/releases) page
```
---
- hosts: localhost
  connection: local
  force_handlers: True

  roles:
  - role: consensys.teku
    vars:
      teku_version: x.y.z

```

Run with ansible-playbook:
```
ansible-playbook -v /path/to/requirements.yml
```


2. Install via github

```
ansible-galaxy install git+https://github.com/consensys/ansible-role-teku.git
```

Create a requirements.yml with the following:
Replace `x.y.z` below with the version you would like to use from the teku [releases](https://github.com/consensys/teku/releases) page
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

Consensys, 2025



### TODO

