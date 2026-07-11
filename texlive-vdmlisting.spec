%global tl_name vdmlisting
%global tl_revision 56905

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Typesetting VDM in ASCII syntax
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/vdmlisting
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vdmlisting.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vdmlisting.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is an extension for the listings package that provides a
source code printer for LaTeX. This package defines new language
definitions and listing environments for the three language dialects of
the Vienna Development Method: VDM-SL, VDM-PP and VDM-RT. If one wants
to typeset VDM with a mathematical syntax instead of the ASCII syntax
used here one should use the vdm pacakge instead

