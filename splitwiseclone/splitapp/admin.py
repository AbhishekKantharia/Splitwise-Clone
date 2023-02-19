# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import UserProfile, Transaction, UserGroup, UserFriend, GroupId,activity

admin.site.register(UserProfile)
# admin.site.register(Group)
admin.site.register(Transaction)
admin.site.register(UserGroup)
admin.site.register(UserFriend)
admin.site.register(GroupId)
admin.site.register(activity)


#
# # Register your models here.
# from splitapp.models import UserProfiles
# from splitapp.models import Groups
# from splitapp.models import Transactions

#
# class UserProfilesAdmin(admin.ModelAdmin):
#   list_display = ['user_id', 'name', 'groups', 'friends']
#
# class GroupsAdmin(admin.ModelAdmin):
#   list_display = ['group_id', 'group_name', 'users']
#
# class TransactionAdmin(admin.ModelAdmin):
#   list_display = ['transaction_id','lender', 'borrower', 'group_id','amount','date_time']

#
# admin.site.register(Groups, GroupsAdmin)
# admin.site.register(UserProfiles, UserProfilesAdmin)
# admin.site.register(Transactions, TransactionAdmin)
