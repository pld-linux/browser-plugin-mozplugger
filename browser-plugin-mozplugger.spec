Summary:	Mozilla multimedia plugin
Summary(es):	Streaming Netscape Plugin
Summary(pl):	Wtyczka Mozilli do multimedi�w
Summary(pt_BR):	Plugin para o Netscape para streaming
Name:		mozilla-plugin-mozplugger
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.enseirb.fr/~bavoil/mozplugger/mozplugger-%{version}.tar.gz
Source1:	%{name}-npunix.c
Patch0:		%{name}-instance.patch
Patch1:		%{name}-pluggerrc.patch
URL:		http://fredrik.hubbe.net/plugger.html
Prereq:		mozilla-embedded
BuildRequires:	mozilla-embedded-devel
Obsoletes:	mozilla-plugin-plugger
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Plugger is a plugin which can show many types of multimedia inside
your Netscape or Mozilla-based browser (mozilla itself, galeon,
skipstone, light). To accomplish this, Plugger uses external programs
such as xanim, mtv, timidity and tracker.

%description -l es
Streaming Multimedia plugin for UNIX Netscape.

%description -l pl
Pakiet zawiera wtyczk�, kt�ra pozwala na wy�wietlanie wielu rodzaj�w
multimedi�w wewn�trz Netscape lub przegl�darki bazuj�cej na Mozilli
(mozilli jako takiej, galeona, skipstone'a, lighta). Aby to uzyska�,
Plugger u�ywa zewn�trznych program�w, takich jak xanim, mtv, timidity
czy tracker.

%description -l pt_BR
Plugin para o Netscape para streaming.

%prep
%setup -q -n mozplugger-%{version}
%patch0 -p1
#%patch1 -p1
mkdir common
cp -f %{SOURCE1} common/npunix.c

%build
CF="%{rpmcflags} -fpic -I%{_includedir}/mozilla"
CF="$CF -I%{_includedir}/mozilla/java -I/usr/include/nspr -I%{_includedir}/mozilla/plugin"
%{__make} all \
        XCFLAGS="$CF" NORM_CFLAGS="$CF" \
        XLDFLAGS=-shared \
	LDFLAGS="%{rpmldflags} -L/usr/X11R6/lib" \
        CC=%{__cc} LD=%{__cc} \
        SDK=. X11=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/mozilla/plugins,%{_bindir}} \
	$RPM_BUILD_ROOT{%{_mandir}/man7,%{_sysconfdir}}
install *.so $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins
install mozpluggerrc $RPM_BUILD_ROOT%{_sysconfdir}
install mozplugger-%{version} $RPM_BUILD_ROOT%{_bindir}
install *.7 $RPM_BUILD_ROOT%{_mandir}/man7
ln -sf mozpluggerrc $RPM_BUILD_ROOT%{_sysconfdir}/mozpluggerrc-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/mozilla/plugins/*.so
%{_mandir}/*/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mozpluggerrc
%{_sysconfdir}/mozpluggerrc-*
