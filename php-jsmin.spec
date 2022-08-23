#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-jsmin
Version  : 3.0.0
Release  : 18
URL      : https://pecl.php.net//get/jsmin-3.0.0.tgz
Source0  : https://pecl.php.net//get/jsmin-3.0.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.0
Requires: php-jsmin-lib = %{version}-%{release}
BuildRequires : buildreq-php
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

%description lib
lib components for the php-jsmin package.


%prep
%setup -q -n jsmin-3.0.0
cd %{_builddir}/jsmin-3.0.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/php/ext/jsmin/php_jsmin.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/jsmin.so
