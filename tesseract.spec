%define langdata() \
%package %{1}\
Group:		Graphics \
Summary:        %{2}%{?3: (%3)} language data for Tesseract \
Requires:       tesseract >= 3.00 \
Provides:       tesseract-language \
%description %{1} \
Tesseract data files required to recognize %{?3:%3 }%{2} text. \
%files %{1} \
%{_datadir}/tessdata/%{1}.* \
%{nil}


Name:		tesseract
Version:	3.01
Release:	2
Summary:	A high-performance OCR engine
URL:		http://code.google.com/p/tesseract-ocr/
License:	Apache
Group:		Graphics
Source0:	%{name}-%{version}.tar.gz
Source1:	tesseract-ocr-3.01.ara.tar.gz
Source2:	tesseract-ocr-3.01.eng.tar.gz
Source3:	tesseract-ocr-3.01.heb-com.tar.gz
Source4:	tesseract-ocr-3.01.heb.tar.gz
Source5:	tesseract-ocr-3.01.hin.tar.gz
Source6:	tesseract-ocr-3.01.osd.tar.gz
Source7:	tesseract-ocr-3.01.slk-frak.tar.gz
Source8:	tesseract-ocr-3.01.tha.tar.gz

Source9:	bul.traineddata.gz
Source10:	cat.traineddata.gz
Source11:	ces.traineddata.gz
Source12:	chi_sim.traineddata.gz
Source13:	chi_tra.traineddata.gz
Source14:	chr.traineddata.gz
Source15:	dan-frak.traineddata.gz
Source16:	dan.traineddata.gz
Source17:	deu-frak.traineddata.gz
Source18:	deu.traineddata.gz
Source19:	ell.traineddata.gz
#Source20:	eng.traineddata.gz
Source21:	fin.traineddata.gz
Source22:	fra.traineddata.gz
Source23:	hun.traineddata.gz
Source24:	ind.traineddata.gz
Source25:	ita.traineddata.gz
Source26:	jpn.traineddata.gz
Source27:	kor.traineddata.gz
Source28:	lav.traineddata.gz
Source29:	lit.traineddata.gz
Source30:	nld.traineddata.gz
Source31:	nor.traineddata.gz
Source32:	pol.traineddata.gz
Source33:	por.traineddata.gz
Source34:	ron.traineddata.gz
Source35:	rus.traineddata.gz
Source36:	slk.traineddata.gz
Source37:	slv.traineddata.gz
Source38:	spa.traineddata.gz
Source39:	srp.traineddata.gz
Source40:	swe-frak.traineddata.gz
Source41:	swe.traineddata.gz
Source42:	tgl.traineddata.gz
Source43:	tur.traineddata.gz
Source44:	ukr.traineddata.gz
Source45:	vie.traineddata.gz

Patch1:		tesseract-3.01-mdv-format-security.patch
Patch2:		tesseract-3.01-upstream-buildfix.patch
Patch3:		tesseract-automake-1.13.patch
BuildRequires:	tiff-devel
BuildRequires:	jpeg-devel
BuildRequires:	leptonica-devel
Requires:	tesseract-language >= 3.00

%description
The Tesseract OCR engine was one of the top 3 engines in the 1995 
UNLV Accuracy test. Since then it has had little work done on it, 
but it is probably one of the most accurate open source OCR engines 
available. The source code will read a binary, grey or color image 
and output text. 

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README ReleaseNotes ChangeLog
%{_bindir}/*
%{_datadir}/tessdata
%exclude %_datadir/tessdata/*cube.*
%exclude %_datadir/tessdata/*.traineddata
%{_mandir}/man?/*

#-----------------------------------------------------------------

%define tesseract_major 3
%define libtesseract %mklibname tesseract %{tesseract_major}

%package -n %{libtesseract}
Summary:	%name support library
Group:		System/Libraries

%description -n %{libtesseract}
%name library.

%files -n %{libtesseract}
%defattr(-,root,root,-)
%_libdir/libtesseract*.so.%{tesseract_major}*

#-----------------------------------------------------------------

%package devel
Summary:	Development files from %name
Group:		Development/C++
Requires:	%{libtesseract} = %version-%release
Provides:	%{mklibname %name -d} = %version-%release
Obsoletes:	%{mklibname %name -d} < 2.04


%description devel
The Tesseract OCR engine was one of the top 3 engines in the 1995
UNLV Accuracy test. Since then it has had little work done on it,
but it is probably one of the most accurate open source OCR engines
available. The source code will read a binary, grey or color image
and output text. A tiff reader is built in that will read
uncompressed TIFF images, or libtiff can be added to read compressed
images.

%files devel
%defattr(-,root,root)
%{_includedir}/tesseract
%{_libdir}/*.so

#-----------------------------------------------------------------

%package osd
Group:          Graphics
Summary:        Orientation & script detection data pack for tesseract

%description osd
Data files required to recognize text orintation and scripts.

%files osd
%{_datadir}/tessdata/osd.*

#-----------------------------------------------------------------

%package heb-com
Group:          Graphics
Summary:        Hebrew (community) language data for Tesseract
Requires:       tesseract >= 3.00
Provides:       tesseract-language
%description heb-com
Tesseract data files required to recognize Hebrew community text.
%files heb-com
%{_datadir}/tessdata/heb-*
%doc tessdata/heb-.README

#-----------------------------------------------------------------

%langdata ara Arabic
%langdata bul Bulgarian
%langdata cat Catalan
%langdata ces Czech
%langdata chi_sim Chinese simplified
%langdata chi_tra Chinese traditional
%langdata chr Cherokee
%langdata dan-frak Danish fraktur
%langdata dan Danish
%langdata deu-frak German fraktur
%langdata deu German
%langdata ell Greek
%langdata eng English
%langdata fin Finnish
%langdata fra French
%langdata heb Hebrew
%langdata hin Hindi
%langdata hun Hungarian
%langdata ind Indonesian
%langdata ita Italian
%langdata jpn Japanese
%langdata kor Korean
%langdata lav Latvian
%langdata lit Lithuanian
%langdata nld Dutch
%langdata nor Norwegian
%langdata pol Polish
%langdata por Portuguese
%langdata ron Romanian
%langdata rus Russian
%langdata slk Slovakian
%langdata slk-frak Slovakian fraktur
%langdata slv Slovenian
%langdata spa Spanish
%langdata srp Serbian latin
%langdata swe-frak Swedish fraktur
%langdata swe Swedish
%langdata tgl Tagalog
%langdata tha Thai
%langdata tur Turkish
%langdata ukr Ukrainian
%langdata vie Vietnamese

%prep
%setup -q -b1 -b2 -b3 -b4 -b5 -b6 -b7 -b8
mv ../tesseract-ocr/tessdata/* ./tessdata/
rm -rf ../tesseract-ocr
%apply_patches

for archive in %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} %{SOURCE15} %{SOURCE16} %{SOURCE17} %{SOURCE18} %{SOURCE19} %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24} %{SOURCE25} %{SOURCE26} %{SOURCE27} %{SOURCE28} %{SOURCE29} %{SOURCE30} %{SOURCE31} %{SOURCE32} %{SOURCE33} %{SOURCE34} %{SOURCE35} %{SOURCE36} %{SOURCE37} %{SOURCE38} %{SOURCE39} %{SOURCE40} %{SOURCE41} %{SOURCE42} %{SOURCE43} %{SOURCE44} %{SOURCE45}
do
filename=`echo $archive | sed -e 's|^.*/||;s|.gz$||'`
gzip -cd $archive > ./tessdata/$filename
done

%build
mkdir m4
./autogen.sh
%configure2_5x --disable-static
%make 

%install
rm -fr %buildroot
%makeinstall_std

for file in tessdata/*cube.* tessdata/*.traineddata
do
install -m 644 -D $file %{buildroot}%{_datadir}/tessdata
done


%changelog
* Sun Nov 06 2011 Andrey Smirnov <asmirnov@mandriva.org> 3.01-1mdv2012.0
+ Revision: 722812
- Update to 3.01
  Linked to Leptonica library
  Couple tons of new language data

* Tue Mar 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.00-1
+ Revision: 647503
- Fix requires in the devel package
- make it build
  Fix file list
  Do not package .la/.a files

  + Zombie Ryushu <ryushu@mandriva.org>
    - use configure
    - Remove deprecated patches
    - Upgrade to 3.00

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.04-6mdv2011.0
+ Revision: 607988
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.04-5mdv2010.1
+ Revision: 524227
- rebuilt for 2010.1

* Wed Sep 16 2009 Helio Chissini de Castro <helio@mandriva.com> 2.04-4mdv2010.0
+ Revision: 443609
- Devel should requires main library

* Wed Sep 16 2009 Helio Chissini de Castro <helio@mandriva.com> 2.04-3mdv2010.0
+ Revision: 443571
- Move tesseract_full to be a shared library. This will solve all issues having with static linking and make olena and nepomuk-scribo happy.
  Hope upstream accept this patch

* Wed Sep 16 2009 Helio Chissini de Castro <helio@mandriva.com> 2.04-1mdv2010.0
+ Revision: 443344
- Create new buildsystem for tesseract based on cmake
- Fix gcc 4.3 build
- Splitted in proper way languages

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jun 19 2008 Funda Wang <fwang@mandriva.org> 2.03-1mdv2009.0
+ Revision: 226134
- remove java makefile
- New version 2.03
- add patch to build against gcc4.3

* Tue Jan 29 2008 Austin Acton <austin@mandriva.org> 2.01-1mdv2008.1
+ Revision: 159875
- new version
- add two new language files

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot

* Sat Aug 25 2007 Austin Acton <austin@mandriva.org> 2.00-1mdv2008.0
+ Revision: 71373
- 2.00
- clean up this disgusting spec file
- fix groups, licenses
- bundle language files
- auto optflags
- simplify file lists
- simplify summaries and descriptions

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Add URL  thanks Austin

* Fri May 18 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.04-1mdv2008.0
+ Revision: 27786
- Fix Licence
- Import tesseract

