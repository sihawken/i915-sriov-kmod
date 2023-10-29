%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     i915-sriov
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  Linux i915 module patched with SR-IOV support.
License:  GPLv2
URL:      https://github.com/sihawken/i915-sriov-kmod

Source:   %{url}/archive/refs/heads/main.tar.gz

Provides: %{name}-kmod-common = %{version}
Requires: %{name}-kmod >= %{version}

BuildRequires: systemd-rpm-macros

%description
Linux i915 module patched with SR-IOV support.

%prep
%setup -q -c %{name}-kmod-main

%files
%doc %{name}-kmod-main/README.md
%license %{name}-kmod-main/LICENSE

%changelog
{{{ git_dir_changelog }}}
