%global tl_name eskdx
%global tl_revision 29235

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.98
Release:	%{tl_revision}.1
Summary:	Modern Russian typesetting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/eskdx
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eskdx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eskdx.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Eskdx is a collection of LaTeX classes and packages to typeset textual
and graphical documents in accordance with Russian (and probably post
USSR) standards for designers.

