Summary: Apache NiFi
Name: nifi
Version: 0.1.0
Release: incubating
License: Apache License, Version 2.0
Group: Applications/System
Source: %{name}-%{version}-%{release}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildarch: noarch
Requires: java >= 1.7.0
Packager: Onyx Point

Prefix: /opt/%{name}

%description
RPM build of Apache NiFi

%prep
%setup -q -n %{name}-%{version}-%{release}

%build

%install
#[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/

dir='../%{name}-%{version}-%{release}'
test -d $dir && cp -r $dir %{buildroot}/%{prefix}/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/

%files
%defattr(0640,root,root,0750)
%{prefix}/

%post
#!/bin/sh

if [ -d %{prefix}/%{name}-%{version}-%{release} ]; then
  /bin/ln -sf %{prefix}/%{name}-%{version}-%{release} %{prefix}/default
fi

%postun
# Post uninstall stuff

%changelog
* Thu Jun 4 2015 Than H. Maung <than.maung@onyxpoint.com>
0.1-0
- Initial build file
