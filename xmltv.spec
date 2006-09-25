#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
#
# TODO
# - patch and remove requirement on perl-Unicode-UTF8simple (we have perl 5.6+)
#
%include	/usr/lib/rpm/macros.perl
Summary:	A set of utilities to manage your TV viewing
Summary(pl):	Zestaw narzêdzi do zarz±dzania ogl±daniem TV
Name:		xmltv
Version:	0.5.44
Release:	1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/xmltv/%{name}-%{version}.tar.bz2
# Source0-md5:	d6832fe7e0460f7abda05b8b56566e99
Patch0:		%{name}-strip_dorkcode_from_Makefile_PL.patch
Patch1:		%{name}-tv_grab_ee.patch
URL:		http://xmltv.org/wiki/
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:	perl-Date-Manip >= 5.42
BuildRequires:	perl-XML-Parser >= 2.34
BuildRequires:	perl-XML-Twig >= 3.10
BuildRequires:	perl-XML-Writer >= 0.6
%if %{with autodeps}
BuildRequires:	perl-Archive-Zip
BuildRequires:	perl-CGI
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-HTML-Parser >= 1.27
BuildRequires:	perl-HTML-TableExtract >= 1.08
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-HTTP-Cache-Transparent
BuildRequires:	perl-IO-stringy
BuildRequires:	perl-Lingua-EN-Numbers-Ordinate
BuildRequires:	perl-Lingua-Preferred >= 0.2.4
BuildRequires:	perl-Locale-Hebrew
BuildRequires:	perl-Memoize
BuildRequires:	perl-SOAP-Lite
BuildRequires:	perl-Storable >= 2.04
BuildRequires:	perl-Term-ProgressBar >= 2.03
BuildRequires:	perl-Term-ReadKey
BuildRequires:	perl-Text-Kakasi
BuildRequires:	perl-Tk
BuildRequires:	perl-Tk-TableMatrix
BuildRequires:	perl-Unicode-String
BuildRequires:	perl-Unicode-UTF8simple
BuildRequires:	perl-WWW-Mechanize >= 1.02
BuildRequires:	perl-XML-LibXML >= 1.58-1.1
BuildRequires:	perl-libwww >= 5.65
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-XMLTV = %{version}-%{release}
Requires:	xmltv-grabbers = %{version}-%{release}
Requires:	xmltv-gui = %{version}-%{release}
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
Obsoletes:	xmltv-grabber-au
Obsoletes:	xmltv-grabber-ch
Obsoletes:	xmltv-grabber-de
Obsoletes:	xmltv-grabber-se

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
#Requires:	%{name}-grabber-au = %{version}-%{release}
Requires:	%{name}-grabber-be = %{version}-%{release}
Requires:	%{name}-grabber-br = %{version}-%{release}
#Requires:	%{name}-grabber-ch = %{version}-%{release}
#Requires:	%{name}-grabber-de = %{version}-%{release}
Requires:	%{name}-grabber-dk = %{version}-%{release}
Requires:	%{name}-grabber-ee = %{version}-%{release}
Requires:	%{name}-grabber-es = %{version}-%{release}
Requires:	%{name}-grabber-fi = %{version}-%{release}
Requires:	%{name}-grabber-fr = %{version}-%{release}
Requires:	%{name}-grabber-huro = %{version}-%{release}
Requires:	%{name}-grabber-is = %{version}-%{release}
Requires:	%{name}-grabber-it = %{version}-%{release}
Requires:	%{name}-grabber-jp = %{version}-%{release}
Requires:	%{name}-grabber-na = %{version}-%{release}
Requires:	%{name}-grabber-nl = %{version}-%{release}
Requires:	%{name}-grabber-no = %{version}-%{release}
Requires:	%{name}-grabber-pt = %{version}-%{release}
Requires:	%{name}-grabber-re = %{version}-%{release}
#Requires:	%{name}-grabber-se = %{version}-%{release}
Requires:	%{name}-grabber-uk = %{version}-%{release}
Requires:	%{name}-grabber-za = %{version}-%{release}

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

%package grabber-au
Summary:	XMLTV grabber for Australia
Summary(pl):	Program ¶ci±gaj±cy informacje XMLTV dla Australii
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{version}-%{release}
Provides:	xmltv-grabbers = %{version}-%{release}

%description grabber-au
Grab TV listings for Australia.

%description grabber-au -l pl
Narzêdzie do ¶ci±gania programu telewizyjnego dla Australii.

%package grabber-be
Summary:	XMLTV grabber for Belgium
Summary(pl):	Program ¶ci±gaj±cy informacje XMLTV dla Belgii
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{version}-%{release}
Provides:	xmltv-grabbers = %{version}-%{release}

%description grabber-be
Grab TV listings for Belgium.

%description grabber-be -l pl
Narzêdzie do ¶ci±gania programu telewizyjnego dla Belgii.

%package grabber-br
Summary:	XMLTV grabber for Brasil
Summary(pl):	Program ¶ci±gaj±cy informacje XMLTV dla Brazylii
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{version}-%{release}
Provides:	xmltv-grabbers = %{version}-%{release}

%description grabber-br
Grab TV listings for Brasil.

%description grabber-br -l pl
Narzêdzie do ¶ci±gania programu telewizyjnego dla Brazylii.

%package grabber-ch
Summary:	XMLTV grabber for Switzerland
Summary(pl):	Program ¶ci±gaj±cy informacje XMLTV dla Szwajcarii
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{version}-%{release}
Provides:	xmltv-grabbers = %{version}-%{release}

%description grabber-ch
Grab TV listings for Switzerland and (partly) central Europe.

%description grabber-ch -l pl
Narzêdzie do ¶ci±gania programu telewizyjnego dla Szwajcarii oraz
(czê¶ciowo) Europy centralnej.

%package grabber-de
Summary:	XMLTV grabbers for Germany
Summary(pl):	Programy ¶ci±gaj±ce informacje XMLTV dla Niemiec
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{version}-%{release}
Provides:	xmltv-grabbers = %{version}-%{release}

%description grabber-de
Grab TV listings for Germany.

%description grabber-de -l pl
Narzêdzia do ¶ci±gania programu telewizyjnego dla Niemiec.

%package grabber-dk
Summary:	XMLTV grabber for Denmark
Summary(pl):	Program ¶ci±gaj±cy informacje XMLTV dla Danii
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{version}-%{release}
Provides:	xmltv-grabbers = %{version}-%{release}

%description grabber-dk
Grab TV listings for Denmark.

%description grabber-dk -l pl
Narzêdzie do ¶ci±gania programu telewizyjnego dla Danii.

%package grabber-ee
Summary:	XMLTV grabber for Estonia
Summary(pl):	Program ¶ci±gaj±cy informacje XMLTV dla Estonii
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{version}-%{release}
Provides:	xmltv-grabbers = %{version}-%{release}

%description grabber-ee
Grab TV listings for Estonia.

%description grabber-ee -l pl
Narzêdzie do ¶ci±gania programu telewizyjnego dla Estonii.

%package grabber-es
Summary:	XMLTV grabbers for Spain
Summary(pl):	Programy ¶ci±gaj±ce informacje XMLTV dla Hiszpanii
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{version}-%{release}
Provides:	xmltv-grabbers = %{version}-%{release}

%description grabber-es
Grab TV listings for Spain.

%description grabber-es -l pl
Narzêdzia do ¶ci±gania programu telewizyjnego dla Hiszpanii.

%package grabber-fi
Summary:	XMLTV grabber for Finland
Summary(pl):	Program ¶ci±gaj±cy informacje XMLTV dla Finlandii
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{version}-%{release}
Provides:	xmltv-grabbers = %{version}-%{release}

%description grabber-fi
Grab TV listings for Finland.

%description grabber-fi -l pl
Narzêdzie do ¶ci±gania programu telewizyjnego dla Finlandii.

%package grabber-fr
Summary:	XMLTV grabber for France
Summary(pl):	Program ¶ci±gaj±cy informacje XMLTV dla Francji
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{version}-%{release}
Provides:	xmltv-grabbers = %{version}-%{release}

%description grabber-fr
Grab TV listings for France.

%description grabber-fr -l pl
Narzêdzie do ¶ci±gania programu telewizyjnego dla Francji.

%package grabber-huro
Summary:	XMLTV grabber for Hungary/Romania
Summary(pl):	Program ¶ci±gaj±cy informacje XMLTV dla Wêgier i Rumunii
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{version}-%{release}
Provides:	xmltv-grabbers = %{version}-%{release}

%description grabber-huro
Grab TV listings for Hungary or Romania.

%description grabber-huro -l pl
Narzêdzie do ¶ci±gania programu telewizyjnego dla Wêgier i Rumunii.

%package grabber-is
Summary:	XMLTV grabber for Iceland
Summary(pl):	Program ¶ci±gaj±cy informacje XMLTV dla Islandii
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{version}-%{release}
Provides:	xmltv-grabbers = %{version}-%{release}

%description grabber-is
Grab TV listings for Iceland.

%description grabber-is -l pl
Narzêdzie do ¶ci±gania programu telewizyjnego dla Islandii.

%package grabber-it
Summary:	XMLTV grabber for Italy
Summary(pl):	Program ¶ci±gaj±cy informacje XMLTV dla W³och
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{version}-%{release}
Provides:	xmltv-grabbers = %{version}-%{release}

%description grabber-it
Grab TV listings for Italy.

%description grabber-it -l pl
Narzêdzie do ¶ci±gania programu telewizyjnego dla W³och.

%package grabber-jp
Summary:	XMLTV grabber for Japan
Summary(pl):	Program ¶ci±gaj±cy informacje XMLTV dla Japonii
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{version}-%{release}
Provides:	xmltv-grabbers = %{version}-%{release}

%description grabber-jp
Grab TV listings for Japan.

%description grabber-jp -l pl
Narzêdzie do ¶ci±gania programu telewizyjnego dla Japonii.

%package grabber-na
Summary:	XMLTV grabbers for North America
Summary(pl):	Programy ¶ci±gaj±ce informacje XMLTV dla Ameryki Pó³nocnej
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{version}-%{release}
Provides:	xmltv-grabbers = %{version}-%{release}

%description grabber-na
Grab TV listings for North America using Zap2IT's Data Direct service.
Grab channel icon images or links from zap2it.com.

%description grabber-na -l pl
Narzêdzie do ¶ci±gania programu telewizyjnego dla Ameryki Pó³nocnej
przy u¿yciu us³ugi Zap2IT Data Direct oraz narzêdzie do pobierania
ikon lub odno¶ników z zap2it.com.

%package grabber-nl
Summary:	XMLTV grabbers for Netherlands
Summary(pl):	Programy ¶ci±gaj±ce informacje XMLTV dla Holandii
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{version}-%{release}
Provides:	xmltv-grabbers = %{version}-%{release}

%description grabber-nl
Grab TV listings for Netherlands.

%description grabber-nl -l pl
Narzêdzia do ¶ci±gania programu telewizyjnego dla Holandii.

%package grabber-no
Summary:	XMLTV grabber for Norway
Summary(pl):	Program ¶ci±gaj±cy informacje XMLTV dla Norwegii
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{version}-%{release}
Provides:	xmltv-grabbers = %{version}-%{release}

%description grabber-no
Grab TV listings for Norway.

%description grabber-no -l pl
Narzêdzie do ¶ci±gania programu telewizyjnego dla Norwegii.

%package grabber-pt
Summary:	XMLTV grabber for Portugal
Summary(pl):	Program ¶ci±gaj±cy informacje XMLTV dla Portugalii
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{version}-%{release}
Provides:	xmltv-grabbers = %{version}-%{release}

%description grabber-pt
Grab TV listings for Portugal.

%description grabber-pt -l pl
Narzêdzie do ¶ci±gania programu telewizyjnego dla Portugalii.

%package grabber-re
Summary:	XMLTV grabber for Reunion Island (France)
Summary(pl):	Program ¶ci±gaj±cy informacje XMLTV dla wyspy Reunion (Francja)
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{version}-%{release}
Provides:	xmltv-grabbers = %{version}-%{release}

%description grabber-re
Grab TV listings for Reunion Island (France).

%description grabber-re -l pl
Narzêdzie do ¶ci±gania programu telewizyjnego dla wyspy Reunion
(Francja).

%package grabber-se
Summary:	XMLTV grabbers for Sweden
Summary(pl):	Programy ¶ci±gaj±ce informacje XMLTV dla Szwecji
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{version}-%{release}
Provides:	xmltv-grabbers = %{version}-%{release}

%description grabber-se
Grab TV listings for Sweden.

%description grabber-se -l pl
Narzêdzia do ¶ci±gania programu telewizyjnego dla Szwecji.

%package grabber-uk
Summary:	XMLTV grabbers for United Kingdom and Ireland
Summary(pl):	Programy ¶ci±gaj±ce informacje XMLTV dla Wielkiej Brytanii i Irlandii
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{version}-%{release}
Provides:	xmltv-grabbers = %{version}-%{release}

%description grabber-uk
Grab TV listings for Britain and Ireland.

%description grabber-uk -l pl
Narzêdzia do ¶ci±gania programu telewizyjnego dla Wielkiej Brytanii i
Irlandii.

%package grabber-za
Summary:	XMLTV grabber for South Africa
Summary(pl):	Program ¶ci±gaj±cy informacje XMLTV dla Afryki Po³udniowej
Group:		Applications/Multimedia
Requires:	perl-XMLTV = %{version}-%{release}
Provides:	xmltv-grabbers = %{version}-%{release}

%description grabber-za
Grab TV listings for South Africa.

%description grabber-za -l pl
Narzêdzia do ¶ci±gania programu telewizyjnego dla Afryki Po³udniowej.

%package gui
Summary:	Graphical frontends to XMLTV
Summary(pl):	Graficzne frontendy dla XMLTV
Group:		Applications/Multimedia
Requires:	perl(LWP) >= 5.65
Requires:	perl-Date-Manip >= 5.41
Requires:	perl-XMLTV = %{version}-%{release}

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
%patch1 -p0

%build
rm -f Makefile
%{__perl} Makefile.PL -yes \
	PREFIX=%{_prefix} \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/XMLTV/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog xmltv.dtd
%attr(755,root,root) %{_bindir}/tv_cat
%attr(755,root,root) %{_bindir}/tv_extractinfo_en
%attr(755,root,root) %{_bindir}/tv_find_grabbers
%attr(755,root,root) %{_bindir}/tv_grab_br_net
%attr(755,root,root) %{_bindir}/tv_grab_de_tvtoday
%attr(755,root,root) %{_bindir}/tv_grab_es_laguiatv
%attr(755,root,root) %{_bindir}/tv_grab_il
%attr(755,root,root) %{_bindir}/tv_grab_se_swedb
%attr(755,root,root) %{_bindir}/tv_grep
%attr(755,root,root) %{_bindir}/tv_imdb
%attr(755,root,root) %{_bindir}/tv_remove_some_overlapping
%attr(755,root,root) %{_bindir}/tv_sort
%attr(755,root,root) %{_bindir}/tv_split
%attr(755,root,root) %{_bindir}/tv_to_latex
%attr(755,root,root) %{_bindir}/tv_to_potatoe
%attr(755,root,root) %{_bindir}/tv_to_text
%attr(755,root,root) %{_bindir}/tv_validate_file
%attr(755,root,root) %{_bindir}/tv_validate_grabber
%{_mandir}/man1/tv_cat.1*
%{_mandir}/man1/tv_extractinfo_en.1*
%{_mandir}/man1/tv_find_grabbers.1p*
%{_mandir}/man1/tv_grab_de_tvtoday.1p*
%{_mandir}/man1/tv_grab_il.1p*
%{_mandir}/man1/tv_grab_se_swedb.1p*
%{_mandir}/man1/tv_grep.1*
%{_mandir}/man1/tv_imdb.1*
%{_mandir}/man1/tv_remove_some_overlapping.1*
%{_mandir}/man1/tv_sort.1*
%{_mandir}/man1/tv_split.1*
%{_mandir}/man1/tv_to_latex.1*
%{_mandir}/man1/tv_to_potatoe.1*
%{_mandir}/man1/tv_to_text.1*
%{_mandir}/man1/tv_validate_file.1p*
%{_mandir}/man1/tv_validate_grabber.1p*

%files -n perl-XMLTV
%defattr(644,root,root,755)
%{perl_vendorlib}/XMLTV.pm
%{perl_vendorlib}/XMLTV
%{_mandir}/man3/*

%files grabbers
%defattr(644,root,root,755)

%if 0
%files grabber-au
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_au
%{_mandir}/man1/tv_grab_au*
%endif

%files grabber-be
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_be
%{_mandir}/man1/tv_grab_be*

%files grabber-br
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_br
%{_mandir}/man1/tv_grab_br*

%if 0
%files grabber-ch
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_ch
%{_mandir}/man1/tv_grab_ch*
%endif

%if 0
%files grabber-de
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_de
%attr(755,root,root) %{_bindir}/tv_grab_de_tvtoday
%{_mandir}/man1/tv_grab_de*
%endif

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

%files grabber-is
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_is
%{_mandir}/man1/tv_grab_is*

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

%files grabber-re
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_re
%{_mandir}/man1/tv_grab_re*

%if 0
%files grabber-se
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tv_grab_se
%attr(755,root,root) %{_bindir}/tv_grab_se_swedb
%{_mandir}/man1/tv_grab_se*
%endif

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
