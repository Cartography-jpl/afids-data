AC_INIT(afids-data, 1.11)
AC_CONFIG_AUX_DIR([config])
AC_CONFIG_MACRO_DIR([config/m4])
AFIDS_COMMON
AC_CONFIG_FILES([afids_data/script/setup_afids_data.csh afids_data/script/setup_afids_data.sh afids_data/data/cspice/geocal.ker afids_data/script/update_spice.sh])
# This set up all the source directories. Source for this is found in
# config/m4/afids_source_directory.m4 so we can include this in multiple
# configuration files.
AFIDS_DATA_SOURCE_DIRECTORY

# Always build AFIDS data
AM_CONDITIONAL([BUILD_AFIDS_DATA], [true])

AFIDS_A_OPTION
AFIDS_DATA_OPTIONS

AC_CONFIG_FILES([Makefile])
AC_OUTPUT

#======================================================================
# Give a nice log message describing what has been configured, and which
# optional libraries are going to be used.
#======================================================================

LOC_MSG()
LOC_MSG([AFIDS data is now configured])
LOC_MSG()
LOC_MSG([  Installation directory:        ${prefix}])
LOC_MSG([  Build debug version:           ${enable_debug}])
LOC_MSG([  Fortran compiler:              ${F77} ${AM_FFLAGS}])
LOC_MSG([  C compiler:                    ${CC} ${CFLAGS}])
LOC_MSG([  CXX compiler:                  ${CXX} ${CXXFLAGS}])
LOC_MSG([  AFIDS test data:               ${ac_afids_test_data_dir_default}])
LOC_MSG([  Have massive test datasets:    ${have_massive_dataset}])
