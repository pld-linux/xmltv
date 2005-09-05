Summary:	A set of utilities to manage your TV viewing.
Name:		xmltv
Version:	0.5.40
Release:	0.62
Group:		Applications/Multimedia
License:	GPL v2
URL:		http://membled.com/work/apps/xmltv/
Source0:	http://dl.sourceforge.net/xmltv/%{name}-%{version}.tar.bz2
# Source0-md5:	5cf460444846217c0dd9f95467e9e0a1
#Patch0:		%{name}-0.5.35-noask.patch
#Patch1:		%{name}-0.5.40-tv_grab_de_tvtoday.patch
Requires:	perl-Date-Manip >= 5.42
Requires:	perl(Term::ProgressBar) >= 2.03
Requires:	perl(WWW::Mechanize) => 1.02
Requires:	perl(Lingua::Preferred) >= 0.2.4
###Requires: perl(HTML::Parser) >= 3.34
Requires:	perl-XMLTV = %{epoch}:%{version}-%{release}
Requires:	xmltv-grabbers = %{epoch}:%{version}-%{release}
Requires:	xmltv-gui = %{epoch}:%{version}-%{release}
BuildRequires:	perl(LWP) >= 5.65
BuildRequires:	perl(XML::Parser) >= 2.34
BuildRequires:	perl(XML::Twig) >= 3.10
BuildRequires:	perl-Date-Manip >= 5.42
BuildRequires:	perl(XML::Writer) >= 0.4.6
BuildRequires:	perl(Memoize), perl(Storable) >= 2.04
# Recommended
BuildRequires:	perl(Lingua::EN::Numbers::Ordinate)
BuildRequires:	perl(Lingua::Preferred) >= 0.2.4
BuildRequires:	perl(Term::ProgressBar) >= 2.03
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl(Unicode::String)
# tv_grab_uk_rt, tv_grab_be, tv_grab_de_tvtoday, tv_grab_fr, tv_grab_no
# tv_grab_za
BuildRequires:	perl(HTML::Entities) >= 1.27
# tv_grab_uk_bleb
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(Archive::Zip)
# tv_grab_na_dd
BuildRequires:	perl(SOAP::Lite)
BuildRequires:	perl(Term::ReadKey)
# tv_grab_na_icons
BuildRequires:	perl(HTML::TableExtract) >= 1.08
BuildRequires:	perl(WWW::Mechanize) => 1.02
# tv_grab_fi, tv_grab_es, tv_grab_es_digital, tv_grab_nl
# tv_grab_nl_wolf, tv_grab_huro, tv_grab_dk, tv_grab_jp
# tv_grab_de_tvtoday, tv_grab_fr, tv_grab_pt, tv_grab_za
BuildRequires:	perl(HTML::TreeBuilder)
# tv_grab_jp
BuildRequires:	perl(Text::Kakasi)
# tv_grab_se, tv_grab_se_swedb
BuildRequires:	perl(XML::LibXML)
# tv_grab_se_swedb
BuildRequires:	perl(IO::Stringy)
BuildRequires:	perl(HTTP::Cache::Transparent)
# tv_check
BuildRequires:	perl(Tk)
BuildRequires:	perl-Tk-TableMatrix
# tv_pick_cgi
BuildRequires:	perl(CGI)
###BuildRequires: perl(HTML::Parser) >= 3.34
###BuildRequires: perl(XML::Simple)
###BuildRequires: perl(PerIO::gzip)
###BuildRequires: perl(HTML::LinkExtractor)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMLTV is a set of utilities to manage your TV viewing. They work with
TV listings stored in the XMLTV format, which is based on XML. The
idea is to separate out the backend (getting the listings) from the
frontend (displaying them for the user), and to implement useful
operations like picking out your favourite programmes as filters that
read and write XML documents.

%package -n perl-XMLTV
Summary:	Perl modules for managing your TV viewing.
Group:		Libraries
Requires:	perl(XML::Twig) >= 3.09
Requires:	perl-Date-Manip >= 5.41,
Requires:	perl-base >= 1:5.6.0

%description -n perl-XMLTV
XMLTV is a set of utilities to manage your TV viewing. They work with
TV listings stored in the XMLTV format, which is based on XML. The
idea is to separate out the backend (getting the listings) from the
frontend (displaying them for the user), and to implement useful
operations like picking out your favourite programmes as filters that
read and write XML documents.

This package contains the perl modules from xmltv.

%package grabbers
Summary:	Backends for xmltv.
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{epoch}:%{version}-%{release}
Requires:	perl-Date-Manip >= 5.41
Requires:	perl(LWP) >= 5.65
Requires:	perl(HTML::TableExtract) >= 1.08
Requires:	perl(Term::ProgressBar) >= 2.00

%description grabbers
XMLTV is a set of utilities to manage your TV viewing. They work with
TV listings stored in the XMLTV format, which is based on XML. The
idea is to separate out the backend (getting the listings) from the
frontend (displaying them for the user), and to implement useful
operations like picking out your favourite programmes as filters that
read and write XML documents.

This package contains the backends (grabbers) for xmltv.

%package gui
Summary:	Graphical frontends to xmltv.
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{epoch}:%{version}-%{release}
Requires:	perl-Date-Manip >= 5.41
Requires:	perl(LWP) >= 5.65

%description gui
XMLTV is a set of utilities to manage your TV viewing. They work with
TV listings stored in the XMLTV format, which is based on XML. The
idea is to separate out the backend (getting the listings) from the
frontend (displaying them for the user), and to implement useful
operations like picking out your favourite programmes as filters that
read and write XML documents.

This package contains graphical frontends to xmltv.

%prep
%setup -q
#%patch0 -p1 -b .noask
#%patch1 -p0 -b .tv_grab_de_tvtoday

%build
echo yes | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT
ln -s tv_grab_de_tvtoday $RPM_BUILD_ROOT%{_bindir}/tv_grab_de

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
#%dir %{_datadir}/xmltv
%{_bindir}/tv_cat
%{_bindir}/tv_extractinfo_en
%{_bindir}/tv_grep
%{_bindir}/tv_imdb
%{_bindir}/tv_remove_some_overlapping
%{_bindir}/tv_sort
%{_bindir}/tv_split
%{_bindir}/tv_to_latex
%{_bindir}/tv_to_text
%{_bindir}/tv_to_potatoe
%{_mandir}/man1/tv_cat.1*
%{_mandir}/man1/tv_extractinfo_en.1*
%{_mandir}/man1/tv_grep.1*
%{_mandir}/man1/tv_imdb.1*
%{_mandir}/man1/tv_remove_some_overlapping.1*
%{_mandir}/man1/tv_sort.1*
%{_mandir}/man1/tv_split.1*
%{_mandir}/man1/tv_to_latex.1*
%{_mandir}/man1/tv_to_text.1*
%{_mandir}/man1/tv_to_potatoe.1*

%files -n perl-XMLTV
%defattr(644,root,root,755)
%{perl_vendorlib}/XMLTV.pm
%{perl_vendorlib}/XMLTV
%{_mandir}/man3/*

%files grabbers
%defattr(644,root,root,755)
%{_bindir}/tv_grab_*
%{_mandir}/man1/tv_grab_*.1*
#%dir %{_datadir}/xmltv
#%{_datadir}/xmltv/tv_grab_*

%files gui
%defattr(644,root,root,755)
%{_bindir}/tv_check
%{_mandir}/man1/tv_check.1*
