%global buildforkernels akmod
%global debug_package %{nil}

# Enable zipping the modules with xz
%global zipmodules 1

%define __spec_install_post \
  %{__arch_install_post}\
  %{__os_install_post}\
  %{__mod_compress_install_post}

%define __mod_compress_install_post \
  if [ "%{zipmodules}" -eq "1" ]; then \
    find %{buildroot}/usr/lib/modules/ -type f -name '*.ko' | xargs xz; \
  fi

Name:     i915-sriov-backports-kmod
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  Linux i915 module patched with SR-IOV support.
License:  GPLv2
URL:      https://github.com/intel-gpu/intel-gpu-i915-backports

Source:   %{url}/archive/refs/heads/backport/main.tar.gz

BuildRequires: kmodtool
ExclusiveArch: x86_64

%{expand:%(kmodtool --target %{_target_cpu} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Linux i915 module patched with SR-IOV support.

%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}

# print kmodtool output for debugging purposes:
kmodtool --target %{_target_cpu} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%setup -q -c intel-gpu-i915-backports-backport-main
echo "search extra" > kmod-i915-sriov.conf

find . -type f -name '*.c' -exec sed -i "s/#VERSION#/%{version}/" {} \+

cp intel-gpu-i915-backports-backport-main/defconfigs/i915 intel-gpu-i915-backports-backport-main/.config;

for kernel_version  in %{?kernel_versions} ; do
  cp -a intel-gpu-i915-backports-backport-main _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version  in %{?kernel_versions} ; do
  make V=1 %{?_smp_mflags} -C ${kernel_version##*___} \
    M=${PWD}/_kmod_build_${kernel_version%%___*} KVER=${kernel_version%%___*}
done

%install
for kernel_version in %{?kernel_versions}; do
    mkdir -p %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
    install -p -m 0755 _kmod_build_${kernel_version%%___*}/*.ko \
        %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
done

%{__install} -d %{buildroot}%{_sysconfdir}/depmod.d/
%{__install} kmod-i915-sriov.conf %{buildroot}%{_sysconfdir}/depmod.d/

%{?akmod_install}

%clean
rm -rf %{buildroot}

%files
/%{_sysconfdir}/depmod.d/kmod-i915-sriov.conf

%changelog
{{{ git_dir_changelog }}}