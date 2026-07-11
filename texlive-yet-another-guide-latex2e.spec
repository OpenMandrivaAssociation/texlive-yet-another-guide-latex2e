%global tl_name yet-another-guide-latex2e
%global tl_revision 77842

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3.2
Release:	%{tl_revision}.1
Summary:	A short guide to using LaTeX2e to typeset high quality documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/yet-another-guide-latex2e
License:	fdl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yet-another-guide-latex2e.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yet-another-guide-latex2e.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This document is a short guide to using LaTeX2e to typeset high quality
documents. It focuses on users of Windows and guides the reader through
installation, some of LaTeX's conventions, and creating the front
matter, body and end matter. The appendices contain a list of useful
facilities not otherwise covered in this document and a list of helpful
resources.

