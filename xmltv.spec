%include	/usr/lib/rpm/macros.perl
Summary:	A set of utilities to manage your TV viewing
Summary(pl):	Zestaw narzêdzi do zarz±dzania ogl±daniem TV
Name:		xmltv
Version:	0.5.40
Release:	1
Group:		Applications/Multimedia
License:	GPL v2
Source0:	http://dl.sourceforge.net/xmltv/%{name}-%{version}.tar.bz2
# Source0-md5:	5cf460444846217c0dd9f95467e9e0a1
Patch0:		http://www.version6.net/mythtv/%{name}-grab_ee-20050412.diff
#Patch0:		%{name}-0.5.35-noask.patch
#Patch1:		%{name}-0.5.40-tv_grab_de_tvtoday.patch
URL:		http://membled.com/work/apps/xmltv/
BuildRequires:	perl(LWP) >= 5.65
BuildRequires:	perl-Date-Manip >= 5.42
BuildRequires:	perl-Memoize
BuildRequires:	perl-Storable >= 2.04
BuildRequires:	perl-XML-Parser >= 2.34
BuildRequires:	perl-XML-Twig >= 3.10
BuildRequires:	perl-XML-Writer >= 0.4.6
# Recommended
BuildRequires:	perl-Lingua-EN-Numbers-Ordinate
BuildRequires:	perl-Lingua-Preferred >= 0.2.4
BuildRequires:	perl-Term-ProgressBar >= 2.03
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-Unicode-String
# tv_grab_uk_rt, tv_grab_be, tv_grab_de_tvtoday, tv_grab_fr, tv_grab_no
# tv_grab_za
BuildRequires:	perl(HTML::Entities) >= 1.27
# tv_grab_uk_bleb
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl-Archive-Zip
# tv_grab_na_dd
BuildRequires:	perl-SOAP-Lite
BuildRequires:	perl-Term-ReadKey
# tv_grab_na_icons
BuildRequires:	perl-HTML-TableExtract >= 1.08
BuildRequires:	perl-WWW-Mechanize => 1.02
# tv_grab_fi, tv_grab_es, tv_grab_es_digital, tv_grab_nl
# tv_grab_nl_wolf, tv_grab_huro, tv_grab_dk, tv_grab_jp
# tv_grab_de_tvtoday, tv_grab_fr, tv_grab_pt, tv_grab_za
BuildRequires:	perl(HTML::TreeBuilder)
# tv_grab_jp
BuildRequires:	perl-Text-Kakasi
# tv_grab_se, tv_grab_se_swedb
BuildRequires:	perl-XML-LibXML
# tv_grab_se_swedb
BuildRequires:	perl-IO-stringy
BuildRequires:	perl-HTTP-Cache-Transparent
# tv_check
BuildRequires:	perl-Tk
BuildRequires:	perl-Tk-TableMatrix
# tv_pick_cgi
BuildRequires:	perl-CGI
###BuildRequires: perl-HTML-Parser >= 3.34
###BuildRequires: perl-XML-Simple
###BuildRequires: perl(PerIO::gzip)
###BuildRequires: perl-HTML-LinkExtractor
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-XMLTV = %{epoch}:%{version}-%{release}
Requires:	xmltv-grabbers = %{epoch}:%{version}-%{release}
Requires:	xmltv-gui = %{epoch}:%{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMLTV is a set of utilities to manage your TV viewing. They work with
TV listings stored in the XMLTV format, which is based on XML. The
idea is to separate out the backend (getting the listings) from the
frontend (displaying them for the user), and to implement useful
operations like picking out your favourite programmes as filters that
read and write XML documents.

%description -l pl
XMLTV to zestaw narzêdzi do zarz±dzania ogl±daniem TV. Dzia³aj± z
programami telewizyjnymi zapisanymi w formacie XMLTV opartym na XML-u.
Idea polega na oddzieleniu backendu (pobierania programów) od
frontendu (wy¶wietlania ich u¿ytkownikowi) oraz zaimplementowaniu
przydatnych operacji takich jak wybieranie ulubionych programów jako
filtrów czytaj±cych i zapisuj±cych dokumenty XML.

%package -n perl-XMLTV
Summary:	Perl modules for managing your TV viewing
Summary(pl):	Modu³y Perla do zarz±dzania ogl±daniem TV
Group:		Development/Languages/Perl
Requires:	perl-Date-Manip >= 5.41
Requires:	perl-XML-Twig >= 3.09
Requires:	perl-base >= 1:5.6.0

%description -n perl-XMLTV
XMLTV is a set of utilities to manage your TV viewing. They work with
TV listings stored in the XMLTV format, which is based on XML. The
idea is to separate out the backend (getting the listings) from the
frontend (displaying them for the user), and to implement useful
operations like picking out your favourite programmes as filters that
read and write XML documents.

This package contains the Perl modules from XMLTV.

%description -n perl-XMLTV -l pl
XMLTV to zestaw narzêdzi do zarz±dzania ogl±daniem TV. Dzia³aj± z
programami telewizyjnymi zapisanymi w formacie XMLTV opartym na XML-u.
Idea polega na oddzieleniu backendu (pobierania programów) od
frontendu (wy¶wietlania ich u¿ytkownikowi) oraz zaimplementowaniu
przydatnych operacji takich jak wybieranie ulubionych programów jako
filtrów czytaj±cych i zapisuj±cych dokumenty XML.

Ten pakiet zawiera modu³y Perla z XMLTV.

%package grabbers
Summary:	Backends for XMLTV
Summary(pl):	Backendy dla XMLTV
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{epoch}:%{version}-%{release}
Requires:	perl(LWP) >= 5.65
Requires:	perl-Date-Manip >= 5.41
Requires:	perl-HTML-TableExtract >= 1.08
Requires:	perl-Term-ProgressBar >= 2.00

%description grabbers
XMLTV is a set of utilities to manage your TV viewing. They work with
TV listings stored in the XMLTV format, which is based on XML. The
idea is to separate out the backend (getting the listings) from the
frontend (displaying them for the user), and to implement useful
operations like picking out your favourite programmes as filters that
read and write XML documents.

This package contains the backends (grabbers) for XMLTV.

%description grabbers -l pl
XMLTV to zestaw narzêdzi do zarz±dzania ogl±daniem TV. Dzia³aj± z
programami telewizyjnymi zapisanymi w formacie XMLTV opartym na XML-u.
Idea polega na oddzieleniu backendu (pobierania programów) od
frontendu (wy¶wietlania ich u¿ytkownikowi) oraz zaimplementowaniu
przydatnych operacji takich jak wybieranie ulubionych programów jako
filtrów czytaj±cych i zapisuj±cych dokumenty XML.

Ten pakiet zawiera backendy (programy do ¶ci±gania informacji) dla
XMLTV.

%package gui
Summary:	Graphical frontends to XMLTV
Summary(pl):	Graficzne frontendy dla XMLTV
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

This package contains graphical frontends to XMLTV.

%description gui -l pl
XMLTV to zestaw narzêdzi do zarz±dzania ogl±daniem TV. Dzia³aj± z
programami telewizyjnymi zapisanymi w formacie XMLTV opartym na XML-u.
Idea polega na oddzieleniu backendu (pobierania programów) od
frontendu (wy¶wietlania ich u¿ytkownikowi) oraz zaimplementowaniu
przydatnych operacji takich jak wybieranie ulubionych programów jako
filtrów czytaj±cych i zapisuj±cych dokumenty XML.

Ten pakiet zawiera graficzne frontendy dla XMLTV.

%prep
%setup -q
%patch0 -p0
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
%attr(755,root,root) %{_bindir}/tv_cat
%attr(755,root,root) %{_bindir}/tv_extractinfo_en
%attr(755,root,root) %{_bindir}/tv_grep
%attr(755,root,root) %{_bindir}/tv_imdb
%attr(755,root,root) %{_bindir}/tv_remove_some_overlapping
%attr(755,root,root) %{_bindir}/tv_sort
%attr(755,root,root) %{_bindir}/tv_split
%attr(755,root,root) %{_bindir}/tv_to_latex
%attr(755,root,root) %{_bindir}/tv_to_text
%attr(755,root,root) %{_bindir}/tv_to_potatoe
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
%attr(755,root,root) %{_bindir}/tv_grab_*
%{_mandir}/man1/tv_grab_*.1*
#%dir %{_datadir}/xmltv
#%{_datadir}/xmltv/tv_grab_*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_check
%{_mandir}/man1/tv_check.1*
