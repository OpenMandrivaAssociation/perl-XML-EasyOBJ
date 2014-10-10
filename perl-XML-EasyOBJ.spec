%define upstream_name 	 XML-EasyOBJ
%define upstream_version 1.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	%{upstream_name} perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch
Requires:	perl(XML::Parser)
Requires:	perl(XML::XSLT)

%description
%{upstream_name} - Easy XML object navigation

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix} 
make

%install
make PREFIX=%{buildroot}%{_prefix} install

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/XML/*


%changelog
* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.120.0-1mdv2010.0
+ Revision: 401866
- rebuild using %%perl_convert_version

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.12-8mdv2009.0
+ Revision: 258838
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.12-7mdv2009.0
+ Revision: 246727
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.12-5mdv2008.1
+ Revision: 136365
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 1.12-5mdv2008.0
+ Revision: 23517
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.12-4mdk
- Fix According to perl Policy
	- Source URL
	- URL
- use mkrel

* Tue Jun 29 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.12-3mdk
- rebuild

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.12-2mdk
- rebuild for new auto{prov,req}

