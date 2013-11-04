%define langdata() \
%package %{1}\
Group:		Graphics \
Summary:        %{3}%{?4: (%4)} language data for Tesseract \
Requires:       tesseract >= 3.00 \
Requires:       locales-%{2} \
Provides:       tesseract-language \
%description %{1} \
Tesseract data files required to recognize %{?4:%4 }%{3} text. \
%files %{1} \
%{_datadir}/tessdata/%{1}.* \
%{nil}

%define major %(echo %version |cut -d. -f1-2)

Name:		tesseract
Version:	3.02.03
Release:	0.svn866.3
Summary:	A high-performance OCR engine
URL:		http://code.google.com/p/tesseract-ocr/
License:	ASL 2.0
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
Patch2:		tesseract-3.02.02-strfmt.patch
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
Requires:	locales-he
Provides:       tesseract-language
%description heb-com
Tesseract data files required to recognize Hebrew community text.
%files heb-com
%{_datadir}/tessdata/heb-*
%doc tessdata/heb-.README

#-----------------------------------------------------------------

%langdata afr af Afrikaans
%langdata ara ar Arabic
%langdata aze az Azerbaijani
%langdata bel be Belarusian
%langdata ben bn Bengali
%langdata bul br Bulgarian
%langdata cat ca Catalan
%langdata ces cs Czech
%langdata chi_sim zh Chinese simplified
%langdata chi_tra zh Chinese traditional
%langdata chr en Cherokee
%langdata dan-frak da Danish fraktur
%langdata dan da Danish
%langdata deu-frak de German fraktur
%langdata deu de German
%langdata ell el Greek
%langdata eng en English
%langdata enm en Middle English (1100-1500)
%langdata epo eo Esperanto
%langdata epo_alt eo Esperanto (alternative)
%langdata equ en Math/Equation
%langdata est et Estonian
%langdata eus eu Basque
%langdata fin fi Finnish
%langdata fra fr French
%langdata frk fr Frankish
%langdata frm fr Middle French (1400-1600)
%langdata glg gl Galician
%langdata grc el Ancient Greek
%langdata heb he Hebrew
%langdata hin hi Hindi
%langdata hrv hr Croatian
%langdata hun hu Hungarian
%langdata ind id Indonesian
%langdata isl is Icelandic
%langdata ita it Italian
%langdata ita_old it Old Italian
%langdata jpn ja Japanese
%langdata kan kn Kannada
%langdata kor ko Korean
%langdata lav lv Latvian
%langdata lit lt Lithuanian
%langdata mal ml Malayalam
%langdata mkd mk Macedonian
%langdata mlt mt Maltese
%langdata msa ms Malay
%langdata nld nl Dutch
%langdata nor no Norwegian
%langdata pol pl Polish
%langdata por pt Portuguese
%langdata ron ro Romanian
%langdata rus ru Russian
%langdata slk sk Slovakian
%langdata slk-frak sk Slovakian fraktur
%langdata slv sl Slovenian
%langdata spa es Spanish
%langdata spa_old es Old Spanish
%langdata sqi sq Albanian
%langdata srp st Serbian latin
%langdata swa sw Swahili
%langdata swe-frak sv Swedish fraktur
%langdata swe sv Swedish
%langdata tam ta Tamil
%langdata tel te Telugu
%langdata tgl en Tagalog
%langdata tha th Thai
%langdata tur tr Turkish
%langdata ukr uk Ukrainian
%langdata vie vi Vietnamese

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

