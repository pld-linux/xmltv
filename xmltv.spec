%include	/usr/lib/rpm/macros.perl
Summary:	A set of utilities to manage your TV viewing
Summary(pl):	Zestaw narzêdzi do zarz±dzania ogl±daniem TV
Name:		xmltv
Version:	0.5.40
Release:	1.4
Group:		Applications/Multimedia
License:	GPL v2
Source0:	http://dl.sourceforge.net/xmltv/%{name}-%{version}.tar.bz2
# Source0-md5:	5cf460444846217c0dd9f95467e9e0a1
Source1:	%{name}.dtd
Patch0:		http://www.version6.net/mythtv/%{name}-grab_ee-20050412.diff
Patch1:		%{name}-mm-version.patch
URL:		http://membled.com/work/apps/xmltv/
BuildRequires:	perl-Archive-Zip
BuildRequires:	perl-CGI
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-Date-Manip >= 5.42
BuildRequires:	perl-HTML-Parser >= 1.27
BuildRequires:	perl-HTML-TableExtract >= 1.08
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-HTTP-Cache-Transparent
BuildRequires:	perl-IO-stringy
BuildRequires:	perl-IO-stringy
BuildRequires:	perl-Lingua-EN-Numbers-Ordinate
BuildRequires:	perl-Lingua-Preferred >= 0.2.4
BuildRequires:	perl-Memoize
BuildRequires:	perl-SOAP-Lite
BuildRequires:	perl-Storable >= 2.04
BuildRequires:	perl-Term-ProgressBar >= 2.03
BuildRequires:	perl-Term-ReadKey
BuildRequires:	perl-Text-Kakasi
BuildRequires:	perl-Tk
BuildRequires:	perl-Tk-TableMatrix
BuildRequires:	perl-Unicode-String
BuildRequires:	perl-WWW-Mechanize => 1.02
BuildRequires:	perl-XML-LibXML >= 1.58-1.1
BuildRequires:	perl-XML-Parser >= 2.34
BuildRequires:	perl-XML-Twig >= 3.10
BuildRequires:	perl-XML-Writer >= 0.4.6
BuildRequires:	perl-devel >= 1:5.8.7-4
BuildRequires:	perl-libwww >= 5.65
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
Requires:	%{name}-grabber-be = %{epoch}:%{version}-%{release}
Requires:	%{name}-grabber-de = %{epoch}:%{version}-%{release}
Requires:	%{name}-grabber-dk = %{epoch}:%{version}-%{release}
Requires:	%{name}-grabber-ee = %{epoch}:%{version}-%{release}
Requires:	%{name}-grabber-es = %{epoch}:%{version}-%{release}
Requires:	%{name}-grabber-fi = %{epoch}:%{version}-%{release}
Requires:	%{name}-grabber-fr = %{epoch}:%{version}-%{release}
Requires:	%{name}-grabber-huro = %{epoch}:%{version}-%{release}
Requires:	%{name}-grabber-it = %{epoch}:%{version}-%{release}
Requires:	%{name}-grabber-jp = %{epoch}:%{version}-%{release}
Requires:	%{name}-grabber-na = %{epoch}:%{version}-%{release}
Requires:	%{name}-grabber-nl = %{epoch}:%{version}-%{release}
Requires:	%{name}-grabber-no = %{epoch}:%{version}-%{release}
Requires:	%{name}-grabber-pt = %{epoch}:%{version}-%{release}
Requires:	%{name}-grabber-se = %{epoch}:%{version}-%{release}
Requires:	%{name}-grabber-uk = %{epoch}:%{version}-%{release}
Requires:	%{name}-grabber-za = %{epoch}:%{version}-%{release}

%description grabbers
XMLTV is a set of utilities to manage your TV viewing. They work with
TV listings stored in the XMLTV format, which is based on XML. The
idea is to separate out the backend (getting the listings) from the
frontend (displaying them for the user), and to implement useful
operations like picking out your favourite programmes as filters that
read and write XML documents.

This package contains all backends (grabbers) for XMLTV. If you want
only one for your country, just install that package.

%description grabbers -l pl
XMLTV to zestaw narzêdzi do zarz±dzania ogl±daniem TV. Dzia³aj± z
programami telewizyjnymi zapisanymi w formacie XMLTV opartym na XML-u.
Idea polega na oddzieleniu backendu (pobierania programów) od
frontendu (wy¶wietlania ich u¿ytkownikowi) oraz zaimplementowaniu
przydatnych operacji takich jak wybieranie ulubionych programów jako
filtrów czytaj±cych i zapisuj±cych dokumenty XML.

Ten pakiet zawiera backendy (programy do ¶ci±gania informacji) dla
XMLTV.

%package grabber-be
Summary:	XMLTV grabber for Belgium
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{epoch}:%{version}-%{release}

%description grabber-be
Grab TV listings for Belgium

%package grabber-de
Summary:	XMLTV grabbers for Germany
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{epoch}:%{version}-%{release}

%description grabber-de
Grab TV listings for Germany.

%package grabber-dk
Summary:	XMLTV grabber for Denmark
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{epoch}:%{version}-%{release}

%description grabber-dk
Grab TV listings for Denmark.

%package grabber-ee
Summary:	XMLTV grabber for Estonia
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{epoch}:%{version}-%{release}

%description grabber-ee
Grab TV listings for Estonia.

%package grabber-es
Summary:	XMLTV grabbers for Spain
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{epoch}:%{version}-%{release}

%description grabber-es
Grab TV listings for Spain.

%package grabber-fi
Summary:	XMLTV grabbers for Finland
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{epoch}:%{version}-%{release}

%description grabber-fi
Grab TV listings for Finland.

%package grabber-fr
Summary:	XMLTV grabbers for France
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{epoch}:%{version}-%{release}

%description grabber-fr
Grab TV listings for France.

%package grabber-huro
Summary:	XMLTV grabber for Hungary/Romania
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{epoch}:%{version}-%{release}

%description grabber-huro
Grab TV listings for Hungary or Romania.

%package grabber-it
Summary:	XMLTV grabbe for Italy
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{epoch}:%{version}-%{release}

%description grabber-it
Grab TV listings for Italy.

%package grabber-jp
Summary:	XMLTV grabbe for Japan
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{epoch}:%{version}-%{release}

%description grabber-jp
Grab TV listings for Japan.

%package grabber-na
Summary:	XMLTV grabber for North America
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{epoch}:%{version}-%{release}

%description grabber-na
Grab TV listings for North America using Zap2IT's Data Direct service.
Grab channel icon images or links from zap2it.com.

%package grabber-nl
Summary:	XMLTV grabber for Netherlands
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{epoch}:%{version}-%{release}

%description grabber-nl
Grab TV listings for Holland.

%package grabber-no
Summary:	XMLTV grabber for Norway
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{epoch}:%{version}-%{release}

%description grabber-no
Grab TV listings for Norway.

%package grabber-pt
Summary:	XMLTV grabber for Portugal
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{epoch}:%{version}-%{release}

%description grabber-pt
Grab TV listings for Portugal.

%package grabber-se
Summary:	XMLTV grabbers for Sweden
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{epoch}:%{version}-%{release}

%description grabber-se
Grab TV listings for Sweden.

%package grabber-uk
Summary:	XMLTV grabber for United Kingdom and Ireland
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{epoch}:%{version}-%{release}

%description grabber-uk
Grab TV listings for Britain and Ireland.

%package grabber-za
Summary:	XMLTV grabber for South Africa
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{epoch}:%{version}-%{release}

%description grabber-za
Grab TV listings for South Africa.

%package gui
Summary:	Graphical frontends to XMLTV
Summary(pl):	Graficzne frontendy dla XMLTV
Group:		Applications/Multimedia
Requires:	perl(LWP) >= 5.65
Requires:	perl-Date-Manip >= 5.41
Requires:	perl-XMLTV = %{epoch}:%{version}-%{release}

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
%patch1 -p1

cp %{SOURCE1} .

%build
%{__perl} Makefile.PL -yes \
	PREFIX=%{_prefix} \
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
%doc README ChangeLog xmltv.dtd
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

%files grabber-be
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_be
%{_mandir}/man1/tv_grab_be*

%files grabber-de
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_de
%attr(755,root,root) %{_bindir}/tv_grab_de_tvtoday
%{_mandir}/man1/tv_grab_de*

%files grabber-dk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_dk
%{_mandir}/man1/tv_grab_dk*

%files grabber-ee
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_ee
%{_mandir}/man1/tv_grab_ee*

%files grabber-es
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_es
%attr(755,root,root) %{_bindir}/tv_grab_es_digital
%{_mandir}/man1/tv_grab_es*

%files grabber-fi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_fi
%{_mandir}/man1/tv_grab_fi*

%files grabber-fr
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_fr
%{_mandir}/man1/tv_grab_fr*

%files grabber-huro
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_huro
%{_mandir}/man1/tv_grab_huro*

%files grabber-it
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_it
%{_mandir}/man1/tv_grab_it*

%files grabber-jp
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_jp
%{_mandir}/man1/tv_grab_jp*

%files grabber-na
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_na_dd
%attr(755,root,root) %{_bindir}/tv_grab_na_icons
%{_mandir}/man1/tv_grab_na*

%files grabber-nl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_nl
%attr(755,root,root) %{_bindir}/tv_grab_nl_wolf
%{_mandir}/man1/tv_grab_nl*

%files grabber-no
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_no
%{_mandir}/man1/tv_grab_no*

%files grabber-pt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_pt
%{_mandir}/man1/tv_grab_pt*

%files grabber-se
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_se
%attr(755,root,root) %{_bindir}/tv_grab_se_swedb
%{_mandir}/man1/tv_grab_se*

%files grabber-uk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_uk_bleb
%attr(755,root,root) %{_bindir}/tv_grab_uk_rt
%{_mandir}/man1/tv_grab_uk*

%files grabber-za
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_za
%{_mandir}/man1/tv_grab_za*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_check
%{_mandir}/man1/tv_check.1*
