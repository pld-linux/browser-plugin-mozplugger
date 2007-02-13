Summary:	Mozilla multimedia plugin
Summary(pl.UTF-8):	Wtyczka Mozilli do multimediów
Summary(pt_BR.UTF-8):	Plugin para o Netscape para streaming
Name:		mozilla-plugin-mozplugger
Version:	1.7.3
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://mozplugger.mozdev.org/files/mozplugger-%{version}.tar.gz
# Source0-md5:	5b56c7c598e9609d9dca3d7c3a88e124
URL:		http://mozplugger.mozdev.org/
BuildRequires:	XFree86-devel
BuildRequires:	mozilla-embedded-devel
Requires:	m4
Requires:	mozilla-embedded
Obsoletes:	mozilla-plugin-plugger
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugger is a plugin which can show many types of multimedia inside
your Netscape or Mozilla-based browser (mozilla itself, galeon,
skipstone, light). To accomplish this, Plugger uses external programs
such as xanim, mtv, timidity and tracker.

%description -l pl.UTF-8
Pakiet zawiera wtyczkę, która pozwala na wyświetlanie wielu rodzajów
multimediów wewnątrz Netscape lub przeglądarki bazującej na Mozilli
(mozilli jako takiej, galeona, skipstone'a, lighta). Aby to uzyskać,
Plugger używa zewnętrznych programów, takich jak xanim, mtv, timidity
czy tracker.

%description -l pt_BR.UTF-8
Plugin para o Netscape para streaming.

%prep
%setup -q -n mozplugger-%{version}
bunzip2 mozplugger.7.bz2

%build
CF="%{rpmcflags} -fpic -I%{_includedir}/mozilla"
CF="$CF -I%{_includedir}/mozilla/java -I/usr/include/nspr -I%{_includedir}/mozilla/plugin"
%{__make} all \
        XCFLAGS="$CF" NORM_CFLAGS="$CF" \
        XLDFLAGS=-shared \
	LDFLAGS="%{rpmldflags} -L/usr/X11R6/%{_lib}" \
        CC="%{__cc}" LD="%{__cc}" \
        SDK=. X11=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/mozilla/plugins,%{_bindir}} \
	$RPM_BUILD_ROOT{%{_mandir}/man7,%{_sysconfdir}}
install *.so $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins
install mozpluggerrc $RPM_BUILD_ROOT%{_sysconfdir}
install mozplugger-controller $RPM_BUILD_ROOT%{_bindir}
install mozplugger-helper $RPM_BUILD_ROOT%{_bindir}
install mozplugger.7 $RPM_BUILD_ROOT%{_mandir}/man7
ln -sf mozpluggerrc $RPM_BUILD_ROOT%{_sysconfdir}/mozpluggerrc-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/mozilla/plugins/*.so
%{_mandir}/*/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mozpluggerrc
%{_sysconfdir}/mozpluggerrc-*
