%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Library for manipulation of context-free grammars (CFGs)
Name:		ocaml-cfg
Version:	2.0.1
Release:	1
License:	LGPL with static compilation exception
Group:		Development/Other
Url:		https://bitbucket.org/mmottl/cfg
Source0:	https://bitbucket.org/mmottl/cfg/downloads/cfg-%{version}.tar.gz
BuildRequires:	menhir
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib
BuildRequires:	tetex-latex

%description
This OCaml-library consists of a set of modules which implement functions
for manipulating context-free grammars (CFGs) in a purely functional way.

The core-module (cfg_impl.ml) contains a functor which allows the
parameterization of the main transformation functions with arbitrary grammar
entities that fill the demanded specification (see the interface in
"cfg_intf.mli" and the BNF-example).

Thus, you may use this module for any kind of symbol system and any kind of
representation which can be treated like a CFG.

%files
%doc README.md COPYING.txt CHANGES.txt AUTHORS.txt
%dir %{_libdir}/ocaml/cfg
%{_libdir}/ocaml/cfg/META
%{_libdir}/ocaml/cfg/*.cmi
%{_libdir}/ocaml/cfg/*.cma
%{_libdir}/ocaml/cfg/*.cmxs

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc html/
%doc examples/
%{_libdir}/ocaml/cfg/*.a
%{_libdir}/ocaml/cfg/*.cmxa
%{_libdir}/ocaml/cfg/*.cmx
%{_libdir}/ocaml/cfg/*.mli
%{_libdir}/ocaml/cfg/*.ml

#----------------------------------------------------------------------------

%prep
%setup -q -n cfg-%{version}

%build
./configure
make
make doc
mv _build/API.docdir/ html

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR/cfg
make install

