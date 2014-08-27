from django.db import transaction

class UserManager(models.Manager):
    """docstring for UserManager"""
    def __init__(self, arg):
        super(UserManager, self).__init__()
        self.arg = arg

    def test():
        User.objects.using('default').all()
        User.objects.using('user').all()

            
class MultiDBModelAdmin(admin.ModelAdmin):
    # 为方便起见定义一个数据库名称常量。
    using = 'other'

    def save_model(self, request, obj, form, change):
        # 让 Django 保存对象到 'other' 数据库。
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # 让 Django 从 'other' 数据库中删除对象。
        obj.delete(using=self.using)

    def queryset(self, request):
        # 让 Django 在 'other' 数据库中搜索对象。
        return super(MultiDBModelAdmin, self).queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        # 让 Django 基于 'other' 数据库生成外键控件。
        return super(MultiDBModelAdmin, self).formfield_for_foreignkey(db_field, request=request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        # 让 Django 基于 'other' 数据库生成多对多关系控件。
        return super(MultiDBModelAdmin, self).formfield_for_manytomany(db_field, request=reque
