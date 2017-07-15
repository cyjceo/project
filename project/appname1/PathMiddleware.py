class UrlMiddleware:
    def process_view(self,request,view_func,view_args,view_kwargs):
        if request.path not in ['/login/','/register/','/login_handle/','/register_handle/','/exit/','/islogin/']:
            request.session['urlpath'] = request.get_full_path()
