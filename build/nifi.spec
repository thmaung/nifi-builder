Summary: Apache NiFi
Name: nifi
Version: 0.1.0
Release: incubating
License: Apache License, Version 2.0
Group: Applications/System
Source: %{name}-%{version}-%{release}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildarch: noarch
# Requires jdk or java-devel but problems with this line for now
#Requires: java >= 1.7.0
Packager: Onyx Point

Prefix: /opt/%{name}

%description
RPM build of Apache NiFi

%prep
%setup -q -n %{name}-%{version}-%{release}

%build

%install
mkdir -p %{buildroot}/%{prefix}/

# It goes into the nifi-0.1.0-incubator directory by default so we are going back a level.
# This way it installs to /opt/nifi/nifi-0.1.0-incubator and then create the default symlink.
dir='../%{name}-%{version}-%{release}'
test -d $dir && cp -r $dir %{buildroot}/%{prefix}/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/

%files
%defattr(0640,root,root,0750)
%{prefix}/
%attr(755,-,-) %{prefix}/%{name}-%{version}-%{release}/bin/nifi.sh

%post
#!/bin/sh

if [ -d %{prefix}/%{name}-%{version}-%{release} ]; then
  /bin/ln -sf %{prefix}/%{name}-%{version}-%{release} %{prefix}/default
fi

%postun
if [ -L %{prefix}/default ]; then
  /bin/rm -f %{prefix}/default
fi

%changelog
* Thu Jun 4 2015 Than H. Maung <than.maung@onyxpoint.com>
0.1-0
- Initial build file
