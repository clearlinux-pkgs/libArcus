#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libArcus
Version  : 4.8
Release  : 22
URL      : https://github.com/Ultimaker/libArcus/archive/4.8/libArcus-4.8.tar.gz
Source0  : https://github.com/Ultimaker/libArcus/archive/4.8/libArcus-4.8.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause LGPL-3.0
Requires: libArcus-lib = %{version}-%{release}
Requires: libArcus-license = %{version}-%{release}
Requires: libArcus-python = %{version}-%{release}
Requires: libArcus-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : protobuf-dev
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : sip-dev
Patch1: 0001-Use-PyQt5.sip.patch

%description
Arcus
=====
This library contains C++ code and Python3 bindings for creating a socket in a thread
and using this socket to send and receive messages based on the Protocol Buffers
library. It is designed to facilitate the communication between Cura and its
backend and similar code.

%package dev
Summary: dev components for the libArcus package.
Group: Development
Requires: libArcus-lib = %{version}-%{release}
Provides: libArcus-devel = %{version}-%{release}
Requires: libArcus = %{version}-%{release}

%description dev
dev components for the libArcus package.


%package lib
Summary: lib components for the libArcus package.
Group: Libraries
Requires: libArcus-license = %{version}-%{release}

%description lib
lib components for the libArcus package.


%package license
Summary: license components for the libArcus package.
Group: Default

%description license
license components for the libArcus package.


%package python
Summary: python components for the libArcus package.
Group: Default
Requires: libArcus-python3 = %{version}-%{release}
Provides: libarcus-python

%description python
python components for the libArcus package.


%package python3
Summary: python3 components for the libArcus package.
Group: Default
Requires: python3-core

%description python3
python3 components for the libArcus package.


%prep
%setup -q -n libArcus-4.8
cd %{_builddir}/libArcus-4.8
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605030292
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1605030292
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libArcus
cp %{_builddir}/libArcus-4.8/LICENSE %{buildroot}/usr/share/package-licenses/libArcus/2fa84abcb9ebd82e02a9ba263551d24b04e8c691
cp %{_builddir}/libArcus-4.8/cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/libArcus/ff3ed70db4739b3c6747c7f624fe2bad70802987
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/Arcus/ArcusExport.h
/usr/include/Arcus/Error.h
/usr/include/Arcus/MessageTypeStore.h
/usr/include/Arcus/Socket.h
/usr/include/Arcus/SocketListener.h
/usr/include/Arcus/Types.h
/usr/lib64/cmake/Arcus/Arcus-targets-relwithdebinfo.cmake
/usr/lib64/cmake/Arcus/Arcus-targets.cmake
/usr/lib64/cmake/Arcus/ArcusConfig.cmake
/usr/lib64/cmake/Arcus/ArcusConfigVersion.cmake
/usr/lib64/libArcus.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libArcus.so.1.1.0
/usr/lib64/libArcus.so.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libArcus/2fa84abcb9ebd82e02a9ba263551d24b04e8c691
/usr/share/package-licenses/libArcus/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
