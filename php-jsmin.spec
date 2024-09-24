#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v3
# autospec commit: c1050fe
#
Name     : php-jsmin
Version  : 3.0.0
Release  : 66
URL      : https://pecl.php.net//get/jsmin-3.0.0.tgz
Source0  : https://pecl.php.net//get/jsmin-3.0.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.0
Requires: php-jsmin-lib = %{version}-%{release}
Requires: php-jsmin-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : perl(Getopt::Long)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: PHP-8.patch

%description
# jsmin - PHP extension for JavaScript minification
[![Build Status](https://api.travis-ci.org/sqmk/pecl-jsmin.svg?branch=master)](https://travis-ci.org/sqmk/pecl-jsmin)

%package dev
Summary: dev components for the php-jsmin package.
Group: Development
Requires: php-jsmin-lib = %{version}-%{release}
Provides: php-jsmin-devel = %{version}-%{release}
Requires: php-jsmin = %{version}-%{release}

%description dev
dev components for the php-jsmin package.


%package lib
Summary: lib components for the php-jsmin package.
Group: Libraries
Requires: php-jsmin-license = %{version}-%{release}

%description lib
lib components for the php-jsmin package.


%package license
Summary: license components for the php-jsmin package.
Group: Default

%description license
license components for the php-jsmin package.


%prep
%setup -q -n jsmin-3.0.0
cd %{_builddir}/jsmin-3.0.0
%patch -P 1 -p1
pushd ..
cp -a jsmin-3.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-jsmin
cp %{_builddir}/jsmin-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-jsmin/ed7acdc8f7b75b080a44c60ebd2317b9a3e96394 || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/php/ext/jsmin/php_jsmin.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20230831/jsmin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-jsmin/ed7acdc8f7b75b080a44c60ebd2317b9a3e96394
