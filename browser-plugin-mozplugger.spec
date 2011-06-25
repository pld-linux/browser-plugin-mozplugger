Summary:	Mozilla multimedia plugin
Summary(pl.UTF-8):	Wtyczka Mozilli do multimediów
Summary(pt_BR.UTF-8):	Plugin para o Netscape para streaming
Name:		browser-plugin-mozplugger
Version:	1.14.3
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://mozplugger.mozdev.org/files/mozplugger-%{version}.tar.gz
# Source0-md5:	ac2f916ac93c3b59dec2ebfc511d00a0
Patch0:		DESTDIR.patch
URL:		http://mozplugger.mozdev.org/
BuildRequires:	xulrunner-devel
Requires:	m4
Obsoletes:	mozilla-plugin-mozplugger
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
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PLUGINDIRS=%{_browserpluginsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_browser_plugins

%postun
if [ "$1" = "0" ]; then
	%update_browser_plugins
fi

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_browserpluginsdir}/*.so
%{_mandir}/*/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mozpluggerrc
%{_sysconfdir}/mozpluggerrc
