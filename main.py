from math import sqrt,floor
def is_prime(number):
    # 2 den küçük bir sayı girildiyse asal olmadığına işaret false return ediyoruz
    if number<2:
        return False
    #  hızlanma için sayının kareköküne kadar olan sayılara bölünebilirliğini kontrol ediyoruz
    #  2 ye bölünüyorsa asal olmadığını; false return ederek bildiriyoruz.
    #  sonrasında ise hızlanma için 2'nin katı olan sayılar için asallık kontrol etmiyoruz ;
    #  bunu yaparken 1'den başlatarak 2'şer artırıyoruz fakat 1'e bölünebilirliği kontrol ettirmiyoruz continue ile
    max_level=floor(sqrt(number))
    if number%2==0:
        return False
    for i in range(1,max_level+1,2):
        if i==1:
            continue
        if number%i==0:
            return False
        
    return True



