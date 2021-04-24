#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-bdsmatrix
Version  : 1.3.4
Release  : 33
URL      : https://cran.r-project.org/src/contrib/bdsmatrix_1.3-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/bdsmatrix_1.3-4.tar.gz
Summary  : Routines for Block Diagonal Symmetric Matrices
Group    : Development/Tools
License  : LGPL-2.0 LGPL-2.1
Requires: R-bdsmatrix-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-bdsmatrix package.
Group: Libraries

%description lib
lib components for the R-bdsmatrix package.


%prep
%setup -q -c -n bdsmatrix
cd %{_builddir}/bdsmatrix

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589519543

%install
export SOURCE_DATE_EPOCH=1589519543
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bdsmatrix
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bdsmatrix
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bdsmatrix
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc bdsmatrix || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/bdsmatrix/COPYRIGHTS
/usr/lib64/R/library/bdsmatrix/DESCRIPTION
/usr/lib64/R/library/bdsmatrix/INDEX
/usr/lib64/R/library/bdsmatrix/Meta/Rd.rds
/usr/lib64/R/library/bdsmatrix/Meta/features.rds
/usr/lib64/R/library/bdsmatrix/Meta/hsearch.rds
/usr/lib64/R/library/bdsmatrix/Meta/links.rds
/usr/lib64/R/library/bdsmatrix/Meta/nsInfo.rds
/usr/lib64/R/library/bdsmatrix/Meta/package.rds
/usr/lib64/R/library/bdsmatrix/NAMESPACE
/usr/lib64/R/library/bdsmatrix/NEWS.Rd
/usr/lib64/R/library/bdsmatrix/R/bdsmatrix
/usr/lib64/R/library/bdsmatrix/R/bdsmatrix.rdb
/usr/lib64/R/library/bdsmatrix/R/bdsmatrix.rdx
/usr/lib64/R/library/bdsmatrix/help/AnIndex
/usr/lib64/R/library/bdsmatrix/help/aliases.rds
/usr/lib64/R/library/bdsmatrix/help/bdsmatrix.rdb
/usr/lib64/R/library/bdsmatrix/help/bdsmatrix.rdx
/usr/lib64/R/library/bdsmatrix/help/paths.rds
/usr/lib64/R/library/bdsmatrix/html/00Index.html
/usr/lib64/R/library/bdsmatrix/html/R.css
/usr/lib64/R/library/bdsmatrix/include/bdsmatrix.h
/usr/lib64/R/library/bdsmatrix/include/bdsmatrix_stub.h
/usr/lib64/R/library/bdsmatrix/tests/backsolvetest.R
/usr/lib64/R/library/bdsmatrix/tests/backsolvetest.Rout.save
/usr/lib64/R/library/bdsmatrix/tests/bdstest.R
/usr/lib64/R/library/bdsmatrix/tests/bdstest.Rout.save
/usr/lib64/R/library/bdsmatrix/tests/chtest.R
/usr/lib64/R/library/bdsmatrix/tests/chtest.Rout.save
/usr/lib64/R/library/bdsmatrix/tests/chtest2.R
/usr/lib64/R/library/bdsmatrix/tests/chtest2.Rout.save
/usr/lib64/R/library/bdsmatrix/tests/corner.R
/usr/lib64/R/library/bdsmatrix/tests/corner.Rout.save
/usr/lib64/R/library/bdsmatrix/tests/corner2.R
/usr/lib64/R/library/bdsmatrix/tests/corner2.Rout.save
/usr/lib64/R/library/bdsmatrix/tests/gtest.R
/usr/lib64/R/library/bdsmatrix/tests/gtest.Rout.save
/usr/lib64/R/library/bdsmatrix/tests/gtest2.R
/usr/lib64/R/library/bdsmatrix/tests/gtest2.Rout.save
/usr/lib64/R/library/bdsmatrix/tests/matrix.R
/usr/lib64/R/library/bdsmatrix/tests/matrix.Rout.save
/usr/lib64/R/library/bdsmatrix/tests/nullr.R
/usr/lib64/R/library/bdsmatrix/tests/nullr.Rout.save
/usr/lib64/R/library/bdsmatrix/tests/reconcile.R
/usr/lib64/R/library/bdsmatrix/tests/reconcile.Rout.save
/usr/lib64/R/library/bdsmatrix/tests/tinv.R
/usr/lib64/R/library/bdsmatrix/tests/tinv.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/bdsmatrix/libs/bdsmatrix.so
/usr/lib64/R/library/bdsmatrix/libs/bdsmatrix.so.avx2
/usr/lib64/R/library/bdsmatrix/libs/bdsmatrix.so.avx512
