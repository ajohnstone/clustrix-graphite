Name:      clustrix-graphite
Summary:   Monitor Clutrix
Version:   %{version}
Release:   %{release}
Group:     Applications/Databases
License:   GPL
Vendor:    Andrew Johnstone.
URL:       https://github.com/ajohnstone/clustrix-graphite
Source:    clustrix-graphite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires:  perl(DBI) >= 1.13, perl(DBD::mysql) >= 1.0
AutoReq:   no

%description
Clustrix monitoring

%prep
%setup -q

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
find $RPM_BUILD_ROOT -type f -name 'clustrix-graphite.pod' -exec rm -f {} ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING INSTALL README.md Changelog
%{_bindir}/*
%{_mandir}/man1/*.1*

%changelog
* Sun Oct 14 2012 Andrew Johnstone
- Initial
