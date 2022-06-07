#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-google_api_python_client
Version  : 2.50.0
Release  : 89
URL      : https://files.pythonhosted.org/packages/67/e0/edf2d40f4eb1080017447a09559d7598139a2996f4e099a101526ab05b75/google-api-python-client-2.50.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/67/e0/edf2d40f4eb1080017447a09559d7598139a2996f4e099a101526ab05b75/google-api-python-client-2.50.0.tar.gz
Summary  : Google API Client Library for Python
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-google_api_python_client-license = %{version}-%{release}
Requires: pypi-google_api_python_client-python = %{version}-%{release}
Requires: pypi-google_api_python_client-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(google_api_core)
BuildRequires : pypi(google_auth)
BuildRequires : pypi(google_auth_httplib2)
BuildRequires : pypi(httplib2)
BuildRequires : pypi(uritemplate)

%description
# Google API Client
[![PyPI version](https://badge.fury.io/py/google-api-python-client.svg)](https://badge.fury.io/py/google-api-python-client)

%package license
Summary: license components for the pypi-google_api_python_client package.
Group: Default

%description license
license components for the pypi-google_api_python_client package.


%package python
Summary: python components for the pypi-google_api_python_client package.
Group: Default
Requires: pypi-google_api_python_client-python3 = %{version}-%{release}

%description python
python components for the pypi-google_api_python_client package.


%package python3
Summary: python3 components for the pypi-google_api_python_client package.
Group: Default
Requires: python3-core
Provides: pypi(google_api_python_client)
Requires: pypi(google_api_core)
Requires: pypi(google_auth)
Requires: pypi(google_auth_httplib2)
Requires: pypi(httplib2)
Requires: pypi(uritemplate)

%description python3
python3 components for the pypi-google_api_python_client package.


%prep
%setup -q -n google-api-python-client-2.50.0
cd %{_builddir}/google-api-python-client-2.50.0
pushd ..
cp -a google-api-python-client-2.50.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1654611806
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-google_api_python_client
cp %{_builddir}/google-api-python-client-2.50.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-google_api_python_client/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-google_api_python_client/7df059597099bb7dcf25d2a9aedfaf4465f72d8d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
