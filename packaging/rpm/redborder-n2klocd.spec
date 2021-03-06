Name: redborder-n2klocd
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: Package for redborder n2klocd initscripts and configuration.

License: AGPL 3.0
URL: https://github.com/redBorder/redborder-n2klocd
Source0: %{name}-%{version}.tar.gz

Requires: n2kafka

%description
%{summary}

%prep
%setup -qn %{name}-%{version}

%build

%install
install -D -m 0644 resources/systemd/n2klocd.service %{buildroot}/usr/lib/systemd/system/n2klocd.service

%pre

%post
systemctl daemon-reload

%files
%defattr(0644,root,root)
/usr/lib/systemd/system/n2klocd.service
%doc

%changelog
* Fri Jan 21 2022 Eduardo Reyes <eareyes@redborder.com> - 0.0.1-1
- first spec version
