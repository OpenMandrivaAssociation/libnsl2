%define major 2
%define libname %mklibname nsl %{major}

Summary:	Old version of the public client interface library for NIS(YP) and NIS+
Name:		libnsl2
Version:	1.3.0
Release:	1
License:	BSD and LGPLv2+
Group:		System/Libraries
Url:		https://github.com/thkukuk/libnsl
Source0:	https://github.com/thkukuk/libnsl/archive/v%{version}.tar.gz
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(libtirpc)

%description
This package contains and old version of the libnsl library.
This library contains the public client interface for NIS(YP) and NIS+.
This code was formerly part of glibc, but is now standalone to
be able to link against TI-RPC for IPv6 support.

%package -n %{libname}
Summary:	Public client interface library for NIS(YP) and NIS+
Group:		System/Libraries

%description -n %{libname}
This package contains the shared library for %{name}.

%prep
%autosetup -p1 -n libnsl-%{version}
autoreconf -fiv

%build
CONFIGURE_TOP="$PWD"
export CFLAGS="%{optflags} -fPIC"

%configure \
	--enable-shared \
	--enable-static

%make_build

%install
%make_install

# No need to ship -devel or -static files
# for an obsolete compat library. We just
# need to keep pam installing until rebuilds
# are complete.
rm -rf %{buildroot}%{_includedir} \
	%{buildroot}%{_libdir}/*.{so,a} \
	%{buildroot}%{_libdir}/pkgconfig

%files -n %{libname}
%{_libdir}/libnsl.so.%{major}*
