%define		devel	3
Summary:	A minimal & complete Object-Oriented (OO) thread interface
Summary(pl):	Minimalny ale kompletny interfejs w±tków w programowaniu OO
Name:		OpenThreads
Version:	1.2
Release:	0.%{devel}.2
License:	LGPL
Group:		Libraries
# version from OSG_OP_OT-0.9.6-2.tar.gz needed to build new OpenSceneGraph
# Source0:	http://dl.sourceforge.net/openthreads/%{name}-v%{version}dev%{devel}-osg0.9.5.tar.gz
Source0:	OpenThreads-v%{version}dev%{devel}.tar.gz
# Source0-md5:  0a1c190e358459aa4a2f1018dc397be5
Patch0:		%{name}-soname.patch
URL:		http://openthreads.sourceforge.net/
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library is intended to provide a minimal & complete
Object-Oriented (OO) thread interface for C++ programmers. It is
loosely modeled on the Java thread API, and the POSIX Threads
standards.

%description -l pl
Biblioteka jest przeznaczona do udostêpniania minimalnego ale pe³nego
interfejsu obiektowo zorientowanych (OO) w±tków dla programistów C++.
Bazuje na modelu API w±tków w Javie oraz na standardzie w±tków POSIX.

%package devel
Summary:	OpenThreads devel files
Summary(pl):	Biblioteki programistyczne OpenThreads
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

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
