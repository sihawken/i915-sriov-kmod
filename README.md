# i915-sriov-kmod

Akmod version of https://github.com/strongtz/i915-sriov-dkms to allow installation on Fedora/RPM based systems.

Add the copr repository and install:
## Fedora Workstation:
```
dnf copr enable sihawken/akmods
dnf install akmod-i915-sriov
akmods --force
depmod -a
dracut --force
```