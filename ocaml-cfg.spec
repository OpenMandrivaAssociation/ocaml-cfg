Name:		ocaml-cfg
Version:	1.7.5
Release:        %mkrel 2
Summary:        Library for manipulation of context-free grammars (CFGs)
License:        LGPL
Group:          Development/Other
URL:		http://ocaml.info/home/ocaml_sources.html#cfg
Source0:	http://hg.ocaml.info/release/cfg/archive/cfg-release-%{version}.tar.bz2
# curl http://hg.ocaml.info/release/cfg/archive/release-%{version}.tar.bz2 > cfg-release-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  tetex-latex
BuildRequires:  gzip

%description
This OCaml-library consists of a set of modules which implement functions
for manipulating context-free grammars (CFGs) in a purely functional way.

The core-module (cfg_impl.ml) contains a functor which allows the
parameterization of the main transformation functions with arbitrary grammar
entities that fill the demanded specification (see the interface in
"cfg_intf.mli" and the BNF-example).

Thus, you may use this module for any kind of symbol system and any kind of
representation which can be treated like a CFG.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n cfg-release-%{version}

%build
make
make doc
gzip --best doc/cfg/latex/doc.ps

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR/cfg
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE
%dir %{_libdir}/ocaml/cfg
%{_libdir}/ocaml/cfg/META
%{_libdir}/ocaml/cfg/*.cma
%{_libdir}/ocaml/cfg/*.cmi

%files devel
%defattr(-,root,root)
%doc README.txt LICENSE Changes  
%doc doc/cfg/html
%doc doc/cfg/latex/*.{dvi,pdf,ps.gz}
%doc examples
%{_libdir}/ocaml/cfg/*.a
%{_libdir}/ocaml/cfg/*.cmxa
%{_libdir}/ocaml/cfg/*.mli

