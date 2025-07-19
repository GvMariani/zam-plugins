%global	debug_package	%{nil}

Summary:	A collection of LV2/LADSPA/JACK audio plugins
Name:	zam-plugins
Version:	4.4
Release:	1
License:	GPLv2+ and ISC
Group:	Sound
Url:		https://www.zamaudio.com/
# Submodules are a pain
#Source0:	https://github.com/zamaudio/zam-plugins/archive/%%{name}-%%{version}.tar.gz
Source0:	%{name}-%{version}.tar.xz
# This package does not build on all arches with upstream build flags.
# These are realtime audio plugins, so we need the fastest possible math;
# flags for x86_64 are set to be compatible with most AMD and Intel CPUs,
# and to use the best possible SIMD instruction set.
Patch0:		zam-plugins-4.4-fix-compile-flags.patch
BuildRequires:	chrpath
BuildRequires:	ladspa-devel
BuildRequires:	libzita-convolver-devel >= 4.0.3
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(clap)
BuildRequires:	pkgconfig(fftw3) >= 3.3.5
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(liblo)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(lv2)
BuildRequires:	pkgconfig(rtaudio)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xrandr)

%description
A collection of LV2/LADSPA/VST/JACK audio plugins for sound processing
developed in-house at ZamAudio.

%files
%doc dpf/LICENSE NOTICE.DPF NOTICE.SFZero README.md
%{_bindir}/Za*

#-----------------------------------------------------------------------------

%package -n %{name}-ladspa
Summary:	A collection of LV2/LADSPA/JACK audio plugins - LADSPA version
Group:	Sound
Requires:	ladspa

%description -n %{name}-ladspa
A collection of LV2/LADSPA/VST/JACK audio plugins for sound processing
developed in-house at ZamAudio.
This package contains the LADSPA version of plugins.

%files -n %{name}-ladspa
%{_libdir}/ladspa/Za*-ladspa.so

#-----------------------------------------------------------------------------

%package -n %{name}-lv2
Summary:	A collection of LV2/LADSPA/JACK audio plugins - LV2 version
Group:	Sound
Requires:	lv2

%description -n %{name}-lv2
A collection of LV2/LADSPA/VST/JACK audio plugins for sound processing
developed in-house at ZamAudio.
This package contains the LV2 version of plugins.

%files -n %{name}-lv2
%{_libdir}/lv2/Za*.lv2/*

#-----------------------------------------------------------------------------

%package -n %{name}-vst
Summary:	A collection of LV2/LADSPA/JACK audio plugins - VST version
Group:	Sound

%description -n %{name}-vst
A collection of LV2/LADSPA/VST/JACK audio plugins for sound processing
developed in-house at ZamAudio.
This package contains the VST version of plugins.

%files -n %{name}-vst
%{_libdir}/vst/Za*-vst.so
%{_libdir}/vst3/Za*.vst3/*

#-----------------------------------------------------------------------------

%package -n %{name}-clap
Summary:	A collection of LV2/LADSPA/JACK audio plugins - CLAP version
Group:	Soundc

%description -n %{name}-clap
A collection of LV2/LADSPA/VST/JACK audio plugins for sound processing
developed in-house at ZamAudio.
This package contains the CLAP version of plugins.

%files -n %{name}-clap
%{_libdir}/clap/*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
# No configure: only Makefile
%set_build_flags
%make PREFIX=%{_prefix} LIBDIR=%{_lib} USE_SYSTEM_LIBS=1

 
%install
%makeinstall_std PREFIX=%{_prefix} LIBDIR=%{_lib} USE_SYSTEM_LIBS=1

# Fix perms
find %{buildroot}%{_libdir}/lv2/ -name "*.ttl" | xargs chmod -x

# Drop rpath
chrpath -d %{buildroot}%{_bindir}/Za*
