# Python3 requests module analysis

## requests 모듈이란?

---

간단하게 requests 모듈은 HTTP REQUEST / RESPONSE 기능을 사용할 수 있는 모듈입니다.

예시로 HTTP/1.1버전의 경우 GET, PUT, POST, HEAD, OPTIONS 등 다양한 HTTP 메서드로 요청이 가능하며 파일 업로드, 매크로 등 다양한 기능에 사용되는 모듈이기도 합니다.

#### References

+ [requests Github](https://github.com/psf/requests)
+ [requests Documentation](https://docs.python-requests.org/en/master/)

### requests module install

---

```bash
~$ pip install requests
~$ pip3 install requests

~$ python3
Python 3.8.10 (default, Jun  2 2021, 10:49:15)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>>
```

### requests REQUEST Code Example

---

```py
import requests

r = requests.get("http://httpbin.org")
print(r.status_code)
print(r.reason)
```

requests 모듈은 이와 같이 짧은 코드로도 요청을 보낼 수 있는 장점이 존재합니다.

만약 put, post, head 등 다양한 메서드로 요청해야되는 경우 requests 모듈 앞에 .method를 추가하여 실행시키면 됩니다.

```py
import requests

get = requests.get
post = requests.post
put = requests.put
head = requests.head
```

---

## requests 모듈 분석

먼저 requests 모듈의 파일 구조는 이렇게 됩니다.

```
requests
   ├── __version__.py    
   ├── _internal_utils.py
   ├── adapters.py
   ├── api.py
   ├── auth.py
   ├── certs.py
   ├── compat.py
   ├── cookies.py
   ├── exceptions.py
   ├── help.py
   ├── hooks.py
   ├── models.py
   ├── packages.py
   ├── sessions.py
   ├── status_codes.py
   ├── structures.py
   └── utils.py
```

+ \_\_version__

    requests 모듈에 관한 버전과 requests 문서 링크 등 다양한 정보가 있는 파일입니다.

    ```py
    __title__ = 'requests'
    __description__ = 'Python HTTP for Humans.'
    __url__ = 'https://requests.readthedocs.io'
    __version__ = '2.25.1'
    __build__ = 0x022501
    __author__ = 'Kenneth Reitz'
    __author_email__ = 'me@kennethreitz.org'
    __license__ = 'Apache 2.0'
    __copyright__ = 'Copyright 2020 Kenneth Reitz'
    __cake__ = u'\u2728 \U0001f370 \u2728'
    ```

+ _internal_utils.py

    _internal_utils.py은 유니코드 문자열 ascii 문자 체크,  ascii 인코딩 정도의 유틸리티 기능을 제공하는 파일입니다.

    ```
    requests._internal_utils
    ~~~~~~~~~~~~~~

    Provides utility functions that are consumed internally by Requests
    which depend on extremely few external helpers (such as compat)
    ```

+ adapters.py

    adapters.py은 requests 모듈을 사용하면서 요청과 연결을 유지하는 코드 등 요청하는 핵심적인 코드가 포함되어있는 파일입니다.

    ```
    requests.adapters
    ~~~~~~~~~~~~~~~~~

    This module contains the transport adapters that Requests uses to define
    and maintain connections.
    ```

+ api.py

    api.py은 requests 모듈의 requests.get, requests.post 등 다양한 요청 api를 사용하기 위해 함수들이 정의되어있는 파일입니다.

    ```
    requests.api
    ~~~~~~~~~~~~

    This module implements the Requests API.
    ```

+ auth.py

    auth.py은 예시로 Authorization 같은 헤더를 구축하기 위한 즉 요청에 대한 인증을 처리하는 파일입니다.

    ```
    requests.auth
    ~~~~~~~~~~~~~

    This module contains the authentication handlers for Requests.
    ```

+ certs.py

    certs.py은 CA인증서 관련 처리하기 위한 파일입니다.

    ```
    requests.certs
    ~~~~~~~~~~~~~~

    This module returns the preferred default CA certificate bundle. There is
    only one — the one from the certifi package.

    If you are packaging Requests, e.g., for a Linux distribution or a managed
    environment, you can change the definition of where() to return a separately
    packaged CA bundle.
    ```

+ compat.py

    compat.py은 python2와 python3 간의 호환성 문제를 처리하는 파일입니다.

    ```
    requests.compat
    ~~~~~~~~~~~~~~~

    This module handles import compatibility issues between Python 2 and Python 3.
    ```

+ cookies.py

    cookies.py은 요청과 동시에 cookielib.CookieJar를 사용할 수 있는 호환성 코드가 있는 파일입니다.

    ```
    requests.cookies
    ~~~~~~~~~~~~~~~~

    Compatibility code to be able to use `cookielib.CookieJar` with requests.

    requests.utils imports from here, so be careful with imports.
    ```

+ exceptions.py

    exceptions.py은 다양한 예외 처리하기 위한 파일입니다.

    ```
    requests.exceptions
    ~~~~~~~~~~~~~~~~~~~

    This module contains the set of Requests' exceptions.
    ```