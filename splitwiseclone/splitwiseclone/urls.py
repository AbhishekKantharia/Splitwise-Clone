from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'^user/(?P<username>[\w-]+)/$',views.user_detail),
    url(r'^account/',include('accounts.urls')),
    url(r'^friends/(?P<username>[\w-]+)/$',views.getfriendlist),
    url(r'^groups/(?P<username>[\w-]+)/$',views.getallgroups),
    url(r'^newgroup/(?P<username>[\w-]+)/$',views.new_group.as_view()),
    url(r'^addfriend/(?P<username>[\w-]+)/(?P<friend_user_name>[\w-]+)/$',views.add_friend),
    url(r'^payfriend/(?P<username>[\w-]+)/(?P<friendname>[\w-]+)/(?P<amount>[\w-]+)/$',views.pay_friend),
    url(r'^uploadimg/(?P<username>[\w-]+)/$',views.upload_img.as_view(),name='upload'),
    url(r'^addmember/(?P<username>[\w-]+)/$',views.add_friend_in_group.as_view()),
    url(r'^members/(?P<username>[\w-]+)/$',views.get_group_members.as_view()),
    url(r'^insight/(?P<username>[\w-]+)/$',views.getTransactions.as_view()),
    url(r'^bargraph1/(?P<username>[\w-]+)/$',views.getTransactions.as_view()),
    url(r'^bargraph2/(?P<username>[\w-]+)/$',views.bargraph2.as_view()),
    url(r'^timeseriesplot/(?P<username>[\w-]+)/$',views.timeSeriesPlot.as_view()),
    url(r'^pieChartTags/(?P<username>[\w-]+)/$',views.tagsPieChart.as_view()),
    url(r'^friendspiechart/(?P<username>[\w-]+)/$',views.friendsPieChart.as_view()),
    url(r'^friendshipchart/(?P<username>[\w-]+)/$',views.friendshipChart.as_view()),
    url(r'^frienddetails/(?P<username>[\w-]+)/$',views.get_friend_details.as_view()),
    url(r'^settleupall/(?P<username>[\w-]+)/$',views.settle_up_all.as_view()),
    url(r'^addtrans/(?P<username>[\w-]+)/$',views.add_transaction.as_view()),
    url(r'^balances/(?P<username>[\w-]+)/$',views.balances.as_view()),
    url(r'^balances2/(?P<username>[\w-]+)/$',views.balances2.as_view()),
    url(r'^leave/(?P<username>[\w-]+)/$',views.leave_group.as_view()),
    url(r'^settleup/(?P<username>[\w-]+)/$',views.settle_up.as_view()),
    url(r'^grouptrans/(?P<username>[\w-]+)/$',views.get_group_transactions.as_view()),
    url(r'^activity/(?P<username>[\w-]+)/$',views.getactivity.as_view()),
    url(r'^name/(?P<username>[\w-]+)/$',views.updatename.as_view()),
    url(r'^passwd/(?P<username>[\w-]+)/$',views.updatepasswd.as_view()),


]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


