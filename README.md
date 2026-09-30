Rastgele Seçici

Bu proje, kararsız kalınan durumlarda verilen bir liste içerisinden rastgele bir seçenek belirleyen basit bir Python dosyasıdır.

Nasıl Çalışır?

Kodun içerisindeki her bir bölümün ne işe yaradığı aşağıda açıklanmıştır:

import random: Python'un yerleşik rastgele sayı ve rastgele seçim yapma modülünü koda dahil eder.

secenekler = [...]: Seçim yapılacak olan alternatifleri (örneğin; "dönerci", "ev", "çatı", "yemekhane") içeren bir listedir. İstediğiniz zaman bu listeye yeni seçenekler ekleyebilir veya çıkarabilirsiniz.

random.choice(secenekler): secenekler listesi içerisinden tamamen rastgele bir öğe seçme işlemini gerçekleştirir.

print(...): Kullanıcıya önce mevcut tüm seçenekleri, ardından da rastgele seçilmiş olan sonucu ekranda gösterir.

input("Cikmak icin ENTER tusuna basin..."): Program çalışmasını tamamladıktan sonra komut ekranının aniden kapanmasını önlemek için kullanıcının ENTER tuşuna basmasını bekler.

Kullanım

Bilgisayarınızda Python'un kurulu olduğundan emin olun.

rasgeleseçim.py dosyasını çalıştırın.

Ekranda seçeneklerinizi ve rastgele seçilen sonucu göreceksiniz. Programdan çıkmak için ENTER tuşuna basmanız yeterlidir.
