%define major 0
%define libname %mklibname fifechan %{major}
%define alibname %mklibname fifechan_allegro %{major}
%define ilibname %mklibname fifechan_irrlicht %{major}
%define olibname %mklibname fifechan_opengl %{major}
%define slibname %mklibname fifechan_sdl %{major}
%define devname %mklibname fifechan -d
%define adevname %mklibname fifechan_allegro -d
%define idevname %mklibname fifechan_irrlicht -d
%define odevname %mklibname fifechan_opengl -d
%define sdevname %mklibname fifechan_sdl -d

Name:		fifechan
Version:	0.1.5
Release:	1
Source0:	https://github.com/fifengine/fifechan/archive/%{name}-%{version}.tar.gz
#Bring back all backend library like allegro or irrlicght disabled in upstream in 0.1.5 (penguin)
Patch0:		fifechan-0.1.5-reenable-allegro-irrlicht.patch
Summary:	C++ GUI library designed for games
URL:		http://fifengine.github.io/fifechan/
License:	LGPL
Group:		System/Libraries
BuildRequires:	cmake ninja
BuildRequires:	pkgconfig(python2)



%description
Fifechan is a C++ GUI library designed for games. It comes with a standard
set of 'widgets' and can use several different objects for displaying
graphics and capturing user input.

%package -n %{libname}
Summary:	The Fifechan game UI library
Group:		System/Libraries

%description -n %{libname}
The Fifechan game UI library

%package -n %{alibname}
Summary:	Allegro backend for the Fifechan game UI library
Group:		System/Libraries

%description -n %{alibname}
Allegro backend for the Fifechan game UI library

%package -n %{ilibname}
Summary:	Irrlicht backend for the Fifechan game UI library
Group:		System/Libraries

%description -n %{ilibname}
Irrlicht backend for the Fifechan game UI library

%package -n %{olibname}
Summary:	OpenGL backend for the Fifechan game UI library
Group:		System/Libraries

%description -n %{olibname}
OpenGL backend for the Fifechan game UI library

%package -n %{slibname}
Summary:	SDL backend for the Fifechan game UI library
Group:		System/Libraries

%description -n %{slibname}
SDL backend for the Fifechan game UI library

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	fifechan-devel = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%package -n %{adevname}
Summary:	Development files for %{name}'s Allegro backend
Group:		Development/C
Requires:	%{devname} = %{EVRD}
Requires:	%{alibname} = %{EVRD}
Provides:	fifechan-allegro-devel = %{EVRD}
BuildRequires:	pkgconfig(allegro)
Requires:	pkgconfig(allegro)

%description -n %{adevname}
Development files for %{name}'s Allegro backend

%package -n %{idevname}
Summary:	Development files for %{name}'s Irrlicht backend
Group:		Development/C
Requires:	%{devname} = %{EVRD}
Requires:	%{alibname} = %{EVRD}
Provides:	fifechan-irrlicht-devel = %{EVRD}
BuildRequires:	irrlicht-devel >= 1.8
Requires:	irrlicht-devel >= 1.8

%description -n %{idevname}
Development files for %{name}'s Irrlicht backend

%package -n %{odevname}
Summary:	Development files for %{name}'s OpenGL backend
Group:		Development/C
Requires:	%{devname} = %{EVRD}
Requires:	%{olibname} = %{EVRD}
Provides:	fifechan-opengl-devel = %{EVRD}
BuildRequires:	pkgconfig(gl)
Requires:	pkgconfig(gl)

%description -n %{odevname}
Development files for %{name}'s OpenGL backend

%package -n %{sdevname}
Summary:	Development files for %{name}'s SDL backend
Group:		Development/C
Requires:	%{devname} = %{EVRD}
Requires:	%{slibname} = %{EVRD}
Provides:	fifechan-sdl-devel = %{EVRD}
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(SDL2_image)
BuildRequires:	pkgconfig(SDL2_ttf)
Requires:	pkgconfig(sdl2)
Requires:	pkgconfig(SDL2_image)
Requires:	pkgconfig(SDL2_ttf)

%description -n %{sdevname}
Development files for %{name}'s SDL backend

%prep
%setup -q
%autopatch -p0

%build
%cmake \
	-Dbuild-library:BOOL=ON \
	-G Ninja
%ninja

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/libfifechan.so.%{major}*

%files -n %{alibname}
%%{_libdir}/libfifechan_allegro.so.%{major}*

%files -n %{ilibname}
%{_libdir}/libfifechan_irrlicht.so.%{major}*

%files -n %{olibname}
%{_libdir}/libfifechan_opengl.so.%{major}*

%files -n %{slibname}
%{_libdir}/libfifechan_sdl.so.%{major}*

%files -n %{devname}
%{_libdir}/libfifechan*.so
%dir %{_includedir}/fifechan
%{_includedir}/fifechan.hpp
%{_includedir}/fifechan/*.hpp
%dir %{_includedir}/fifechan/contrib
%{_includedir}/fifechan/widgets

%files -n %{adevname}
%{_includedir}/fifechan/allegro
%{_includedir}/fifechan/contrib/allegro

%files -n %{idevname}
%{_includedir}/fifechan/irrlicht

%files -n %{odevname}
%{_includedir}/fifechan/opengl
%{_includedir}/fifechan/contrib/opengl

%files -n %{sdevname}
%{_includedir}/fifechan/sdl
%{_includedir}/fifechan/contrib/sdl
