Name: tesseract
Version: 2.04
Release: %mkrel 3
Summary: A high-performance OCR engine
URL: http://code.google.com/p/tesseract-ocr/
License: Apache
Group: Graphics
Source: %{name}-%{version}.tar.gz
Source1: tesseract-2.00.eng.tar.gz
Source2: tesseract-2.00.fra.tar.gz
Source3: tesseract-2.00.ita.tar.gz
Source4: tesseract-2.00.deu.tar.gz
Source5: tesseract-2.00.spa.tar.gz
Source6: tesseract-2.00.nld.tar.gz
Source7: tesseract-2.01.por.tar.gz
Source8: tesseract-2.01.deu-f.tar.gz
Source9: tesseract-2.01.vie.tar.gz
Patch0:	tesseract-locale-fix.diff
Patch1: tesseract-cmake.patch 
Patch2: tesseract-2.04-gcc4.3.patch
BuildRequires: tiff-devel
BuildRequires: jpeg-devel
BuildRequires: cmake
Requires: tesseract-language
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%description
The Tesseract OCR engine was one of the top 3 engines in the 1995 
UNLV Accuracy test. Since then it has had little work done on it, 
but it is probably one of the most accurate open source OCR engines 
available. The source code will read a binary, grey or color image 
and output text. A tiff reader is built in that will read 
uncompressed TIFF images, or libtiff can be added to read compressed 
images.

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README ReleaseNotes ChangeLog
%{_bindir}/*
%{_datadir}/tessdata
%exclude %_datadir/tessdata/*.DangAmbigs
%exclude %_datadir/tessdata/*.freq-dawg
%exclude %_datadir/tessdata/*.inttemp
%exclude %_datadir/tessdata/*.normproto
%exclude %_datadir/tessdata/*.pffmtable
%exclude %_datadir/tessdata/*.unicharset
%exclude %_datadir/tessdata/*.user-words
%exclude %_datadir/tessdata/*.word-dawg

#-----------------------------------------------------------------

%define tesseract_full_major 2
%define libtesseract_full %mklibname tesseract_full %{tesseract_full_major}

%package -n %{libtesseract_full}
Summary: Nepomuk support library
Group: System/Libraries

%description -n %{libtesseract_full}
Nepomuk support library.

%files -n %{libtesseract_full}
%defattr(-,root,root,-)
%_libdir/libtesseract_full.so.%{tesseract_full_major}*

#-----------------------------------------------------------------

%package devel
Summary: Development files from %name
Group:  Development/C++
Provides: %{mklibname %name -d} = %version-%release
Obsoletes: %{mklibname %name -d} < 2.04


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

%package eng
Group:   Graphics
Summary: English language pack for tesseract
Provides: tesseract-language

%description eng
Data files required to recognize English OCR.

%files eng
%{_datadir}/tessdata/eng.*

#-----------------------------------------------------------------

%package fra
Group:   Graphics
Summary: French language pack for tesseract
Provides: tesseract-language

%description fra
Data files required to recognize French OCR.

%files fra
%{_datadir}/tessdata/fra.*

#-----------------------------------------------------------------

%package ita
Group:   Graphics
Summary: Italian language pack for tesseract
Provides: tesseract-language

%description ita
Data files required to recognize Italian OCR.

%files ita
%{_datadir}/tessdata/ita.*

#-----------------------------------------------------------------

%package deu
Group:   Graphics
Summary: German language pack for tesseract
Provides: tesseract-language

%description deu
Data files required to recognize German OCR.

%files deu
%{_datadir}/tessdata/deu.*

#-----------------------------------------------------------------

%package spa
Group:   Graphics
Summary: Spanish language pack for tesseract
Provides: tesseract-language

%description spa
Data files required to recognize Spanish OCR.

%files spa
%{_datadir}/tessdata/spa.*

#-----------------------------------------------------------------

%package nld
Group:   Graphics
Summary: Dutch language pack for tesseract
Provides: tesseract-language

%description nld
Data files required to recognize Dutch OCR.

%files nld
%{_datadir}/tessdata/nld.*

#-----------------------------------------------------------------

%package por
Group:   Graphics
Summary: Portugese (Brazillian) language pack for tesseract
Provides: tesseract-language

%description por
Data files required to recognize Portugese (Brazillian) OCR.

%files por
%{_datadir}/tessdata/por.*

#-----------------------------------------------------------------

%package deu-f
Group:   Graphics
Summary: Fraktu (Old German) language pack for tesseract
Provides: tesseract-language

%description deu-f
Data files required to recognize Fraktu (Old German) OCR.

%files deu-f
%{_datadir}/tessdata/deu-f.*

#-----------------------------------------------------------------

%package vie
Group:   Graphics
Summary: Vietnamese Language data for Tesseract
Provides: tesseract-language

%description vie
Data files required to recognize Vietnamese OCR.

%files vie
%{_datadir}/tessdata/vie.*

#-----------------------------------------------------------------

%prep
%setup -q -a1 -a2 -a3 -a4 -a5 -a6
%patch0 -p1 
%patch1 -p1 -b .orig 
%patch2 -p0 -b .orig

%build
%cmake
%make 

%install
rm -fr %buildroot
%makeinstall_std -C build

pushd %buildroot/%_datadir
tar xfz %SOURCE7
tar xfz %SOURCE8
tar xfz %SOURCE9
popd

%clean
rm -rf %buildroot 


