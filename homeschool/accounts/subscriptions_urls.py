from django.urls import path

from . import views

app_name = "subscriptions"
urlpatterns = [
    path("", views.subscriptions_index, name="index"),
    path(
        "create-checkout-session/",
        views.create_checkout_session,
        name="create_checkout_session",
    ),
    path("success/", views.SuccessView.as_view(), name="success"),
    path("stripe-cancel/", views.StripeCancelView.as_view(), name="stripe_cancel"),
    path(
        "stripe-billing-portal/",
        views.create_billing_portal_session,
        name="create_billing_portal_session",
    ),
]
