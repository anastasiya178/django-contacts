from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@method_decorator(csrf_exempt, name="get")
class IsUserAuthenticated(View):
    """
    Handles logic of validating User authentication result.

    Please Note:
        - this view does not require csrf token;
        - endpoint for this view is excluded from LoginRequiredMiddleware.
    """
    def get(self, request, *args, **kwargs) -> JsonResponse:
        """
        Validates whether User is authenticated or not.

        :return: JSON {"is_user_authenticated": bool}
        """
        return JsonResponse({
            "is_user_authenticated": request.user.is_authenticated
        })
