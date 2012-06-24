%include        /usr/lib/rpm/macros.perl
Summary:	perl-Mon module
Summary(pl):	Modu� perla Mon
Name:		perl-Mon	
version:	0.11	
Release:	3	
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Mon/Mon-%{version}.tar.gz
URL:		http://www.kernel.org/software/mon/
BuildArch:	noarch
BuildRequires:	perl-devel >= 5.6.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
   
%description
This is the Perl5 module for interfacing with the Mon system
monitoring package. Currently only the client interface is
implemented, but more things like special logging routines and
persistent monitors are being considered.

%description -l pl
To jest modu� perla do komunikacji z systemem monitoruj�cym Mon.
Aktualnie zaimplementowany jest tylko interfejs klienta.

%prep
%setup -q -n Mon-%{version}

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
%{perl_sitelib}/Mon
%{_mandir}/man3/*

%clean
rm -rf $RPM_BUILD_ROOT
