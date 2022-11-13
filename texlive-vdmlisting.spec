Name:		texlive-vdmlisting
Version:	56905
Release:	1
Summary:	Typesetting VDM in ASCII syntax
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/vdmlisting
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vdmlisting.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vdmlisting.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
