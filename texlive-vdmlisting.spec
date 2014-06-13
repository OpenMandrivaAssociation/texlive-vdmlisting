# revision 29944
# category Package
# catalog-ctan /macros/latex/contrib/vdmlisting
# catalog-date 2013-04-16 11:30:34 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-vdmlisting
Version:	1.0
Release:	6
Summary:	Typesetting VDM in ASCII syntax
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/vdmlisting
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vdmlisting.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vdmlisting.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is an extension for the listings package that
provides a source code printer for LaTeX. This package defines
new language definitions and listing environments for the three
language dialects of the Vienna Development Method: VDM-SL,
VDM-PP and VDM-RT. If one wants to typeset VDM with a
mathematical syntax instead of the ASCII syntax used here one
should use the vdm pacakge instead.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/vdmlisting/vdmlisting.sty
%doc %{_texmfdistdir}/doc/latex/vdmlisting/README
%doc %{_texmfdistdir}/doc/latex/vdmlisting/vdmlisting.pdf
%doc %{_texmfdistdir}/doc/latex/vdmlisting/vdmlisting.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
