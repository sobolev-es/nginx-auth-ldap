%define mod_name        nginx-auth-ldap

Summary: LDAP Authentication module for nginx
Name: nginx-mod-auth-ldap
Version: %{_nginx_abiversion}
Release: 2.git7a0bdb1a%{?dist}
License: BSD-2-Clause
URL: https://github.com/kvspb/nginx-auth-ldap

Source0: nginx-auth-ldap-git7a0bdb1a.tgz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: nginx >= %{_nginx_abiversion}
Requires: openldap
BuildRequires: nginx-mod-devel
BuildRequires: openldap-devel
BuildRequires: pcre-devel
BuildRequires: zlib-devel
BuildRequires: openssl-devel

%description
LDAP Authentication module for nginx

%prep
%setup -q -n nginx-auth-ldap

%build
%nginx_modconfigure --with-http_ssl_module
%nginx_modbuild

%install
%{__rm} -rf %{buildroot}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_modconfdir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_moddir}

%{__install} -p -D -m 0755 %{_builddir}/%{mod_name}/redhat-linux-build/ngx_http_auth_ldap_module.so \
    ${RPM_BUILD_ROOT}%{nginx_moddir}/ngx_http_auth_ldap_module.so

echo 'load_module "%{nginx_moddir}/ngx_http_auth_ldap_module.so";' \
    > %{buildroot}%{nginx_modconfdir}/mod-auth_ldap.conf

%files
%defattr(-,root,root)
%{nginx_moddir}/*.so
%doc LICENSE README.md
%config(noreplace) %{nginx_modconfdir}/mod-*.conf

%clean
%{__rm} -rf %{buildroot}

%changelog
* Sun Jul 14 2024 Eugene S. Sobolev <sobolev@protei.ru>
- Build git.7a0bdb1a for nginx-1.20.1-14.0.2.el9_2.1

* Fri Jul 12 2024 Eugene S. Sobolev <sobolev@protei.ru>
- Build git.241200ea for nginx-1.20.1-14.0.2.el9_2.1
