from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.utils.translation import gettext_lazy as _

# 自定义 AdminSite 以加载自定义 CSS
class CustomAdminSite(AdminSite):
	site_header = "眼科临床训练系统后台"
	site_title = "眼科临床训练系统后台"
	index_title = "管理后台"

	def each_context(self, request):
		context = super().each_context(request)
		context["admin_custom_css"] = "/static/admin_custom.css"
		return context

	def get_urls(self):
		from django.urls import path
		urls = super().get_urls()
		return urls

custom_admin_site = CustomAdminSite(name='custom_admin')

# 注册你的模型到 custom_admin_site 而不是 admin.site

# 兼容原有 admin.site


