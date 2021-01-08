from django.db import models

# Create your models here. 
class Spros(models.Model):
  object_type = models.CharField("Тип объекта", max_length=50)
  id_rayona = models.ForeignKey(Rayoni, verbose_name="ID Района", on_delete=models.CASCADE)
  id_goroda = models.ForeignKey(Gorod, verbose_name="ID Города", on_delete=models.CASCADE)
  kolvo_etashei_ot = models.IntegerField("Кол-во этажей от", max_length=3)
  kolvo_etashei_do = models.IntegerField("Кол-во этажей до", max_length=3)
  etash_ot = models.IntegerField("Этаж от", max_length=3)
  etash_do = models.IntegerField("Этаж до", max_length=3)
  kolvo_komnat_ot = models.IntegerField("Кол-во комнат от", max_length=2)
  kolvo_komnat_do = models.IntegerField("Кол-во комнат до", max_length=2)
  ploshad_ot = models.IntegerField("Площадь от", max_length=4)
  ploshad_do = models.IntegerField("Площадь до", max_length=4)
  stoimost_ot = models.IntegerField("Стоимость от", max_length=15)
  stoimost_do = models.IntegerField("Стоимость до", max_length=15)
  id_client = models.ForeignKey(Polzovateli, verbose_name="ID Клиента", on_delete=models.CASCADE)
  actualnost = models.BooleanField("Актуальность")

  class Meta:
    verbose_name = "Спрос"
    verbose_name_plural = "Спрос"

class Rayoni(models.Model):
  name = models.CharField("Наименование района", max_length=100)

  class Meta:
    verbose_name = "Районы"
    verbose_name_plural = "Районы"

class Gorod(models.Model):
  name = models.CharField("Наименование города", max_length=100)

  class Meta:
    verbose_name = "Города"
    verbose_name_plural = "Города"

class Predlozheniya(models.Model):
  object_type = models.CharField("Тип объекта", max_length=50)
  id_rayona = models.ForeignKey(Rayoni, verbose_name="ID Района", on_delete=models.CASCADE)
  id_goroda = models.ForeignKey(Gorod, verbose_name="ID Города", on_delete=models.CASCADE)
  adres = models.CharField("Адрес", max_length=255)
  kolvo_etashei = models.IntegerField("Кол-во этажей", max_length=3)
  etash = models.IntegerField("Этаж", max_length=3)
  kolvo_komnat = models.IntegerField("Кол-во комнат", max_length=2)
  plozhad = models.IntegerField("Площадь", max_length=4)
  xoz_postroyki = models.CharField("Хоз. постройки", max_length=50)
  opisanie = models.CharField("Описание", max_length=255)
  stoimost = models.IntegerField("Стоимость", max_length=15)
  id_prodavca = models.ForeignKey(Polzovateli, verbose_name="ID Продавца", on_delete=models.CASCADE)
  actualnost = models.BooleanField("Актуальность")

  class Meta:
    verbose_name = "Предложения"
    verbose_name_plural = "Предложения"

class Polzovateli(models.Model):
  familia = models.CharField("Фамилия", max_length=50)
  name = models.CharField("Имя", max_length=50)
  otchestvo = models.CharField("Отчество", max_length=50)
  passport = models.CharField("Паспорт", max_length=255)
  nomer_telefona = models.IntegerField("Номер телефона", max_length=11)
  login = models.CharField("Логин", max_length=50)
  password = models.CharField("Пароль", max_length=255)
  id_role = models.ForeignKey(Role, verbose_name="ID Роли", on_delete=models.CASCADE)

  class Meta:
    verbose_name = "Пользователи"
    verbose_name_plural = "Пользователи"

class Role(models.Model):
  name = models.CharField("Наименование роли", max_length=50)

  class Meta:
    verbose_name = "Роли"
    verbose_name_plural = "Роли"

class Straxovoi(models.Model):
  id_predlozhenia = models.ForeignKey(Predlozheniya, verbose_name="ID Предложения", on_delete=models.CASCADE)
  id_rieltora = models.ForeignKey(Polzovateli, verbose_name="ID Риэлтора", on_delete=models.CASCADE)
  id_tarifa = models.ForeignKey(Tariphy, verbose_name="ID Тарифа", on_delete=models.CASCADE)
  kolvo_let = models.IntegerField("Кол-во лет", max_length=4)

  class Meta:
    verbose_name = "Страховой контракт"
    verbose_name_plural = "Страховой контракт"

class Tariphy(models.Model):
  name = models.CharField("Название", max_length=50)
  stavka_polgoda = models.IntegerField("Процентная ставка за полгода", max_length=3)
  stavka_god = models.IntegerField("Процентная ставка за 1 год", max_length=3)
  stavka_tri = models.IntegerField("Процентная ставка за 3 год", max_length=3)

  class Meta:
    verbose_name = "Тарифы"
    verbose_name_plural = "Тарифы"

class Operahii(models.Model):
  name = models.CharField("Название операции", max_length=50)

  class Meta:
    verbose_name = "Операции"
    verbose_name_plural = "Операции"

class Sdelki(models.Model):
  id_kontrakta = models.ForeignKey(Straxovoi, verbose_name="ID Контракта", on_delete=models.CASCADE)
  id_pokypatelia = models.ForeignKey(Polzovateli, verbose_name="ID Покупателя", on_delete=models.CASCADE)
  date = models.DateTimeField("Дата сделки")
  komissionie_agenty = models.IntegerField("Комиссионные агенты", max_length=4)
  proc_rieltora = models.IntegerField("Процент риэлтора", max_length=3)
  id_operachii = models.ForeignKey(Operahii, verbose_name="Код операции", on_delete=models.CASCADE)

  class Meta:
    verbose_name = "Сделки"
    verbose_name_plural = "Сделки"