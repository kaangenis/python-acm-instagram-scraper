# acmApp

#Gerekli Kütüphaneler:

-Selenium

-PyQt6

#ACM Topluluğu için instagram web scraping ve çekiliş işlemlerini yapan bir bot.

Projenin amacı kullanıcının hedeflediği Instagram gönderisindeki yorum yapan kullanıcıların kullanıcı isimlerinin çekilerek bu kullanıcılar arasında rastgele kazananlar belirlemektir.

'main.py' dosyası çalıştırılarak açılan arayüze hedeflenen gönderinin url'si girildikten sonra 'Yorumları Al' buttonu kullanılarak Selenium tarafından kullanıcı isimleri çekilir.

Bu işlem tamamlandıktan sonra karşımıza gelen kullanıcı isimleri arasından kazananları rastgele şekilde belirlemek için 'Kazananları Belirle' buttonu kullanılarak rastgele biçimde kullanıcı isimleri 'Kazananlar' bölümüne geçer.

'Kazananlar' bölümüne geçen kişi sonraki çekilişten bağımsız tutulur (bir kişinin birden fazla çekilişi kazanmaması ve diğer kişilerin şansını düşürmemesi için)


