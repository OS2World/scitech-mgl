Summary: library for full screen [S]VGA graphics
Summary(fr): Biblioth�que pour les graphiques plein �cran [S]VGA
Summary(tr): Tam-ekran [S]VGA �izimleri kitapl���
Name: svgalib
Version: 1.3.1sdd
Release: 5
Exclusivearch: i386
Exclusiveos: Linux
Requires: scitech-nucleus
Copyright: distributable
Group: Libraries
Source: ftp://ftp.scitechsoft.com/pub/linux/svgalib-nucleus-1.3.1.tar.gz
URL: http://www.scitechsoft.com/
Vendor: SciTech Software, Inc.
Packager: Stephane Peter <StephaneP@scitechsoft.com>
Buildroot: /var/tmp/svgalib-root

%description
SVGAlib is a library which allows applications to use full screen
graphics on a variety of hardware platforms. Many games and utilities
are available which take advantage of SVGAlib for graphics access, as
it is more suitable for machines with little memory than X Windows is.

This version of SVGAlib is designed to be used with the Nucleus 
driver architecture provided by SciTech Display Doctor for Linux.
It features many enhancements like acceleration and many new
display modes.

%package devel
Summary: development libraries and include files for [S]VGA graphics
Group: Development/Libraries
Requires: svgalib
Summary(fr): Biblioth�ques et en-t�tes de d�veloppement pour graphiques [S]VGA.
Summary(tr): [S]VGA grafikleri i�in geli�tirme kitapl�klar� ve ba�l�k dosyalar�

%description devel
These are the libraries and header files that are needed to build programs
which use SVGAlib. SVGAlib allows programs to use full screen graphics
on a variety of hardware platforms and without the overhead X requires.

%description -l de devel
Dies sind die Libraries und Header-Dateien, die zum Erstellen von Programmen
erforderlich sind, die SVGAlib verwenden. Mit SVGAlib k�nnen Programme
Vollbildgrafiken auf einer Reihe von Plattformen verwenden, ohne den von X
erforderlichen Overhead.

%description -l fr devel
Biblioth�ques et en-t�tes pour construire des programmes utilisant SVGAlib.
SVGAlib permet au programmes d'utiliser des graphiques plein �cran sur une
grande vari�t� de plates-formes mat�rielles et sans le surco�t qu'entra�ne X.

%description -l tr devel
Bu paket, SVGAlib kitapl���n� kullanan programlar geli�tirmek i�in gereken
ba�l�k dosyalar�n� ve statik kitapl�klar� i�erir.

%package libc5
Summary: SVGAlib libc5 compatibility libraries for glibc systems
Group: Libraries
Requires: svgalib
Summary(fr): Librairies de compatibilit� SVGAlib libc5 pour syst�mes glibc

%description libc5
These are the shared library files to use old libc5 SVGAlib applications
on glibc systems.

%description -l fr libc5
Ce paquetage comprend les librairies partag�es SVGAlib destin�es � �tre
utilis�es avec d'anciennes applications libc5, sur un syst�me bas� sur glibc.

%prep
rm -rf $RPM_BUILD_DIR/svgalib
tar xzovf $RPM_SOURCE_DIR/svgalib-nucleus-1.3.1.tar.gz


%build
cd svgalib
make static shared

%install
export PATH=/sbin:$PATH
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/vga
mkdir -p $RPM_BUILD_ROOT/usr/{bin,include,lib,man/man{1,3,5,6,7}}
mkdir -p $RPM_BUILD_ROOT/usr/i486-linux-libc5/lib
cd svgalib
make INSTALL_PREFIX="$RPM_BUILD_ROOT" install

strip $RPM_BUILD_ROOT/usr/bin/restorefont
strip $RPM_BUILD_ROOT/usr/bin/restorepalette
strip $RPM_BUILD_ROOT/usr/bin/dumpreg
strip $RPM_BUILD_ROOT/usr/bin/restoretextmode

%clean
rm -fr $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%config /etc/vga/*
/usr/bin/*
%doc svgalib/doc/FILES svgalib/doc/Makefile svgalib/doc/README.joystick svgalib/doc/README.patching
%doc svgalib/doc/SECURITY.advisory
%doc svgalib/0-README svgalib/0-INSTALL svgalib/0-RELEASE svgalib/README.scitech
/usr/lib/libvga.so.*
/usr/lib/libvgagl.so.*
/usr/man/man1/*
/usr/man/man5/*
/usr/man/man6/*
/usr/man/man7/*

%files devel
%defattr(-,root,root)
%doc svgalib/demos/*.[ch] svgalib/demos/Makefile
/usr/include/*
/usr/lib/*.a
/usr/lib/*.so
/usr/man/man3/*

%files libc5
%defattr(-,root,root)
/usr/i486-linux-libc5/lib/libvga*.so.*
