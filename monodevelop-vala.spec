Name:     	monodevelop-vala
Version:	1.9.2
Release:	%mkrel 1
License:	MIT
BuildArch:      noarch
URL:		http://www.go-mono.com
Source0:	http://ftp.novell.com/pub/mono/sources/monodevelop-vala/%{name}-%{version}.tar.bz2
BuildRequires:  monodevelop >= %version
BuildRequires:  mono-devel
Summary:	Monodevelop Vala Addin
Group:		Development/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:       vala

%description
Monodevelop Vala Addin


%prep
%setup -q

%build
./configure --prefix=%_prefix
%make

%install
rm -rf "$RPM_BUILD_ROOT" %name.lang
%makeinstall_std

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-, root, root)
%_prefix/lib/monodevelop/AddIns/BackendBindings/MonoDevelop.ValaBinding.dll*
