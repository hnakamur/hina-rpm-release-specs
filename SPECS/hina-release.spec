Name:           hina-release
Version:        6
Release:        2
Summary:        hina-release rpm repository

Group:          System Environment/Base
License:        MIT

URL:            http://naruh.com/pub/hina-release/
Source0:        RPM-GPG-KEY-hina
Source1:        hina.repo

BuildArch:     noarch
Requires:      redhat-release >=  %{version}
Conflicts:     fedora-release

%description
This package contains yum configuration and GPG key for
hina-release rpm repository.

%prep
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .

%build


%install
rm -rf $RPM_BUILD_ROOT

#GPG Key
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
install -Dpm 644 %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/

%clean
rm -rf $RPM_BUILD_ROOT

%post

%preun

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*


%changelog
* Thu Feb 07 2013 Hiroaki Nakamura <hnakamur@gmail.com> - 6-2
- Merged hina-release repo file with hina-testing.

* Tue Jan 22 2013 Hiroaki Nakamura <hnakamur@gmail.com> - 6-1
- Initial commit.
