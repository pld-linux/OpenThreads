%define		devel	2
Summary:	A minimal & complete Object-Oriented (OO) thread interface
Summary(pl):	Minimalny ale kompletny interfejs w±tków w programowaniu OO
Name:		OpenThreads
Version:	1.2
Release:	0.%{devel}.1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/openthreads/%{name}-v%{version}dev%{devel}-osg0.9.5.tar.gz
URL:		http://openthreads.sourceforge.net
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library is intended to provide a minimal & complete
Object-Oriented (OO) thread interface for C++ programmers. It is
loosely modeled on the Java thread API, and the POSIX Threads
standards.

%description -l pl
Biblioteka jest przeznaczona do udostêpniania minimalnego ale pe³nego
interfejsu obiektowo zorientowanych (OO) w±tków dla programistów C++.
Bazuje na modelu API w±tków w javie oraz na standardzie w±tków POSIX.

%package devel
Summary:	OpenThreads devel files
Summary(pl):	Biblioteki programistyczne OpenThreads
Group:		Development/Libraries

%description devel
OpenThreads devel files.

%description devel -l pl
Biblioteki programistyczne OpenThreads.

%prep
%setup -q -n %{name}

%build
%{__make} \
	CXX="%{__cxx} %{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install \
	INST_LOCATION=$RPM_BUILD_ROOT%{_prefix}
mv $RPM_BUILD_ROOT%{_prefix}/lib/libOpenThreads.so $RPM_BUILD_ROOT%{_libdir}/libOpenThreads.so.0
ln -sf libOpenThreads.so.0 $RPM_BUILD_ROOT%{_libdir}/libOpenThreads.so

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib%{name}.so.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS.txt ChangeLog README.txt TODO.txt
%attr(755,root,root) %{_libdir}/lib%{name}.so
%{_includedir}/%{name}
