%include        /usr/lib/rpm/macros.perl
Summary:	perl-Mon module
Name:		perl-Mon	
version:	0.11	
Release:	1	
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.kernel.org/pub/software/admin/mon/Mon-%{version}.tar.gz
URL:		http://www.kernel.org/software/mon/
BuildRequires:	perl-devel >= 5.6.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
   
%description
This is the Perl5 module for interfacing with the Mon system
monitoring package. Currently only the client interface is
implemented, but more things like special logging routines and
persistent monitors are being considered.

%prep
%setup -q  -n Mon-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CHANGES README

%files
%defattr(644,root,root,755)
%doc *.gz 
%{perl_sitelib}/*
%{_mandir}/man3/*

%clean
rm -rf $RPM_BUILD_ROOT
