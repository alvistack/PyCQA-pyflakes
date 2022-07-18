%global debug_package %{nil}

Name: python-pyflakes
Epoch: 100
Version: 2.3.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Passive checker of Python programs
License: MIT
URL: https://github.com/PyCQA/pyflakes/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Pyflakes is program to analyze Python programs and detect various
errors. It works by parsing the source file, not importing it, so it is
safe to use on modules with side effects. It's also much faster.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-pyflakes
Summary: Passive checker of Python programs
Requires: python3
Provides: python3-pyflakes = %{epoch}:%{version}-%{release}
Provides: python3dist(pyflakes) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pyflakes = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pyflakes) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pyflakes = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pyflakes) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pyflakes
Pyflakes is program to analyze Python programs and detect various
errors. It works by parsing the source file, not importing it, so it is
safe to use on modules with side effects. It's also much faster.

%files -n python%{python3_version_nodots}-pyflakes
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-pyflakes
Summary: Passive checker of Python programs
Requires: python3
Provides: python3-pyflakes = %{epoch}:%{version}-%{release}
Provides: python3dist(pyflakes) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pyflakes = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pyflakes) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pyflakes = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pyflakes) = %{epoch}:%{version}-%{release}

%description -n python3-pyflakes
Pyflakes is program to analyze Python programs and detect various
errors. It works by parsing the source file, not importing it, so it is
safe to use on modules with side effects. It's also much faster.

%files -n python3-pyflakes
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
