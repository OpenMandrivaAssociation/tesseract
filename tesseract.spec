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

%define major %(echo %version |cut -d. -f1-2)

Name:		tesseract
Version:	3.02.02
Release:	1
Summary:	A high-performance OCR engine
URL:		http://code.google.com/p/tesseract-ocr/
License:	Apache
Group:		Graphics
Source0:	http://tesseract-ocr.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.eng.tar.gz
Source2:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.ukr.tar.gz
Source3:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.tur.tar.gz
Source4:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.tha.tar.gz
Source5:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.tgl.tar.gz
Source6:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.tel.tar.gz
Source7:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.tam.tar.gz
Source8:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.swe.tar.gz
Source9:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.swa.tar.gz
Source10:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.srp.tar.gz
Source11:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.sqi.tar.gz
Source12:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.spa_old.tar.gz
Source13:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.spa.tar.gz
Source14:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.slv.tar.gz
Source15:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.slk.tar.gz
Source16:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.ron.tar.gz
Source17:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.por.tar.gz
Source18:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.pol.tar.gz
Source19:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.nor.tar.gz
Source20:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.nld.tar.gz
Source21:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.msa.tar.gz
Source22:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.mlt.tar.gz
Source23:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.mkd.tar.gz
Source24:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.mal.tar.gz
Source25:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.lit.tar.gz
Source26:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.lav.tar.gz
Source27:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.kor.tar.gz
Source28:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.kan.tar.gz
Source29:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.ita_old.tar.gz
Source30:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.ita.tar.gz
Source31:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.isl.tar.gz
Source32:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.ind.tar.gz
Source33:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.chr.tar.gz
Source34:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.hun.tar.gz
Source35:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.hrv.tar.gz
Source36:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.hin.tar.gz
Source37:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.heb.tar.gz
Source38:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.glg.tar.gz
Source39:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.frm.tar.gz
Source40:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.frk.tar.gz
Source41:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.fra.tar.gz
Source42:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.fin.tar.gz
Source43:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.eus.tar.gz
Source44:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.est.tar.gz
Source45:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.equ.tar.gz
Source46:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.epo.tar.gz
Source47:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.epo_alt.tar.gz
Source48:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.enm.tar.gz
Source49:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.ell.tar.gz
Source50:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.deu.tar.gz
Source51:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.dan.tar.gz
Source52:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.ces.tar.gz
Source53:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.cat.tar.gz
Source54:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.bul.tar.gz
Source55:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.ben.tar.gz
Source56:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.bel.tar.gz
Source57:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.aze.tar.gz
Source58:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.ara.tar.gz
Source59:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.afr.tar.gz
Source60:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.jpn.tar.gz
Source61:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.chi_sim.tar.gz
Source62:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.chi_tra.tar.gz
Source63:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.grc.tar.gz
Source64:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.rus.tar.gz
Source65:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-%major.vie.tar.gz
# Not released with 3.02
Source66:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-3.01.osd.tar.gz
Source67:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-3.01.heb-com.tar.gz
Source68:	http://tesseract-ocr.googlecode.com/files/tesseract-ocr-3.01.slk-frak.tar.gz

Source100:	http://tesseract-ocr.googlecode.com/files/swe-frak.traineddata.gz

Patch1:		tesseract-format-security.patch
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
%_libdir/pkgconfig/*.pc

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

%langdata afr Afrikaans
%langdata ara Arabic
%langdata aze Azerbaijani
%langdata bel Belarusian
%langdata ben Bengali
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
%langdata enm Middle English (1100-1500)
%langdata epo Esperanto
%langdata epo_alt Esperanto (alternative)
%langdata equ Math/Equation
%langdata est Estonian
%langdata eus Basque
%langdata fin Finnish
%langdata fra French
%langdata frk Frankish
%langdata frm Middle French (1400-1600)
%langdata glg Galician
%langdata grc Ancient Greek
%langdata heb Hebrew
%langdata hin Hindi
%langdata hrv Croatian
%langdata hun Hungarian
%langdata ind Indonesian
%langdata isl Icelandic
%langdata ita Italian
%langdata ita_old Old Italian
%langdata jpn Japanese
%langdata kan Kannada
%langdata kor Korean
%langdata lav Latvian
%langdata lit Lithuanian
%langdata mal Malayalam
%langdata mkd Macedonian
%langdata mlt Maltese
%langdata msa Malay
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
%langdata spa_old Old Spanish
%langdata sqi Albanian
%langdata srp Serbian latin
%langdata swa Swahili
%langdata swe-frak Swedish fraktur
%langdata swe Swedish
%langdata tam Tamil
%langdata tel Telugu
%langdata tgl Tagalog
%langdata tha Thai
%langdata tur Turkish
%langdata ukr Ukrainian
%langdata vie Vietnamese

%prep
%setup -q -b1 -b2 -b3 -b4 -b5 -b6 -b7 -b8 -b9 -b10 -b11 -b12 -b13 -b14 -b15 -b16 -b17 -b18 -b19 -b20 -b21 -b22 -b23 -b24 -b25 -b26 -b27 -b28 -b29 -b30 -b31 -b32 -b33 -b34 -b35 -b36 -b37 -b38 -b39 -b40 -b41 -b42 -b43 -b44 -b45 -b46 -b47 -b48 -b49 -b50 -b51 -b52 -b53 -b54 -b55 -b56 -b57 -b58 -b59 -b60 -b61 -b62 -b63 -b64 -b65 -b66 -b67 -b68
mv ../tesseract-ocr/tessdata/* ./tessdata/
rm -rf ../tesseract-ocr
%apply_patches

for archive in %SOURCE100; do
	filename=`echo $archive | sed -e 's|^.*/||;s|.gz$||'`
	if [ -e ./tessdata/$filename ]; then
		echo "FIXME: Check for duplicate: $filename"
		read
	else
		gzip -cd $archive > ./tessdata/$filename
	fi
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

