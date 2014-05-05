Name:           ms-sys
Version:        2.1.4
Release:        1%{?dist}
Summary:        Create DOS/MS-compatible boot records

Group:          Applications/System
License:        GPLv2
URL:            http://ms-sys.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: bash, gettext


%description
This program is used to create DOS/MS-compatible boot records. It is
able to do the same as Microsoft "fdisk /mbr" to a hard disk. It is
also able to do the same as DOS "sys" to a floppy or FAT32 partition
except that it does not copy any system files, only the boot record is
written.


%prep
%setup -q 

%build
%{__mkdir} dep
%{__make} \
    CC="${CC:-%{__cc}}" \
    EXTRA_CFLAGS="%{optflags} -fasm" \
    EXTRA_LDFLAGS="%{optflags}" \
    PREFIX="%{_prefix}" \
    SHELL="/bin/bash"

iconv --from=ISO-8859-1 --to=UTF-8 CONTRIBUTORS > CONTRIBUTORS.new
iconv --from=ISO-8859-1 --to=UTF-8 CHANGELOG > CHANGELOG.new
mv CONTRIBUTORS.new CONTRIBUTORS
mv CHANGELOG.new CHANGELOG

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" PREFIX="%{_prefix}" MANDIR="%{_mandir}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, -)
%doc CHANGELOG CONTRIBUTORS COPYING FAQ README TODO
%doc %{_mandir}/man1/ms-sys.1*
%{_bindir}/ms-sys



%changelog
* Mon May 05 2014 Brandon Perkins <bperkins@redhat.com> 2.1.4-1
- new package built with tito

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild


* Mon Aug 04 2008 Rahul Sundaram <sundaram@fedoraproject.org> - 2.1.3-2
- Fix license tag and disable debugging.

* Mon Aug 04 2008 Rahul Sundaram <sundaram@fedoraproject.org> - 2.1.3-1
- Initial package


