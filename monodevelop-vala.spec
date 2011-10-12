%define vala 0.12
Name:     	monodevelop-vala
Version:	2.8
Release:	%mkrel 1
License:	MIT
BuildArch:      noarch
URL:		http://www.go-mono.com
Source0:	http://download.mono-project.com/sources/%name/%name-%version.tar.bz2
#gw missing form the 2.8 tarball:
Source1:	MonoDevelop.ValaBinding.dll.config
BuildRequires:  monodevelop >= %version
BuildRequires:  mono-devel
BuildRequires:  mono-addins-devel
BuildRequires:  vala-devel >= %vala
Summary:	Monodevelop Vala Addin
Group:		Development/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:       vala >= %vala

%description
Monodevelop Vala Addin


%prep
%setup -q
cp %SOURCE1 .

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
