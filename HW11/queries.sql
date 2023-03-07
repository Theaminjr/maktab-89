
--1
-- important: کشور اسپانیا تو جدول نبود اما دستوراتش به شکل زیر میشه
Delete from Customer where Country ='Spain'; -- مشتری هایی که از اسپانیا هستن رو پاک کن
select * from Customer where Country = 'Spain';  -- مشتری هایی که از اسپانیا هستن رو نشون بده (برای چک کردن که پاک شدن)

--2
UPDATE 'Order' set OrderDate = '2021-06-20' where CustomerId = 'VICTE'; -- تاریخ رو برای ایدی مشخص شده تغییر بده
select * from 'Order' where CustomerId = 'VICTE'; -- چک کن ببین ایدی تغییر کرده یا نه

--3
insert into Shipper (CompanyName,Phone) values ('snap',123456789),('divar',123456789),('digikala',123456789); -- سه تا شیپر مشخض شده رو به جدول شیپر ها اضافه کن
select * from Shipper; -- لیست کل شیپر هارو نشون بده

--4
select * from Product where UnitPrice < 50 and Discontinued = 1; -- کالا هایی که قیمتشون از ۵۰ واحد کمتره و دیگه تولید نمیشن رو نمایش بده


--5
create table Transfer (
id serial primary key,                   -- ایدی تکراری نمیشه و اتوماتیک افزایش پیدا میکنه
method_transfer TEXT DEFAULT 'by post')  -- تایپ رو برابر تکست قرار بده با مقدار دیفالت مشخص شده


