#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Specifications for callback functions passed in to an API
Summary(pl.UTF-8):	Specyfikacje funkcji wywołań zwrotnych przekazywane do API
Name:		python-backcall
Version:	0.1.0
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/backcall/
Source0:	https://files.pythonhosted.org/packages/source/b/backcall/backcall-%{version}.tar.gz
# Source0-md5:	87ce0c7839808e6a3427d57df6a792e7
URL:		https://pypi.org/project/backcall/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If your code lets other people supply callback functions, it's
important to specify the function signature you expect, and check that
functions support that. Adding extra parameters later would break
other peoples code unless you're careful.

backcall provides a way of specifying the callback signature using a
prototype function.

%description -l pl.UTF-8
Jeśli kod wymaga od innych przekazywania funkcji wywołań zwrotnych
(callbacków), ważne jest określenie oczekiwanej sygnatury funkcji i
sprawdzenie, że funkcje je obsługują. Dodanie później dodatkowych
parametrów może zepsuć istniejący kod innych osób.

backcall zapewnia sposób określania sygnatury wywołań zwrotnych przy
użyciu funkcji prototypowej.

%package -n python3-backcall
Summary:	Specifications for callback functions passed in to an API
Summary(pl.UTF-8):	Specyfikacje funkcji wywołań zwrotnych przekazywane do API
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-backcall
If your code lets other people supply callback functions, it's
important to specify the function signature you expect, and check that
functions support that. Adding extra parameters later would break
other peoples code unless you're careful.

backcall provides a way of specifying the callback signature using a
prototype function.

%description -n python3-backcall -l pl.UTF-8
Jeśli kod wymaga od innych przekazywania funkcji wywołań zwrotnych
(callbacków), ważne jest określenie oczekiwanej sygnatury funkcji i
sprawdzenie, że funkcje je obsługują. Dodanie później dodatkowych
parametrów może zepsuć istniejący kod innych osób.

backcall zapewnia sposób określania sygnatury wywołań zwrotnych przy
użyciu funkcji prototypowej.

%prep
%setup -q -n backcall-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/backcall
%{py_sitescriptdir}/backcall-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-backcall
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/backcall
%{py3_sitescriptdir}/backcall-%{version}-py*.egg-info
%endif
