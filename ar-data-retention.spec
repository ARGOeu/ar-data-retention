Name: ar-data-retention
Summary: A/R data retention scripts
Version: 1.0.1
Release: 1%{?dist}
License: ASL 2.0
Buildroot: %{_tmppath}/%{name}-buildroot
Group:     EGI/SA4
BuildArch: x86_64
Source0:   %{name}-%{version}.tar.gz
Requires: hive
Requires: python-pymongo

%description
Installs the A/R data retention scripts

%prep
%setup 

%install 
%{__rm} -rf %{buildroot}
install --directory %{buildroot}/usr/libexec/ar-data-retention
install --directory %{buildroot}/var/log/ar-data-retention
install --directory %{buildroot}/etc
install --directory %{buildroot}/etc/cron.d
install --directory %{buildroot}/etc/ar-data-retention

install --mode 644 etc/ar-data-retention/ar-data-retention.conf %{buildroot}/etc/ar-data-retention/
install --mode 755 bin/ar-data-retention %{buildroot}/usr/libexec/ar-data-retention
install --mode 644 cronjobs/ar-data-retention %{buildroot}/etc/cron.d/ar-data-retention

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root)
%attr(0755,root,root) /usr/libexec/ar-data-retention/ar-data-retention
%config(noreplace) /etc/ar-data-retention/ar-data-retention.conf
%attr(0644,root,root) /etc/cron.d/ar-data-retention

%changelog
* Thu Jan 29 2015 Luko Gjenero <lgjenero@gmail.com> - 1.0.2-1%{?dist}
- Added file removal
* Thu Aug 29 2013 Luko Gjenero <lgjenero@srce.hr> - 1.0.0-1%{?dist}
- Initial release
