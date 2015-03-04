Name: ar-data-retention
Summary: A/R data retention scripts
Version: 1.0.2
Release: 4%{?dist}
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
* Mon Mar 2 2015 Paschalis Korosoglou <pkoro@grid.auth.gr> - 1.0.2-3%{?dist}
- Corrections in paths for consumer and sync data
- Mongo tables we need to apply retention to
- Drop hive partitions using hdfs user
- Leave only tables that exist on Hive in configuration
- Minor fixes
* Sun Mar 1 2015 Paschalis Korosoglou <pkoro@grid.auth.gr> - 1.0.2-2%{?dist}
- Minor modifications and typos
- Raised retention in days too extremely high value only for initial deployment/testing purposes
- Generic hostnames in configuration file and main script
- Quick fix to have function loadConfiguration overwrite globally assigned values
* Thu Jan 29 2015 Luko Gjenero <lgjenero@gmail.com> - 1.0.2-1%{?dist}
- Added file removal
* Thu Aug 29 2013 Luko Gjenero <lgjenero@srce.hr> - 1.0.0-1%{?dist}
- Initial release
