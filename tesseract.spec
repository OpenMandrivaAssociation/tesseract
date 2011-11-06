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
Release:	%mkrel 1
Summary:	A high-performance OCR engine
URL:		http://code.google.com/p/tesseract-ocr/
License:	Apache
Group:		Graphics
Source:		%{name}-%{version}.tar.gz
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
%patch1 -p1

for archive in %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} %{SOURCE15} %{SOURCE16} %{SOURCE17} %{SOURCE18} %{SOURCE19} %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24} %{SOURCE25} %{SOURCE26} %{SOURCE27} %{SOURCE28} %{SOURCE29} %{SOURCE30} %{SOURCE31} %{SOURCE32} %{SOURCE33} %{SOURCE34} %{SOURCE35} %{SOURCE36} %{SOURCE37} %{SOURCE38} %{SOURCE39} %{SOURCE40} %{SOURCE41} %{SOURCE42} %{SOURCE43} %{SOURCE44} %{SOURCE45}
do
filename=`echo $archive | sed -e 's|^.*/||;s|.gz$||'`
gzip -cd $archive > ./tessdata/$filename
done

%build
%__automake
%configure2_5x
%make 

%install
rm -fr %buildroot
%makeinstall_std

for file in tessdata/*cube.* tessdata/*.traineddata
do
install -m 644 -D $file %{buildroot}%{_datadir}/tessdata
done

rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf %buildroot 


