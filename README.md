![Logo](https://raw.githubusercontent.com/idealista/consul_keystore-role/master/logo.gif)

# Consul Keystore Ansible role

Ansible role to manage Consul Keystore.

- [Getting Started](#getting-started)
  - [Prerequisities](#prerequisities)
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

### Prerequisities

Ansible 2.4.3.0 version installed.
Molecule 1.25 version installed.
Ansible-Lint 3.4.20 version installed.
python-consul 1.1.0 version installed

Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Vagrant](https://www.vagrantup.com/) as driver (with [hostmanager](https://github.com/devopsgroup-io/vagrant-hostmanager) plugin) and [VirtualBox](https://www.virtualbox.org/) as provider.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

``` yml
- src: idealista.consul_keystore-role
  version: 1.0.0
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
molecule test
```

or

```sh
./tests/scripts/run-test.sh
```

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.4.3.0-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/consul_keystore-role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

- **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/consul_keystore-role/contributors) who participated in this project.

## License

![Apache 2.0 License](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
