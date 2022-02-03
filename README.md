![Logo](https://raw.githubusercontent.com/idealista/consul_keystore_role/master/logo.gif)

[![Build Status](https://travis-ci.org/idealista/consul_keystore_role.png)](https://travis-ci.org/idealista/consul_keystore_role)

# Consul Keystore Ansible role

Ansible role to manage Consul Keystore.

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installing](#installing)
- [Usage](#usage)
- [Testing](#testing)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Contributing](#contributing)

## Getting Started

These instructions will get you a copy of the role for your Ansible Playbook. Once launched, it will manage the consul keystore.

### Prerequisites

Ansible 2.10.x version installed. Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Docker](https://www.docker.com/) as driver.
See [test-requirements](test-requirements.txt).

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

``` yml
- src: idealista.consul_keystore_role
  version: 2.0.0
  name: consul_keystore
```

Install the role with ansible-galaxy command:

```sh
ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

``` yml
---
- hosts: localhost
  connection: local
  become: false
  roles:
    - consul_keystore
```

## Usage

Look to the [defaults](defaults/main.yml) properties file to see the possible configuration properties.

## Testing

```sh
$ pipenv sync
```
For more information read the [pipenv docs](https://pipenv-fork.readthedocs.io/en/latest)
```
$ pipenv run molecule test
```


## Built With

![Ansible](https://img.shields.io/badge/ansible-2.10.7-green.svg)
![Molecule](https://img.shields.io/badge/molecule-3.1.5-green.svg)
![Goss](https://img.shields.io/badge/goss-0.3.16-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/consul_keystore_role/tags).

You can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

- **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/consul_keystore_role/contributors) who participated in this project.

## License

![Apache 2.0 License](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
