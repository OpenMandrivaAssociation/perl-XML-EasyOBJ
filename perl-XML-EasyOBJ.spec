%define module 	XML-EasyOBJ
%define version 1.12
%define release %mkrel 7

Summary:	%{module} perl module
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{module}-%{version}.tar.bz2
Requires:	perl-XML-Parser 
Requires:       perl-XML-XSLT 
BuildRequires:	perl-devel >= 5.8.0
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch
Url:		http://search.cpan.org/dist/%{module}

%description
%{module} - Easy XML object navigation

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix} 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} PREFIX=$RPM_BUILD_ROOT%{_prefix} install

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/XML/*


