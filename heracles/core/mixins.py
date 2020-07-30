from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import View

# class NotPermissions(LoginRequiredMixin,PermissionRequiredMixin):
#     login_url = 'login'
#
#     def handle_no_permission(self):
#         if self.request.user.is_authenticated:
#             mensaje = messages.error(self.request, 'Document deleted.')
#             return HttpResponse(content=mensaje)
#         else:
#             return HttpResponseRedirect(reverse_lazy(self.login_url))

class ValidateRequiredMixin(object):
    permission_required =''
    url_redirect = None

    def get_perms(self):
        if isinstance(self.permission_required, str):
            perms = (self.permission_required,)
        else:
            perms = self.permission_required

        return perms

    def get_url_redirect(self):
        if self.url_redirect == None:
            return reverse_lazy('login')
        return self.url_redirect

    def dispatch(self,request,*args,**kwargs):
        if request.user.has_perm(self.get_perms()):
            return super().dispatch(request,*args,**kwargs)
        messages.error(request, 'No tiene permisos para realizar esta accion')
        return HttpResponseRedirect(self.get_url_redirect())