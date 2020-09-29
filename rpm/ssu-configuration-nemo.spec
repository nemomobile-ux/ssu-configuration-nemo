Name: 		ssu-kickstart-configuration-nemo
Summary: 	Sample vendor configuration data
Version:	1.0.0
Release:	0
Source:		%{name}-%{version}.tar.bz2
Group:		System
License:	BSD-3-Clause

Provides: 	ssu-kickstart-configuration
Requires: 	ssu-ks >= 0.29
Requires:	 grep

BuildArch:	noarch

%description
Configuration required to build kickstarts using ssuks.

%prep
%setup -q

%build
rm -rf %{buildroot}/

%install
mkdir -p $RPM_BUILD_ROOT
cp -r data/* $RPM_BUILD_ROOT/

%files
%defattr(-,root,root,-)
%{_datadir}/ssu/board-mappings.d/01-kickstart.ini
%{_datadir}/ssu/kickstart/*

