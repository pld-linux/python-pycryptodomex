# Conditional build:
%bcond_without	doc	# API documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	pycryptodomex
Summary:	Package of low-level cryptographic primitives
Summary(pl.UTF-8):	Pakiet niskopoziomowych funkcji kryptograficznych
Name:		python-%{module}
Version:	3.23.0
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/p/pycryptodomex/%{module}-%{version}.tar.gz
# Source0-md5:	c54ba32585587dd47087a8cf8032d72b
Patch0:		x32.patch
URL:		https://www.pycryptodome.org/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.7
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	sphinx-pdg-3 >= 4.5
# >= 7.1.0 when available
%endif
Requires:	python-modules >= 1:2.7
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

%description -l pl.UTF-8
PyCryptodomex to odgałęzienie PyCrypto. Dostarcza następujące
rozszerzenia w stosunku do ostatniej oficjalnej wersji PyCrypto
(2.6.1):
- uwierzytelniane tryby szyfrowania (GCM, CCM, EAX, SIV, OCB)
- akcelerowane szyfrowanie AES na platformach Intela poprzez AES-NI
- dobra obsługa PyPy
- kryptografia krzywych eliptycznych (tylko NIST P-256, P-384, P-521)
- lepsze i bardziej kompaktowe API (atrybuty nonce i iv dla szyfrów,
  automatyczne generowanie losowych nonce i IV, uproszczony tryb
  szyfrowania CTR itp.)
- SHA-3 (w tym SHAKE XOF), skrócone algorytmy SHA-512 i BLAKE2
- szyfry strumieniowe Salsa20 i ChaCha20/XChaCha20
- MAC Poly1305
- szyfry uwierzytelniane ChaCha20-Poly1305 i XChaCha20-Poly1305
- funkcje pochodne scrypt, bcrypt i HKDF
- deterministyczne (EC)DSA
- kontenery kluczy PKCS#8 chronione hasłem
- schemat Shamir's Secret Sharing
- liczby losowe pochodzące bezpośrednio z systemu operacyjnego
  (zamiast CSPRNG w przestrzeni użytkownika)
- uproszczony proces instalacji, w tym lepsza obsługa Windows
- czystsze generowanie kluczy RSA i DSA (oparte głównie na FIPS 186-4)
- spore oczyszczenie i uproszczenie kodu

%package -n python3-%{module}
Summary:	Package of low-level cryptographic primitives
Summary(pl.UTF-8):	Pakiet niskopoziomowych funkcji kryptograficznych
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.7

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

%description -n python3-%{module} -l pl.UTF-8
PyCryptodomex to odgałęzienie PyCrypto. Dostarcza następujące
rozszerzenia w stosunku do ostatniej oficjalnej wersji PyCrypto
(2.6.1):
- uwierzytelniane tryby szyfrowania (GCM, CCM, EAX, SIV, OCB)
- akcelerowane szyfrowanie AES na platformach Intela poprzez AES-NI
- dobra obsługa PyPy
- kryptografia krzywych eliptycznych (tylko NIST P-256, P-384, P-521)
- lepsze i bardziej kompaktowe API (atrybuty nonce i iv dla szyfrów,
  automatyczne generowanie losowych nonce i IV, uproszczony tryb
  szyfrowania CTR itp.)
- SHA-3 (w tym SHAKE XOF), skrócone algorytmy SHA-512 i BLAKE2
- szyfry strumieniowe Salsa20 i ChaCha20/XChaCha20
- MAC Poly1305
- szyfry uwierzytelniane ChaCha20-Poly1305 i XChaCha20-Poly1305
- funkcje pochodne scrypt, bcrypt i HKDF
- deterministyczne (EC)DSA
- kontenery kluczy PKCS#8 chronione hasłem
- schemat Shamir's Secret Sharing
- liczby losowe pochodzące bezpośrednio z systemu operacyjnego
  (zamiast CSPRNG w przestrzeni użytkownika)
- uproszczony proces instalacji, w tym lepsza obsługa Windows
- czystsze generowanie kluczy RSA i DSA (oparte głównie na FIPS 186-4)
- spore oczyszczenie i uproszczenie kodu

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
%patch -P 0 -p1

# adjust for pycryptodomex
%{__sed} -i -e 's,Crypto\.Util,Cryptodome.Util,' \
	-e 's/"Crypto"/"Cryptodome"/' Doc/conf.py

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
PYTHONPATH=$(echo $(pwd)/build-3/lib.linux-*) \
%{__make} -C Doc html \
	SPHINXBUILD=sphinx-build-3
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
%doc {AUTHORS,Changelog,LICENSE,README}.rst
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
%dir %{py_sitedir}/Cryptodome/Math
%{py_sitedir}/Cryptodome/Math/*.py[coi]
%attr(755,root,root) %{py_sitedir}/Cryptodome/Math/*.so
%dir %{py_sitedir}/Cryptodome/Protocol
%{py_sitedir}/Cryptodome/Protocol/*.py[coi]
%attr(755,root,root) %{py_sitedir}/Cryptodome/Protocol/*.so
%dir %{py_sitedir}/Cryptodome/PublicKey
%{py_sitedir}/Cryptodome/PublicKey/*.py[coi]
%attr(755,root,root) %{py_sitedir}/Cryptodome/PublicKey/*.so
%{py_sitedir}/Cryptodome/Random
%{py_sitedir}/Cryptodome/SelfTest
%{py_sitedir}/Cryptodome/Signature
%dir %{py_sitedir}/Cryptodome/Util
%{py_sitedir}/Cryptodome/Util/*.py[coi]
%attr(755,root,root) %{py_sitedir}/Cryptodome/Util/*.so
%{py_sitedir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc {AUTHORS,Changelog,LICENSE,README}.rst
%dir %{py3_sitedir}/Cryptodome
%{py3_sitedir}/Cryptodome/*.py
%{py3_sitedir}/Cryptodome/*.pyi
%{py3_sitedir}/Cryptodome/py.typed
%{py3_sitedir}/Cryptodome/__pycache__
%dir %{py3_sitedir}/Cryptodome/Cipher
%{py3_sitedir}/Cryptodome/Cipher/*.py
%{py3_sitedir}/Cryptodome/Cipher/*.pyi
%{py3_sitedir}/Cryptodome/Cipher/__pycache__
%attr(755,root,root) %{py3_sitedir}/Cryptodome/Cipher/*.so
%dir %{py3_sitedir}/Cryptodome/Hash
%{py3_sitedir}/Cryptodome/Hash/*.py
%{py3_sitedir}/Cryptodome/Hash/*.pyi
%{py3_sitedir}/Cryptodome/Hash/__pycache__
%attr(755,root,root) %{py3_sitedir}/Cryptodome/Hash/*.so
%{py3_sitedir}/Cryptodome/IO
%dir %{py3_sitedir}/Cryptodome/Math
%{py3_sitedir}/Cryptodome/Math/*.py
%{py3_sitedir}/Cryptodome/Math/*.pyi
%{py3_sitedir}/Cryptodome/Math/__pycache__
%attr(755,root,root) %{py3_sitedir}/Cryptodome/Math/*.so
%dir %{py3_sitedir}/Cryptodome/Protocol
%{py3_sitedir}/Cryptodome/Protocol/*.py
%{py3_sitedir}/Cryptodome/Protocol/*.pyi
%{py3_sitedir}/Cryptodome/Protocol/__pycache__
%attr(755,root,root) %{py3_sitedir}/Cryptodome/Protocol/*.so
%dir %{py3_sitedir}/Cryptodome/PublicKey
%{py3_sitedir}/Cryptodome/PublicKey/*.py
%{py3_sitedir}/Cryptodome/PublicKey/*.pyi
%{py3_sitedir}/Cryptodome/PublicKey/__pycache__
%attr(755,root,root) %{py3_sitedir}/Cryptodome/PublicKey/*.so
%{py3_sitedir}/Cryptodome/Random
%{py3_sitedir}/Cryptodome/SelfTest
%{py3_sitedir}/Cryptodome/Signature
%dir %{py3_sitedir}/Cryptodome/Util
%{py3_sitedir}/Cryptodome/Util/*.py
%{py3_sitedir}/Cryptodome/Util/*.pyi
%{py3_sitedir}/Cryptodome/Util/__pycache__
%attr(755,root,root) %{py3_sitedir}/Cryptodome/Util/*.so
%{py3_sitedir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc Doc/_build/html/{_images,_static,src,*.html,*.js}
%endif
