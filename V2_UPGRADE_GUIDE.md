# Version 2.0.0 upgrade guide

With this version `2.0.0` we introduce changes to put properties.

- Now you can choose mode to upload properties (key-value or yml file).
- Now you have to put filename with extension.

Next we'll show you how to migrate from 1.x.x to 2.0.0.

### Plugins
In 1.x.x release, we configure files for example as:
```
---
consul_keystore_properties_files:
  - some_properties
  - another_properties
  - more
```

Now, in 2.x.x release, we changed to:
```
---
consul_keystore_properties_files:
  - name: some_properties.yml
    format: kv
  - name: another_properties.yml
    format: kv
  - name: more.properties
    format: kv
```
So basically, you have to:
1. Add extension of file item.
2. Add format `kv` or `file`. `kv` to put properties individually or `file` to put entire file.

If you want to put properties as file, it could be as:
```
---
consul_keystore_properties_files:
    - name: full_yml.yml
      key: data
      format: file
```

You can see example in molecule defaults [here](molecule/default/group_vars/all.yml).