%define upstream_name 	 XML-EasyOBJ
%define upstream_version 1.12
Name:		perl-%{upstream_name}
Version:	1.12
Release:	1

Summary:	%{upstream_name} perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/XML-EasyOBJ
Source0:	https://cpan.metacpan.org/authors/id/R/RH/RHANSON/XML-EasyOBJ-1.12.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch
Requires:	perl(XML::Parser)
Requires:	perl(XML::XSLT)

%description
%{upstream_name} - Easy XML object navigation

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix} 
make

%install
make PREFIX=%{buildroot}%{_prefix} install

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/XML/*


