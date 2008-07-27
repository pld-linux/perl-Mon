#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	perl-Mon module
Summary(pl.UTF-8):	Moduł Perla Mon
Name:		perl-Mon
Version:	0.11
Release:	7
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Mon/Mon-%{version}.tar.gz
# Source0-md5:	762a8c6f845f8f1482a696e6f95f4492
URL:		http://www.kernel.org/software/mon/
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Perl5 module for interfacing with the Mon system
monitoring package. Currently only the client interface is
implemented, but more things like special logging routines and
persistent monitors are being considered.

%description -l pl.UTF-8
To jest moduł Perla do komunikacji z systemem monitorującym Mon.
Aktualnie zaimplementowany jest tylko interfejs klienta.

%prep
%setup -q -n Mon-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/Mon
%{_mandir}/man3/*
