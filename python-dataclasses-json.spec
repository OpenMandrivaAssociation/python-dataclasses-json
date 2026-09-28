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

%prep -a
# Cooker has marshmallow 4. The 3.x pin and the field argument names
# are the marshmallow 3 API.
sed -i 's/marshmallow = ">=3.18.0,<4.0.0"/marshmallow = ">=3.18.0"/' pyproject.toml
sed -i "s/missing_key = 'missing' if infer_missing else 'default'/missing_key = 'load_default' if infer_missing else 'dump_default'/" dataclasses_json/mm.py

%description
Easily serialize dataclasses to and from JSON.

%files
%{py_sitedir}/*
