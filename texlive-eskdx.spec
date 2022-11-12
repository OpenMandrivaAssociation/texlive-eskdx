Name:		texlive-eskdx
Version:	29235
Release:	1
Summary:	Modern Russian typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eskdx
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eskdx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eskdx.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Eskdx is a collection of LaTeX classes and packages to typeset
textual and graphical documents in accordance with Russian (and
probably post USSR) standards for designers.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/eskdx/eskdafterpkg.sty
%{_texmfdistdir}/tex/latex/eskdx/eskdappsheet.sty
%{_texmfdistdir}/tex/latex/eskdx/eskdbiblist.sty
%{_texmfdistdir}/tex/latex/eskdx/eskdcap.sty
%{_texmfdistdir}/tex/latex/eskdx/eskdchngsheet.sty
%{_texmfdistdir}/tex/latex/eskdx/eskddstu.sty
%{_texmfdistdir}/tex/latex/eskdx/eskdexplan.sty
%{_texmfdistdir}/tex/latex/eskdx/eskdfont.sty
%{_texmfdistdir}/tex/latex/eskdx/eskdfootnote.sty
%{_texmfdistdir}/tex/latex/eskdx/eskdfreesize.sty
%{_texmfdistdir}/tex/latex/eskdx/eskdgraph.cls
%{_texmfdistdir}/tex/latex/eskdx/eskdhash.sty
%{_texmfdistdir}/tex/latex/eskdx/eskdindent.sty
%{_texmfdistdir}/tex/latex/eskdx/eskdinfo.sty
%{_texmfdistdir}/tex/latex/eskdx/eskdlang.sty
%{_texmfdistdir}/tex/latex/eskdx/eskdlist.sty
%{_texmfdistdir}/tex/latex/eskdx/eskdpara.sty
%{_texmfdistdir}/tex/latex/eskdx/eskdplain.sty
%{_texmfdistdir}/tex/latex/eskdx/eskdrussian.def
%{_texmfdistdir}/tex/latex/eskdx/eskdsect.sty
%{_texmfdistdir}/tex/latex/eskdx/eskdspec.sty
%{_texmfdistdir}/tex/latex/eskdx/eskdspecii.sty
%{_texmfdistdir}/tex/latex/eskdx/eskdstamp.sty
%{_texmfdistdir}/tex/latex/eskdx/eskdtab.cls
%{_texmfdistdir}/tex/latex/eskdx/eskdtext.cls
%{_texmfdistdir}/tex/latex/eskdx/eskdtitle.sty
%{_texmfdistdir}/tex/latex/eskdx/eskdtitlebase.sty
%{_texmfdistdir}/tex/latex/eskdx/eskdtotal.sty
%{_texmfdistdir}/tex/latex/eskdx/eskdukrainian.def
%doc %{_texmfdistdir}/doc/latex/eskdx/ChangeLog
%doc %{_texmfdistdir}/doc/latex/eskdx/Makefile
%doc %{_texmfdistdir}/doc/latex/eskdx/Makefile.unpacked
%doc %{_texmfdistdir}/doc/latex/eskdx/NEWS
%doc %{_texmfdistdir}/doc/latex/eskdx/NEWS.in
%doc %{_texmfdistdir}/doc/latex/eskdx/README
%doc %{_texmfdistdir}/doc/latex/eskdx/README.in
%doc %{_texmfdistdir}/doc/latex/eskdx/include.m4
%doc %{_texmfdistdir}/doc/latex/eskdx/include.mak
%doc %{_texmfdistdir}/doc/latex/eskdx/manifest.txt
%doc %{_texmfdistdir}/doc/latex/eskdx/manual/Makefile
%doc %{_texmfdistdir}/doc/latex/eskdx/manual/eskdx.pdf
%doc %{_texmfdistdir}/doc/latex/eskdx/manual/eskdx.tex.in
%doc %{_texmfdistdir}/doc/latex/eskdx/manual/example.tex
%doc %{_texmfdistdir}/doc/latex/eskdx/manual/img-form1.svg
%doc %{_texmfdistdir}/doc/latex/eskdx/manual/img-form2.svg
%doc %{_texmfdistdir}/doc/latex/eskdx/manual/img-form2a.svg
%doc %{_texmfdistdir}/doc/latex/eskdx/manual/img-title.svg
%doc %{_texmfdistdir}/doc/latex/eskdx/manual/latex2html-init
%doc %{_texmfdistdir}/doc/latex/eskdx/source/Makefile
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdafterpkg.sty.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdappsheet.sty.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdbiblist.sty.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdcap.sty.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdchngsheet.sty.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskddstu.sty.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdexplan.sty.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdfont.sty.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdfootnote.sty.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdfreesize.sty.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdgraph.cls.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdhash.sty.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdindent.sty.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdinfo.sty.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdlang.sty.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdlist.sty.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdpara.sty.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdplain.sty.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdrussian.def.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdsect.sty.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdspec.sty.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdspecii.sty.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdstamp.sty.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdtab.cls.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdtext.cls.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdtitle.sty.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdtitlebase.sty.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdtotal.sty.in
%doc %{_texmfdistdir}/doc/latex/eskdx/source/eskdukrainian.def.in
%doc %{_texmfdistdir}/doc/latex/eskdx/test/Makefile
%doc %{_texmfdistdir}/doc/latex/eskdx/test/appsheet.tex
%doc %{_texmfdistdir}/doc/latex/eskdx/test/drawing-a2.tex
%doc %{_texmfdistdir}/doc/latex/eskdx/test/drawing-a3-mp.tex
%doc %{_texmfdistdir}/doc/latex/eskdx/test/drawing-a3-p.tex
%doc %{_texmfdistdir}/doc/latex/eskdx/test/drawing-a3.tex
%doc %{_texmfdistdir}/doc/latex/eskdx/test/drawing-a4.tex
%doc %{_texmfdistdir}/doc/latex/eskdx/test/footnote.tex
%doc %{_texmfdistdir}/doc/latex/eskdx/test/freesizesheets.tex
%doc %{_texmfdistdir}/doc/latex/eskdx/test/general.tex
%doc %{_texmfdistdir}/doc/latex/eskdx/test/general2.tex
%doc %{_texmfdistdir}/doc/latex/eskdx/test/numbering.tex
%doc %{_texmfdistdir}/doc/latex/eskdx/test/pagestyle.tex
%doc %{_texmfdistdir}/doc/latex/eskdx/test/spec.tex
%doc %{_texmfdistdir}/doc/latex/eskdx/test/specii.tex
%doc %{_texmfdistdir}/doc/latex/eskdx/test/twoside.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
