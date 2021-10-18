"""Used to enforce user authentication across the website"""

import re

from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.utils.http import is_safe_url

EXEMPT_URLS = [
    re.compile(settings.LOGIN_URL.lstrip("/")),
    re.compile("user/is_authenticated/")
]

if hasattr(settings, "LOGIN_EXEMPT_URLS"):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware(MiddlewareMixin):
    """Login Required Middleware"""

    def process_request(self, request):
        assert hasattr(request, "user"), "The Login Required Middleware"
        if not request.user.is_authenticated:
            path = request.path_info.lstrip("/")
            if not any(m.match(path) for m in EXEMPT_URLS):
                redirect_to = settings.LOGIN_URL
                # 'next' variable to support redirection to attempted page after login
                if len(path) > 0 and is_safe_url(
                    url=request.path_info, allowed_hosts=request.get_host()
                ):
                    redirect_to = f"{settings.LOGIN_URL}?next={request.path_info}"

                return HttpResponseRedirect(redirect_to)
