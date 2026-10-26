import re 

# result = dir(re)

#**RE MODULE**

str = "python kursu: python programlama rehberiniz | 40 saat"

# re.findall() = Belirtilen bir Regex (düzenli ifade) kalıbıyla eşleşen tüm sonuçları bir metin içinden bulup bir liste halinde döndürmeye yarar.

# result = re.findall("python",str)
# result = len(result)

# re.split() = Belirtilen bir Regex kalıbıyla eşleşen yerlerden kaynak metni bölerek (parçalayarak) bir liste halinde döndürmeye yarar.


# result = re.split(" ",str)
# result = re.split("r",str)

# re.sub() = metin üzerinde tarama yapar, kalıp ile eşleşen her yeri bulur ve bu eşleşmeleri anında yeni_metin ile değiştirir.

# result = re.sub(" ","-",str)
# result = re.sub("\s","-",str)

# re.search() = Kaynak metin içinde, belirtilen Regex kalıbıyla eşleşen ilk yeri bulmaya yarar.

result = re.search("python",str)

# result = result.span()
# result = result.start()
# result = result.end()
# result = result.group()
# result = result.string


#**REGULAR EXPRESSİON**

"""
    [] - köşeli parantezler arasına yazılan bütün karakterler
         aranır.
        
        [abc] => a        : 1 match
                 ac       : 2 match
                 python   : no match
        
        [a-e] => [abcde]
        [1-5] => [12345]
        [0-39] => [1239]

        [^abc] => abc dışındaki karakterler.
        [^0-9] => rakam olmayan karakterler.


"""

result = re.findall("[abc]",str)
result = re.findall("[sat]",str)
result = re.findall("[a-e]",str)
result = re.findall("[a-z]",str)
result = re.findall("[0-5]",str)
result = re.findall("[^abc]",str)
result = re.findall("[^0-9]",str)

"""
    . - her hangi bir tek karakteri belirtir

        .. => a    : No match 
              ab   : 1 match 
              abc  : 1 match
              abcd : 2 matches 


"""

result = re.findall("...",str)
result = re.findall("py..on",str)

"""
    ^ - Belirtilen string karakterle başlıyor mu ?

    ^a => a:    1 match
          abc:  1 match
          bac:  No match

"""

result = re.findall("^p",str)

"""
    $ - Belirtilen karakterle bitiyor mu ?

    a$ => a      : 1 match
          lamba  : 1 match
          Python : No match 

"""

result = re.findall("t$",str)
result = re.findall("saat$",str)
result = re.findall("saatt$",str)

"""
    * - Bir karakterin sıfır ya da daha fazla sayıda olmasını 
        kontrol eder.

        ma*n => mn     : 1 match
                man    : 1 match
                maaan  : 1 match
                main   : No match (a' nın arkasına n gelmiyor.)
"""

result = re.findall("sa*t",str)

"""
    + - Bir karakterin bir ya da daha fazla sayıda olmasını 
        kontrol eder.

        ma+n => mn     : No match 
                man    : 1 match 
                maaan  : 1 match 
                main   : No match (a' nın arkasına n gelmiyor.)
"""

result = re.findall("sa+t",str)

"""
    ? - Bir karakterin sıfır ya da bir kez olmasını
        kontrol eder.

        ma+n => mn        : No match
                man       : 1 match
                maaan     : 1 match
                main      : No match (a' nın arkasına n gelmiyor.)
"""

result = re.findall("sa?t",str)


"""
    {} - Karakter sayısını kontrol eder.

        al{2}   => a karakterinin arkasına 1 karakteri 3 kez tekrarlamalı.
        al{2,3} => a karakterinin arkasına 1 karakteri en az 2 en fazla 3 kez tekrarlamalı .
        [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar.
"""

result = re.findall("a{2}",str)
result = re.findall("[0-9]{2}",str)

"""
    | - alternatif seçeneklerden birinin gerçekleşmesi gerekir
        
        a|b => a ya da b 

            cde =>    no match
            ade =>    1 match 
            acdbea => 3 match 
"""

result = re.findall("a|b",str)

"""
    () - gruplamak için kullanılır.

         (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir.
"""

"""
    \ - özel karakterleri aramamızı sağlar.
        \$a => $ karakterinin arkasına a karakterinin arar. Yani
               $ regular exp. engine tarafından yorumlanmaz.

    \A - Belirtilen karakter string in başında mı ?
         \athe => the string in başındamı

    \Z - Belirtilen karakter string in sonunda mı ?
         the\Z => the string in sonunda mı 

    
    
    

    
    \b - Belirtilen karakter kelimenin in başında ya da sonunda mı ?
         \bthe => the kelimenin in başında değil mi?
         the\B => the kelimenin in sonunda değil mi?

    \B - Belirtilen karakter kelimenin in başında ya da sonunda değil mi ?
         \Bthe => the kelimenin in başında değil mi?
         the\B => the kelimenin in sonunda değil mi?

    \d - [0-9] ile aynı anlama gelir yani rakamları arar.
         \d => 12abc34

    \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
         \D => 1abb44_50
    
    \s - Boşluk karakterlerini arar.
    \s - Boşluk karakterleri dışındakiler.
    \w- Alfabetik karakterler, rakamlar ve alt çizgi karakteri.
    \W - \w nin tam tersi

"""

result = re.findall("\Apython",str)
result = re.findall("saat\Z",str)



print(result)