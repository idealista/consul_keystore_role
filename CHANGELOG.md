# Change Log

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a changelog](https://github.com/olivierlacan/keep-a-changelog).

## [Unreleased]

[Full Changelog](https://github.com/idealista/consul_keystore_role/compare/master...develop)

## [2.0.1] 2022-03-04
### Fixed
- *[#13](https://github.com/idealista/consul_keystore_role/issues/13) Fixed delete steps making diff of whole keys and files processed. @adrian-arapiles*

## [2.0.0] 2022-02-03

### Added
- *[#13](https://github.com/idealista/consul_keystore_role/issues/13) Support for put entire yml files to consul keystore* @adrian-arapiles
- *Added tests for entire yml put on consul keystore* @adrian-arapiles
- *Add ansible-lint and improve yamllint* @adrian-arapiles
- *Add migrate guide from 1.x.x to 2.0.0* @adrian-arapiles

### Changed
- *Improve task to avoid unnecessary skipped or loops* @adrian-arapiles
- *Update test-requirements and deleted 2.7 python* @adrian-arapiles
- *Add test for debian buster environment* @adrian-arapiles
- *Update molecule tests and test files* @adrian-arapiles
- *Rename from `consul_keystore-role` to `consul_keystore_role` as ansible recommendations* @adrian-arapiles
- *Replace module `consul_keystore` committed in repo in favour of `consul_kv` official module* @adrian-arapiles

## [1.0.2] - 2018-12-18

### Fixed

- *[#10](https://github.com/idealista/consul_keystore_role/issues/10) Fix problem removing properties in python 3* @jmonterrubio

## [1.0.1] - 2018-11-13

### Fixed

- *[#8](https://github.com/idealista/consul_keystore_role/issues/8) Fix problem with empty lines and comments in .properties file* @jmonterrubio
- *[#3](https://github.com/idealista/consul_keystore_role/issues/3) Fix property is ansible changed if no value is setted* @jmonterrubio
- *[#4](https://github.com/idealista/consul_keystore_role/issues/4) Fix boolean values converted with capital letter* @jmonterrubio

## [1.0.0] - 2018-10-10

### Added

*Initial version* @jmonterrubio

[2.0.0]: https://github.com/idealista/consul_keystore_role/tree/2.0.0
[1.0.2]: https://github.com/idealista/consul_keystore_role/tree/1.0.2
[1.0.1]: https://github.com/idealista/consul_keystore_role/tree/1.0.1
[1.0.0]: https://github.com/idealista/consul_keystore_role/tree/1.0.0
[Unreleased]: https://github.com/idealista/consul_keystore_role/tree/develop
