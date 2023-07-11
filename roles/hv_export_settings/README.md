# Ansible hikvision ISAPI exporting settings

Example of usage:
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
         hv_export_key: "<your-export-key>
```