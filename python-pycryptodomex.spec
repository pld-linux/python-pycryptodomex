# Conditional build:
%bcond_with	doc	# API documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	pycryptodomex
Summary:	Package of low-level cryptographic primitives
Name:		python-%{module}
Version:	3.10.1
Release:	2
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.debian.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	91b86ca7fa80d41179d7735067c7347a
URL:		https://www.pycryptodome.org/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.5
%if %{with tests}
#BuildRequires:	python-
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
%if %{with tests}
#BuildRequires:	python3-
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python-modules >= 1:2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyCryptodomex is a fork of PyCrypto. It brings the following
enhancements with respect to the last official version of PyCrypto
(2.6.1):

- Authenticated encryption modes (GCM, CCM, EAX, SIV, OCB)
- Accelerated AES on Intel platforms via AES-NI
- First class support for PyPy
- Elliptic curves cryptography (NIST P-256, P-384 and P-521 curves
  only)
- Better and more compact API (nonce and iv attributes for ciphers,
  automatic generation of random nonces and IVs, simplified CTR cipher
  mode, and more)
- SHA-3 (including SHAKE XOFs), truncated SHA-512 and BLAKE2 hash
  algorithms
- Salsa20 and ChaCha20/XChaCha20 stream ciphers
- Poly1305 MAC
- ChaCha20-Poly1305 and XChaCha20-Poly1305 authenticated ciphers
- scrypt, bcrypt and HKDF derivation functions
- Deterministic (EC)DSA
- Password-protected PKCS#8 key containers
- Shamir's Secret Sharing scheme
- Random numbers get sourced directly from the OS (and not from a
  CSPRNG in userspace)
- Simplified install process, including better support for Windows
- Cleaner RSA and DSA key generation (largely based on FIPS 186-4)
- Major clean ups and simplification of the code base

%package -n python3-%{module}
Summary:	Package of low-level cryptographic primitives
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-%{module}
PyCryptodomex is a fork of PyCrypto. It brings the following
enhancements with respect to the last official version of PyCrypto
(2.6.1):

- Authenticated encryption modes (GCM, CCM, EAX, SIV, OCB)
- Accelerated AES on Intel platforms via AES-NI
- First class support for PyPy
- Elliptic curves cryptography (NIST P-256, P-384 and P-521 curves
  only)
- Better and more compact API (nonce and iv attributes for ciphers,
  automatic generation of random nonces and IVs, simplified CTR cipher
  mode, and more)
- SHA-3 (including SHAKE XOFs), truncated SHA-512 and BLAKE2 hash
  algorithms
- Salsa20 and ChaCha20/XChaCha20 stream ciphers
- Poly1305 MAC
- ChaCha20-Poly1305 and XChaCha20-Poly1305 authenticated ciphers
- scrypt, bcrypt and HKDF derivation functions
- Deterministic (EC)DSA
- Password-protected PKCS#8 key containers
- Shamir's Secret Sharing scheme
- Random numbers get sourced directly from the OS (and not from a
  CSPRNG in userspace)
- Simplified install process, including better support for Windows
- Cleaner RSA and DSA key generation (largely based on FIPS 186-4)
- Major clean ups and simplification of the code base

%package apidocs
Summary:	API documentation for Python %{module} module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona %{module}
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Python %{module} module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona %{module}.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
%{__make} -C Doc html \
	PHINXBUILD=sphinx-build-3
rm -rf Doc/_build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc {AUTHORS,Changelog,FuturePlans,README}.rst
%dir %{py_sitedir}/Cryptodome
%{py_sitedir}/Cryptodome/*.py[coi]
%{py_sitedir}/Cryptodome/py.typed
%dir %{py_sitedir}/Cryptodome/Cipher
%{py_sitedir}/Cryptodome/Cipher/*.py[coi]
%attr(755,root,root) %{py_sitedir}/Cryptodome/Cipher/*.so
%dir %{py_sitedir}/Cryptodome/Hash
%{py_sitedir}/Cryptodome/Hash/*.py[coi]
%attr(755,root,root) %{py_sitedir}/Cryptodome/Hash/*.so
%{py_sitedir}/Cryptodome/IO
%dir %{py_sitedir}/Cryptodome/PublicKey
%{py_sitedir}/Cryptodome/PublicKey/*.py[coi]
%attr(755,root,root) %{py_sitedir}/Cryptodome/PublicKey/*.so
%dir %{py_sitedir}/Cryptodome/Protocol
%{py_sitedir}/Cryptodome/Protocol/*.py[coi]
%attr(755,root,root) %{py_sitedir}/Cryptodome/Protocol/*.so
%{py_sitedir}/Cryptodome/Random
%{py_sitedir}/Cryptodome/SelfTest
%{py_sitedir}/Cryptodome/Signature
%dir %{py_sitedir}/Cryptodome/Util
%{py_sitedir}/Cryptodome/Util/*.py[coi]
%attr(755,root,root) %{py_sitedir}/Cryptodome/Util/*.so
%dir %{py_sitedir}/Cryptodome/Math
%{py_sitedir}/Cryptodome/Math/*.py[coi]
%attr(755,root,root) %{py_sitedir}/Cryptodome/Math/*.so
%{py_sitedir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc {AUTHORS,Changelog,FuturePlans,README}.rst
%dir %{py3_sitedir}/Cryptodome
%{py3_sitedir}/Cryptodome/*.py*
%{py3_sitedir}/Cryptodome/py.typed
%{py3_sitedir}/Cryptodome/__pycache__
%dir %{py3_sitedir}/Cryptodome/Cipher
%{py3_sitedir}/Cryptodome/Cipher/*.py*
%{py3_sitedir}/Cryptodome/Cipher/__pycache__
%attr(755,root,root) %{py3_sitedir}/Cryptodome/Cipher/*.so
%dir %{py3_sitedir}/Cryptodome/Hash
%{py3_sitedir}/Cryptodome/Hash/*.py*
%{py3_sitedir}/Cryptodome/Hash/__pycache__
%attr(755,root,root) %{py3_sitedir}/Cryptodome/Hash/*.so
%{py3_sitedir}/Cryptodome/IO
%dir %{py3_sitedir}/Cryptodome/PublicKey
%{py3_sitedir}/Cryptodome/PublicKey/*.py*
%{py3_sitedir}/Cryptodome/PublicKey/__pycache__
%attr(755,root,root) %{py3_sitedir}/Cryptodome/PublicKey/*.so
%dir %{py3_sitedir}/Cryptodome/Protocol
%{py3_sitedir}/Cryptodome/Protocol/*.py*
%{py3_sitedir}/Cryptodome/Protocol/__pycache__
%attr(755,root,root) %{py3_sitedir}/Cryptodome/Protocol/*.so
%{py3_sitedir}/Cryptodome/Random
%{py3_sitedir}/Cryptodome/SelfTest
%{py3_sitedir}/Cryptodome/Signature
%dir %{py3_sitedir}/Cryptodome/Util
%{py3_sitedir}/Cryptodome/Util/*.py*
%{py3_sitedir}/Cryptodome/Util/__pycache__
%attr(755,root,root) %{py3_sitedir}/Cryptodome/Util/*.so
%dir %{py3_sitedir}/Cryptodome/Math
%{py3_sitedir}/Cryptodome/Math/*.py*
%{py3_sitedir}/Cryptodome/Math/__pycache__
%attr(755,root,root) %{py3_sitedir}/Cryptodome/Math/*.so
%{py3_sitedir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
