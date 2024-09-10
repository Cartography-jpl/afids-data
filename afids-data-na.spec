Summary: This is the AFIDS data files
Name: afids-data
Version: 1.11
# The "na" is for "no afids a", we don't use the --with-afids-a option
Release: 1na.el%{rhel}
License: Copyright 2019 California Institute of Technology ALL RIGHTS RESERVED
Group: Applications/Engineering
Vendor: California Institute of Technology
URL: http://www-mipl.jpl.nasa.gov/cartlab/cartlab.html
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Prefix: /opt/afids

%description

This is the AFIDS data

%define _debugsource_template %{nil}
%prep
%setup -q

%build
./configure --prefix=/opt/afids
make %_smp_mflags 

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
/opt/afids/data/setup_afids_data.csh
/opt/afids/data/setup_afids_data.sh
/opt/afids/data/cib1
/opt/afids/data/cib5
/opt/afids/data/landsat
/opt/afids/data/srtmL2_filled
/opt/afids/data/srtmL1_filled
/opt/afids/data/adrg
/opt/afids/data/vmap1
/opt/afids/data/vdev/port_gaston_doq.img
/opt/afids/data/vdev/port_gaston_elv.hlf
/opt/afids/data/api/afidswcib1dbTemplate.pdf
/opt/afids/data/api/afidswcib5dbTemplate.pdf
/opt/afids/data/api/afidswcibbothdbTemplate.pdf
/opt/afids/data/api/afidswdbTemplate.pdf
/opt/afids/data/api/ali2Template.pdf
/opt/afids/data/api/aliTemplate.pdf
/opt/afids/data/api/aster2Template.pdf
/opt/afids/data/api/aster2autoTemplate.pdf
/opt/afids/data/api/asterTemplate.pdf
/opt/afids/data/api/cibLinuxTemplate.pdf
/opt/afids/data/api/cibTemplate.pdf
/opt/afids/data/api/dtedTemplate.pdf
/opt/afids/data/api/hyperion2Template.pdf
/opt/afids/data/api/hyperionTemplate.pdf
/opt/afids/data/api/ikonos2Template.pdf
/opt/afids/data/api/ikonosTemplate.pdf
/opt/afids/data/api/landsat2CoregTemplate.pdf
/opt/afids/data/api/landsatCoregTemplate.pdf
/opt/afids/data/api/landsatTemplate.pdf
/opt/afids/data/api/modis2Template.pdf
/opt/afids/data/api/modisTemplate.pdf
/opt/afids/data/api/ntmTemplate.pdf
/opt/afids/data/api/quickbird2Template.pdf
/opt/afids/data/api/quickbirdTemplate.pdf
/opt/afids/data/api/spot2Template.pdf
/opt/afids/data/api/spotTemplate.pdf
/opt/afids/data/api/srtmTemplate.pdf
/opt/afids/data/api/wvMultiAddBandTemplate.pdf
/opt/afids/data/api/wvMultiMasterSecondaryTemplate.pdf
/opt/afids/data/update_spice.sh
/opt/afids/data/cspice/README
/opt/afids/data/cspice/fk/planets/earth_assoc_itrf93.tf
/opt/afids/data/cspice/fk/planets/eci_tod.tf
/opt/afids/data/cspice/geocal.ker
/opt/afids/data/cspice/lsk/naif0012.tls
/opt/afids/data/cspice/lsk/latest_leapseconds.tls
/opt/afids/data/cspice/pck/earth_latest_high_prec.bpc
/opt/afids/data/cspice/pck/earth_070425_370426_predict.bpc
/opt/afids/data/cspice/pck/earth_720101_070426.bpc
/opt/afids/data/cspice/pck/geophysical.ker
/opt/afids/data/cspice/pck/pck00010.tpc
/opt/afids/data/cspice/spk/planets/de432s.bsp
/opt/afids/data/genealg/mat1.int
/opt/afids/data/genealg/mat10.int
/opt/afids/data/genealg/mat11.int
/opt/afids/data/genealg/mat3.int
/opt/afids/data/genealg/mat4.int
/opt/afids/data/genealg/mat5.int
/opt/afids/data/genealg/mat6.int
/opt/afids/data/genealg/mat9.int
/opt/afids/data/genealg/materialofinterest3.ibis
/opt/afids/data/mars_kernel
/opt/afids/data/vdev/EGM96_20_x100.HLF
/opt/afids/data/vdev/af1a_bk.int
/opt/afids/data/vdev/chaman1b_bk.int
/opt/afids/data/vdev/etop02nbelps.hlf
/opt/afids/data/vdev/etop02nobath.hlf
/opt/afids/data/vdev/portgaston_bk.int
/opt/afids/data/vdev/target_bm.img
/opt/afids/data/vdev/world_30as_lwm.img
/opt/afids/data/pommosdata/projdef/earth_equidistant.prj
/opt/afids/data/pommosdata/projdef/earth_geographic.prj
/opt/afids/data/pommosdata/projdef/earth_latlon.vic
/opt/afids/data/pommosdata/projdef/earth_north_pole_stereographic.prj
/opt/afids/data/pommosdata/projdef/earth_proj_equidistant.vic
/opt/afids/data/pommosdata/projdef/earth_proj_latlon.vic
/opt/afids/data/pommosdata/projdef/earth_proj_northpole_stereographic.vic
/opt/afids/data/pommosdata/projdef/earth_proj_sinusoidal.vic
/opt/afids/data/pommosdata/projdef/earth_proj_southpole_stereographic.vic
/opt/afids/data/pommosdata/projdef/earth_sinusoidal.prj
/opt/afids/data/pommosdata/projdef/earth_south_pole_stereographic.prj
/opt/afids/data/pommosdata/projdef/go_make_files.pdf
/opt/afids/data/pommosdata/projdef/luna_equidistant.prj
/opt/afids/data/pommosdata/projdef/luna_geographic.prj
/opt/afids/data/pommosdata/projdef/luna_north_pole_stereographic.prj
/opt/afids/data/pommosdata/projdef/luna_proj_equidistant.vic
/opt/afids/data/pommosdata/projdef/luna_proj_latlon.vic
/opt/afids/data/pommosdata/projdef/luna_proj_northpole_stereographic.vic
/opt/afids/data/pommosdata/projdef/luna_proj_sinusoidal.vic
/opt/afids/data/pommosdata/projdef/luna_proj_southpole_stereographic.vic
/opt/afids/data/pommosdata/projdef/luna_sinusoidal.prj
/opt/afids/data/pommosdata/projdef/luna_south_pole_stereographic.prj
/opt/afids/data/pommosdata/projdef/make_cimage_proj_files.pdf
/opt/afids/data/pommosdata/projdef/mars_equidistant.prj
/opt/afids/data/pommosdata/projdef/mars_geographic.prj
/opt/afids/data/pommosdata/projdef/mars_north_pole_stereographic.prj
/opt/afids/data/pommosdata/projdef/mars_proj_equidistant.vic
/opt/afids/data/pommosdata/projdef/mars_proj_latlon.vic
/opt/afids/data/pommosdata/projdef/mars_proj_northpole_stereographic.vic
/opt/afids/data/pommosdata/projdef/mars_proj_sinusoidal.vic
/opt/afids/data/pommosdata/projdef/mars_proj_southpole_stereographic.vic
/opt/afids/data/pommosdata/projdef/mars_sinusoidal.prj
/opt/afids/data/pommosdata/projdef/mars_south_pole_stereographic.prj
/opt/afids/data/pommosdata/projdef/NOTES_for_Mars_Projections.txt
/opt/afids/data/pommosdata/planet_dem
/opt/afids/data/pommosdata/testcases
/opt/afids/share/joe/*
/opt/afids/data/vextract/*

%changelog
* Tue Mar 14 2023 Smyth <smyth@macsmyth> - 1.11-1.el%{rhel}
- Add pommos data.

* Mon Oct 21 2019 Smyth <smyth@macsmyth> - 1.10-1na.el%{rhel}
- Update high precision earth spice kernel.

* Tue Jun  5 2018 Smyth <smyth@macsmyth> - 1.09-1na.el%{rhel}
- Remove use of relative paths in geocal.ker, this causes problem when
  reloading kernels. Also fix long path problem with cspice.

* Wed Oct 18 2017 Smyth <smyth@macsmyth> - 1.08-1na.el%{rhel}
- Add MARS_KERNEL environment variable for changing where the mars spice
  kernels are.

* Fri Jun 23 2017 Smyth <smyth@macsmyth> - 1.07-1na.el%{rhel}
- Update geophysical.ker to spice toolkit N0066 version

* Thu May 25 2017 Smyth <smyth@macsmyth> - 1.06-1na.el%{rhel}
- Add link for mars_kernel an update leapseconds file.

* Thu Dec 17 2015 Mike M Smyth <smyth@pistol> - 1.05-2na
- Rebuild package

* Wed Nov 25 2015 Mike M Smyth <smyth@pistol> - 1.05-1na
- Update the links used for data to new location on system. In 
  particular, update SRTM to the version 3 of this dataset.

* Tue Jun  2 2015 Mike M Smyth <smyth@pistol> - 1.04-1na
- Add a symbolic link for the latest version of the earth kernel, so
  we can update it easier

* Wed Aug  6 2014 Mike M Smyth <smyth@pistol> - 1.03-1na
- Use smaller planet SPK, the last one used is large because it covers
  a very long time period. This one covers 1950 to 2050, which is
  plenty long

* Mon Aug  4 2014 Mike M Smyth <smyth@pistol> - 1.02-1na
- Update geocal SPICE kernel to include stuff needed for solar angle 
  calculations. 

* Wed Jun  5 2013 Mike M Smyth <smyth@pistol> - 1.01-1na
- Update to latest automake tools (no data changes)

* Thu Nov 29 2012 Mike M Smyth <smyth@pistol> - data-1
- Initial build.








