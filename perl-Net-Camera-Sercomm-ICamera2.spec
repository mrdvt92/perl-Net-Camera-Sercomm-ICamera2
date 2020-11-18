Name:           perl-Net-Camera-Sercomm-ICamera2
Version:        0.02
Release:        1%{?dist}
Summary:        Perl Interface for Sercomm ICamera2 network camera
License:        MIT
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Net-Camera-Sercomm-ICamera2/
Source0:        http://www.cpan.org/modules/by-module/Net/Net-Camera-Sercomm-ICamera2-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Package::New)
Requires:       perl(HTTP::Request)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Package::New)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The Sercomm ICamera2 is network camera that can be accessed via a
web interface. This module provides methods to retrieve an image
from the camera.

%prep
%setup -q -n Net-Camera-Sercomm-ICamera2-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/*

%changelog
* Fri Nov 13 2020 Michael R. Davis <mrdvt92@yahoo.com> 0.01-1
- Specfile autogenerated by cpanspec 1.78.
