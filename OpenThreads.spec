Summary:	A minimal & complete Object-Oriented (OO) thread interface
Summary(pl):	Minimalny ale kompletny interfejs w�tk�w w programowaniu OO
Name:		OpenThreads
Version:	1.3
Release:	0.1
License:	LGPL
Group:		Libraries
# version from OSG_OP_OT-0.9.6-2.tar.gz needed to build new OpenSceneGraph
# Source0:	http://dl.sourceforge.net/openthreads/%{name}-v%{version}dev%{devel}-osg0.9.5.tar.gz
#Source0:	OpenThreads-v%{version}dev%{devel}.tar.gz
Source0:	http://dl.sourceforge.net/openscenegraph/%{name}-%{version}.tar.gz
# Source0-md5:	a1d792ae4ce38590ff498e0c7d9ad939
Source1:	%{name}.pc
Patch0:		%{name}-soname.patch
URL:		http://openthreads.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library is intended to provide a minimal & complete
Object-Oriented (OO) thread interface for C++ programmers. It is
loosely modeled on the Java thread API, and the POSIX Threads
standards.

%description -l pl
Biblioteka jest przeznaczona do udost�pniania minimalnego ale pe�nego
interfejsu obiektowo zorientowanych (OO) w�tk�w dla programist�w C++.
Bazuje na modelu API w�tk�w w Javie oraz na standardzie w�tk�w POSIX.

%package devel
Summary:	OpenThreads devel files
Summary(pl):	Biblioteki programistyczne OpenThreads
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
OpenThreads devel files.

%description devel -l pl
Biblioteki programistyczne OpenThreads.

%prep
%setup -q -n %{name}
%patch0 -p0

%build
%{__make} \
	CXX="%{__cxx} %{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INST_LOCATION=$RPM_BUILD_ROOT%{_prefix}
if [ "%{_libdir}" == "%{_prefix}/lib64" ]; then
	mv $RPM_BUILD_ROOT{%{_prefix}/lib,%{_libdir}}
fi
ln -sf `basename $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so.*` $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so
install -d $RPM_BUILD_ROOT%{_pkgconfigdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_pkgconfigdir}/openthreads.pc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib%{name}.so.*.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS.txt ChangeLog README.txt TODO.txt
%attr(755,root,root) %{_libdir}/lib%{name}.so
%{_includedir}/%{name}
%{_pkgconfigdir}/openthreads.pc
