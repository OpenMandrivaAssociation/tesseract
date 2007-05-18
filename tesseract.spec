%define lib_major 0
%define lib_name %mklibname lazy %{lib_major}


Name:     tesseract
Summary:  An OCR Engine that was developed at HP Labs between 1985 and 1995.
Version: 1.04
Release: %mkrel 1
License: LGPL
Group: Development/Libraries
Source: %{name}-%{version}b.tar.bz2
Patch0:  tesseract-1.04-fix-build.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%{_bindir}/cntraining
%{_bindir}/mftraining
%{_bindir}/tesseract
%{_datadir}/tessdata/*
#--------------------------------------------------------------------

%package -n %{lib_name}-devel
Summary:  %{summary}
Group: %{group}
Provides: %name-devel
Requires: %{name} = %{version}

%description -n %{lib_name}-devel
The Tesseract OCR engine was one of the top 3 engines in the 1995
UNLV Accuracy test. Since then it has had little work done on it,
but it is probably one of the most accurate open source OCR engines
available. The source code will read a binary, grey or color image
and output text. A tiff reader is built in that will read
uncompressed TIFF images, or libtiff can be added to read compressed
images.

%files -n %{lib_name}-devel
%defattr(-,root,root)
%dir %{_includedir}/tesseract
%{_includedir}/tesseract/*
%{_libdir}/*.a

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0
%build
export CFLAGS="$RPM_OPT_FLAGS"

%configure2_5x \

%make

%install
make DESTDIR=%buildroot install

%clean
rm -rf %buildroot 

