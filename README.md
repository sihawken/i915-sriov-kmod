# i915-sriov-kmod

~~Akmod version of https://github.com/strongtz/i915-sriov-dkms to allow installation on Fedora/RPM based systems.~~

Akmod version of https://github.com/sihawken/i915-sriov-dkms to allow installation on Fedora/RPM based systems.

Newer version of i915 library taken from https://github.com/intel/mainline-tracking/tree/80524e664317c8d56559fbea0ea8675e9142f601

Add the copr repository and install:
## Fedora Workstation:
```
dnf copr enable sihawken/akmods
dnf install akmod-i915-sriov
akmods --force
depmod -a
dracut --force
```
