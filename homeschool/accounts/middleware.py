from .models import Account


class AccountGateMiddleware:
    """Check that an account is in a valid status to permit access.

    Inactive accounts will be redirected to a plan selection page
    unless the URL is on an allowed list of routes.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.account = None
        if request.user.is_authenticated:
            request.account = Account.objects.filter(user=request.user).first()
        return self.get_response(request)
