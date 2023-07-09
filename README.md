# Ansible Collection - tafeen.hikvision
This collection was based on latest ISAPI documentation from Hikvision.
Also this collection enables to call commands over SSH (hv_cmd role)

## Examples of usage

1. Save current settings of hosts:
```
---
- name: Export settings from hosts
  hosts: cctv
    
  tasks:
    - name: Export Settings
      import_role:
         name: tafeen.hikvision.hv_export_settings
      vars:
         export_path_dir: ~/
         hv_export_key: "<your-export-key>"
```

2. Get list of commands provided by hosts
```
---
- name: Get list of commands provided by host
  hosts: cctv
  gather_facts: false # Otherwise it will stuck
    
  tasks:
    - name: Get list of commands
      import_role:
         name: tafeen.hikvision.hv_cmd
      vars:
         command: "help"
```

3. Check date on hosts
```
---
- name: Check date on hosts
  hosts: cctv
  gather_facts: false # Otherwise it will stuck
    
  tasks:
    - name: Check date of host
      import_role:
         name: tafeen.hikvision.hv_cmd
      vars:
         command: "getDateInfo"
```