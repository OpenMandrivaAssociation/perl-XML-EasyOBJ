%define upstream_name 	 XML-EasyOBJ
%define upstream_version 1.12

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release: 	%mkrel 1

Summary:	%{upstream_name} perl module
License: 	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Requires:  perl-XML-Parser 
Requires:  perl-XML-XSLT 

%description
%{upstream_name} - Easy XML object navigation

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
