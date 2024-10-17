Name:		texlive-yet-another-guide-latex2e
Version:	68564
Release:	1
Summary:	A short guide to using LaTeX2e to typeset high quality documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/yet-another-guide-latex2e
License:	fdl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yet-another-guide-latex2e.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yet-another-guide-latex2e.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This document is a short guide to using LaTeX2e to typeset high
quality documents. It focuses on users of Windows and guides
the reader through installation, some of LaTeX's conventions,
and creating the front matter, body and end matter. The
appendices contain a list of useful facilities not otherwise
covered in this document and a list of helpful resources.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/yet-another-guide-latex2e

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
