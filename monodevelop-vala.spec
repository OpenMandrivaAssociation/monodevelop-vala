%define vala 0.18
Name:     	monodevelop-vala
Version:	2.9.1
Release:	%mkrel 1
License:	MIT
BuildArch:      noarch
URL:		http://www.go-mono.com
Source0:	http://download.mono-project.com/sources/%name/%name-%version.tar.bz2
BuildRequires:  monodevelop >= %version
BuildRequires:  mono-devel
BuildRequires:  mono-addins-devel
BuildRequires:  vala-devel >= %vala
#gw not yet packaged yet: http://code.google.com/p/vtg/
#BuildRequires:  libafrodite-devel
Summary:	Monodevelop Vala Addin
Group:		Development/Other
Requires:       vala >= %vala

%description
Monodevelop Vala Addin


%prep
%setup -q


%build
sed -i -e 's!vala-0.12!vala-0.18!' configure
sed -i -e 's!vala-0.12!vala-0.18!' configure.in
sed -i -e 's!vala-0.12!vala-0.18!' MonoDevelop.ValaBinding.dll.config
autoconf
#./configure --prefix=%_prefix
./configure --prefix=/usr LIBVALA_CFLAGS="-pthread -I/usr/include/vala-0.14 -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include" LIBVALA_LIBS="-pthread -lvala-0.14 -lgobject-2.0 -lgthread-2.0 -lrt -lglib-2.0"
%make

%install
rm -rf "$RPM_BUILD_ROOT" %name.lang
%makeinstall_std

%files
%_prefix/lib/monodevelop/AddIns/BackendBindings/MonoDevelop.ValaBinding.dll*
