# snapshot extracted from git://git.savannah.gnu.org/gnulib.git using
# gnulib-tool --create-testdir --without-tests --dir=${PN} ${PN};
# cd ${PN}; ./configure; make maintainer-clean
%define	subver	20140223
%define	rel		1
Summary:	git "merge" driver for GNU style ChangeLog files
Name:		git-merge-changelog
Version:	0.0.0
Release:	0.%{subver}.%{rel}
License:	GPL-3+
Group:		Applications/Text
Source0:	https://dev.gentoo.org/~ulm/distfiles/%{name}-%{subver}.tar.xz
# Source0-md5:	a7af561b36a8b227f12ccff2ef1a398f
URL:		https://www.gnu.org/software/gnulib/
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The default merge driver of 'git' *always* produces conflicts when
pulling public modifications into a privately modified ChangeLog file.
This is because ChangeLog files are always modified at the top; the
default merge driver has no clue how to deal with this.

This program serves as a 'git' merge driver that avoids these
problems.

%prep
%setup -qc
mv %{name}/* .

sed -n "/README/{h;:x;n;/^#/!{H;bx};g;s/\n*$//;s:/""usr/local:%{_prefix}:g;p;q}" \
	gllib/git-merge-changelog.c >README

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/git-merge-changelog
