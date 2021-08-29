from django.db import models
from django.core import validators
from django.contrib.auth import get_user_model

class Item(models.Model):
  SEX_CHOICES = (
    (1, '男性'),
    (2, '女性'),
  )
  firstName = models.CharField(
    verbose_name = '姓（first name）', 
    max_length = 200,
    default = ""
  )

  middleName = models.CharField(
    verbose_name = 'ミドルネーム（middle name）', 
    max_length = 200,
    default = ""
  )
  lastName = models.CharField(
    verbose_name = '名（last name）', 
    max_length = 200,
    default = ""
  )

  age = models.IntegerField(
    verbose_name = '年齢',
    validators = [validators.MinValueValidator(1)],
    blank = True,
    null = True,
  )

  sex = models.IntegerField(
    verbose_name = '性別',
    choices = SEX_CHOICES,
    default = ""
  )
  memo = models.TextField(
    verbose_name = '備考',
    max_length = 300,
    blank = True,
    null = True,
  )
  created_at = models.DateTimeField(
    verbose_name = '登録日',
    auto_now_add = True
  )

  created_by = models.ForeignKey(
    get_user_model(),
    verbose_name = '登録ユーザー',
    on_delete = models.CASCADE,
    default = ""
  )

  # 以下は管理サイト上の表示設定
  def __str__(self):
    return str(self.id) + " - " + self.firstName + self.middleName + self.lastName

  class Meta:
    verbose_name = 'アイテム'
    verbose_name_plural = 'アイテム'