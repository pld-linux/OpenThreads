Summary:	A minimal & complete Object-Oriented (OO) thread interface
Summary(pl):	Minimalny ale kompletny interfejs w±tków w programowaniu OO
Name:		OpenThreads
Version:	1.3
Release:	1
License:	LGPL
Group:		Libraries
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
Biblioteka jest przeznaczona do udostêpniania minimalnego ale pe³nego
interfejsu obiektowo zorientowanych (OO) w±tków dla programistów C++.
Bazuje na modelu API w±tków w Javie oraz na standardzie w±tków POSIX.

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
	INST_LOCATION=$RPM_BUILD_ROOT%{_prefix} \
	INST_LIBS=$RPM_BUILD_ROOT%{_libdir}

ln -sf `basename $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so.*` $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so

install -d $RPM_BUILD_ROOT%{_pkgconfigdir}
sed -e 's/^libdir=.*/libdir=%{_libdir}/' %{SOURCE1} >$RPM_BUILD_ROOT%{_pkgconfigdir}/openthreads.pc

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
