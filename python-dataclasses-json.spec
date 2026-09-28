Name:		python-dataclasses-json
Version:	0.6.7
Release:	1
Summary:	Easily serialize dataclasses to and from JSON
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/dataclasses-json/
Source0:	dataclasses_json-0.6.7.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(poetry-dynamic-versioning)
BuildArch:	noarch
%description
Easily serialize dataclasses to and from JSON.

%files
%{py_sitedir}/*
