%define	name	tesseract
%define version	2.00
%define	release	%mkrel 1

%define major 	0
%define libname %mklibname %name %{major}
%define libnamedev %mklibname %name -d

Name:		%name
Version:	%version
Release:	%release
Summary: 	A high-performance OCR engine
URL:		http://code.google.com/p/tesseract-ocr/

License:  	Apache
Group:    	Graphics
Source:   	%{name}-%{version}.tar.gz
Source1:        tesseract-%{version}.eng.tar.gz
Source2:        tesseract-%{version}.fra.tar.gz
Source3:        tesseract-%{version}.ita.tar.gz
Source4:        tesseract-%{version}.deu.tar.gz
Source5:        tesseract-%{version}.spa.tar.gz
Source6:        tesseract-%{version}.nld.tar.gz

BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%description
The Tesseract OCR engine was one of the top 3 engines in the 1995 
UNLV Accuracy test. Since then it has had little work done on it, 
but it is probably one of the most accurate open source OCR engines 
available. The source code will read a binary, grey or color image 
and output text. A tiff reader is built in that will read 
uncompressed TIFF images, or libtiff can be added to read compressed 
images.

%package -n %{libnamedev}
Summary:  Development files from %name.
Group:	  Development/C++
Provides: %name-devel
Requires: %{name} = %{version}

%description -n %{libnamedev}
The Tesseract OCR engine was one of the top 3 engines in the 1995
UNLV Accuracy test. Since then it has had little work done on it,
but it is probably one of the most accurate open source OCR engines
available. The source code will read a binary, grey or color image
and output text. A tiff reader is built in that will read
uncompressed TIFF images, or libtiff can be added to read compressed
images.

%package eng
Group:   Graphics
Summary: English language pack for tesseract

%description eng
Data files required to recognize English OCR.

%package fra
Group:   Graphics
Summary: French language pack for tesseract

%description fra
Data files required to recognize French OCR.

%package ita
Group:   Graphics
Summary: Italian language pack for tesseract

%description ita
Data files required to recognize Italian OCR.

%package deu
Group:   Graphics
Summary: German language pack for tesseract

%description deu
Data files required to recognize German OCR.

%package spa
Group:   Graphics
Summary: Spanish language pack for tesseract

%description spa
Data files required to recognize Spanish OCR.

%package nld
Group:   Graphics
Summary: Dutch language pack for tesseract

%description nld
Data files required to recognize Dutch OCR.

%prep
%setup -q -a1 -a2 -a3 -a4 -a5 -a6

%build
%configure2_5x
%make

%install
%makeinstall_std

%clean
rm -rf %buildroot 

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README ReleaseNotes ChangeLog
%{_bindir}/*
%{_datadir}/tessdata

%files -n %{libnamedev}
%defattr(-,root,root)
%{_includedir}/tesseract
%{_libdir}/*.a

%files eng
%{_datadir}/tessdata/eng.*

%files fra
%{_datadir}/tessdata/fra.*

%files ita
%{_datadir}/tessdata/ita.*

%files deu
%{_datadir}/tessdata/deu.*

%files spa
%{_datadir}/tessdata/spa.*

%files nld
%{_datadir}/tessdata/nld.*
