# i915-sriov-kmod

Not functional. Tested on Fedora Silverblue 38.

I have exhausted all things to try to get this to work.

The module installs to ``lib/modules/<kernel version>/extra/i915-sriov/i915.ko.xz`` and creates a file: ``/etc/depmod.d/kmod-i915-sriov.conf`` with contents: ``override i915 * extra/i915-sriov/``

As far as I can tell, it:

- Compiles against the kernel
- ``modinfo i915`` shows correct location of i915 module.
- Modules.dep shows the correct location for the kernel module: ``cat /usr/lib/modules/"$(rpm -qa kernel --queryformat '%{VERSION}-%{RELEASE}.%{ARCH}')"/modules.dep | grep i915``

And yet it doesnt work.

If you can figure it out, please fork this and submit a merge request. Thanks!