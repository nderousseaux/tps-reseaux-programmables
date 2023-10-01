Lancer la vm :

```bash
qemu-system-x86_64 -drive file=p4-utils-vm.qcow2,format=qcow2 -m 2048 -boot c -nic user,hostfwd=tcp::8888-:22 --nographic
```

Se connecter en ssh :

```bash
ssh p4@127.0.0.1 -p 8888
```


## À l'intérieur de p4

Pour lancer le réseau :
```bash
sudo p4run
```

Ensuite dans le mininet, pour reboot un switch :
```bash
p4switch_reboot s1
```

Pour se connecter à un host
```bash
mx h1
```

