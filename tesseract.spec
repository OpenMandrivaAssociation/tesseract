%define langdata() \
%package %{1}\
Group:		Graphics \
Summary:	%{3}%{?4: (%4)} language data for Tesseract \
#Version:	%{version_tessdata} \
BuildArch:	noarch \
Requires:	tesseract >= %{version_tesseract} \
Requires:	locales%{?2:-%2} \
Provides:	tesseract-language = %{version_tessdata} \
%description %{1} \
Tesseract data files required to recognize %{?4:%4 }%{3} text. \
\
%files %{1} \
%{_datadir}/tessdata/%{1}.* \
%{nil}

%define version_tesseract 5.0.0
%define version_tessdata  3.04.00

%define tesseract_major 5
%define libtesseract %mklibname %name %tesseract_major
%define devtesseract %mklibname %name -d

%bcond_without libdoc
%bcond_with    scrollview
%bcond_without training

Summary:	An high-performance OCR engine
Name:		tesseract
Version:	%{version_tesseract}
Release:	1
License:	ASL 2.0
Group:		Graphics
URL:		https://github.com/tesseract-ocr/%{name}
Source0:	https://github.com/tesseract-ocr/tesseract/archive/%{version_tesseract}/%{name}-%{version_tesseract}.tar.gz
Source1:	https://github.com/tesseract-ocr/langdata/archive/%{version_tessdata}/langdata-%{version_tessdata}.tar.gz
Patch100:	%{name}-3.04.01-scrollview.patch
Patch101:	%{name}-3.04.01-piccolo2d.patch

BuildRequires:	autoconf
BuildRequires:	asciidoc
BuildRequires:	xsltproc
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(lept) >= 1.71
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(libcurl)
%if %{with libdoc}
BuildRequires:	doxygen
%endif
%if %{with training}
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(icu-uc)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)
%endif
%if %{with scrollview}
BuildRequires:	java-headless
BuildRequires:	piccolo2d
%endif

Requires:	tesseract-language >= 3.00
%if %{with scrollview}
Requires:	java-headless
Requires:	piccolo2d
%endif

%description
The Tesseract OCR engine was one of the top 3 engines in the 1995 
UNLV Accuracy test. Since then it has had little work done on it, 
but it is probably one of the most accurate open source OCR engines 
available. The source code will read a binary, grey or color image 
and output text. 

%files
%doc AUTHORS README.md ChangeLog
%{_bindir}/*
%{_datadir}/tessdata
%exclude %{_datadir}/tessdata/*cube.*
%exclude %{_datadir}/tessdata/*.traineddata
%{_mandir}/man?/*
%if %{with scrollview}
%{_javadir}/ScrollView.jar
%endif

#-----------------------------------------------------------------

%package -n %{libtesseract}
Summary:	%name support library
Group:		System/Libraries

%description -n %{libtesseract}
%name library.

%files -n %{libtesseract}
%{_libdir}/libtesseract*.so.%{tesseract_major}*

#-----------------------------------------------------------------

%package devel
Summary:	Development files from %name
Group:		Development/C++
Requires:	%{libtesseract} = %{version}-%{release}
Provides:	%{devtesseract} = %{version}-%{release}
Obsoletes:	%{devtesseract} < 2.04

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
%{_libdir}/pkgconfig/*.pc
%if %{with libdoc}
%doc doc/html
%endif

#-----------------------------------------------------------------

%package osd
Group:		Graphics
Summary:	Orientation & script detection data pack for tesseract

%description osd
Data files required to recognize text orientation and scripts.

%files osd
%{_datadir}/tessdata/osd.*

#-----------------------------------------------------------------

# NOTE: names refer to doc/tesseract.1.asc
%langdata afr af Afrikaans
%langdata amh am Amharic
%langdata ara ar Arabic
%langdata asm as Assamese
%langdata aze az Azerbaijani
%langdata aze_cyrl az Azerbaijani Cyrilic
%langdata bel be Belarusian
%langdata ben bn Bengali
%langdata bod bo Tibetan
%langdata bos bs Bosnian
%langdata bul bg Bulgarian
%langdata cat ca "Catalan / Valencian"
#NOTE: Cebuano has not ISO 639-1 two-letter code
#      (https://en.wikipedia.org/wiki/Cebuano_language)
#      This is not provided by glibc.
%langdata ceb "" Cebuano
%langdata ces cs Czech
%langdata chi_sim zh Chinese simplified
%langdata chi_tra zh Chinese traditional
%langdata chr en Cherokee
%langdata cym cy Welsh
%langdata dan da Danish
%langdata dan_frak da Danish Fraktur
%langdata deu de German
%langdata deu_frak de German Fraktur
%langdata dzo dz Dzongkha
%langdata ell el "Modern Greek (1453-today)"
%langdata eng en English
%langdata enm en "Middle English (1100-1500)"
%langdata epo eo Esperanto
#% langdata epo_alt eo Esperanto alternative
%langdata equ en Math "equation detection module"
%langdata est et Estonian
%langdata eus eu Basque
%langdata fas fa Persian Farsi
%langdata fin fi Finnish
%langdata fra fr French
%langdata frk fr Frankish
%langdata frm fr "Middle French (ca.1400-1600)"
%langdata gle ga Irish
%langdata glg gl Galician
%langdata grc el "Ancient Greek (to 1453)"
%langdata guj gu Gujarati
%langdata hat ht Haitian Creole
%langdata heb he Hebrew
%langdata hin hi Hindi
%langdata hrv hr Croatian
%langdata hun hu Hungarian
%langdata iku iu Inuktitut
%langdata ind id Indonesian
%langdata isl is Icelandic
%langdata ita it Italian
%langdata ita_old it Italian Old
#NOTE: Javanese has several ISO 639-1 two-letter codes:
#               jav jvn, jas, osi, tes, kaw
#      (https://en.wikipedia.org/wiki/Cebuano_language)
#      None of them are provided by glibc.
%langdata jav "" Javanese
%langdata jpn ja Japanese
%langdata kan kn Kannada
%langdata kat ka Georgian
%langdata kat_old ka Georgian Old
%langdata kaz kk Kazakh
%langdata khm km "Central Khmer"
%langdata kir ky "Kirghiz or Kyrgyz"
%langdata kor ko Korean
%langdata kur ku Kurdish
%langdata lao lo Lao
#NOTE: Cebuano has "lat" as ISO 639-1 two-letter code
#      (https://en.wikipedia.org/wiki/Cebuano_language)
#      This is not provided by glibc.
%langdata lat "" Latin
%langdata lav lv Latvian
%langdata lit lt Lithuanian
%langdata mal ml Malayalam
%langdata mar mr Marathi
%langdata mkd mk Macedonian
%langdata mlt mt Maltese
%langdata msa ms Malay
%langdata mya my Burmese
%langdata nep ne Nepali
%langdata nld nl Dutch Flemish
%langdata nor no Norwegian
%langdata ori or Oriya
%langdata pan pa "Panjabi or Punjabi"
%langdata pol pl Polish
%langdata por pt Portuguese
%langdata pus ps "Pushto or Pashto"
%langdata ron ro "Romanian or Moldavian or Moldovan"
%langdata rus ru Russian
%langdata san sa Sanskrit
%langdata sin si "Sinhala or Sinhalese"
%langdata slk sk Slovakian
%langdata slk_frak sk Slovakian Fraktur
%langdata slv sl Slovenian
%langdata spa es Spanish Castilian
%langdata spa_old es Spanish "Old Castilian"
%langdata sqi sq Albanian
%langdata srp sr Serbian
%langdata srp_latn sr Serbian Latin
%langdata swe sv Swedish
%langdata swa sw Swahili
#% langdata swe_frak sv Swedish Fraktur
%langdata syr ar Syriac
%langdata tam ta Tamil
%langdata tel te Telugu
%langdata tgk tg Tajik
%langdata tgl en Tagalog
%langdata tha th Thai
%langdata tir am Tigrinya
%langdata tur tr Turkish
%langdata uig ug "Uighur or Uyghur"
%langdata ukr uk Ukrainian
%langdata urd ur Urdu
%langdata uzb uz Uzbek
%langdata uzb_cyrl uz Uzbek Cyrillic
%langdata vie vi Vietnamese
%langdata yid yi Yiddish

%prep
%setup -q -n %{name}-%{version} -a1
%if %{with scrollview}
%patch100 -p1 -b .orig
%patch101 -p1 -b .orig
%endif

# Move tessdata in the right path
mv ./tessdata-%{version_tessdata}/* ./tessdata/
rm -rf ./tessdata-%{version_tessdata}/

# debugger
%if %{with scrollview}
sed -i 's|@scrollviewpath@|\$(DESTDIR)%{_javadir}|' java/Makefile.am
%endif

%build
./autogen.sh
%configure
%make

# training binary
%if %{with training}
%make training
%endif

# debugger
%if %{with scrollview}
%make ScrollView.jar
%endif

# library documentation
%if %{with libdoc}
%make doc
%endif

%install
%makeinstall_std

# training binary
%if %{with training}
%makeinstall_std training-install
%endif

# debugger
%if %{with scrollview}
%makeinstall_std install-jars
%endif

# library documentation
%if %{with libdoc}
%makeinstall_std doc
%endif

# language data
for file in tessdata/*cube.* tessdata/*.traineddata
do
	install -m 0644 -D "$file" %{buildroot}%{_datadir}/tessdata
done
