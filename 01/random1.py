
import random
import string


a = list('tatttatatttatatctatattaatataataatttatataaaataaattttaaacttataaattttaaatttttaatttcaggtttttataagatttatagcgccaatttttattatttaaattaaatttattaatttttgagtttttagacctgttgctataaatatcacattaaataattatagaatagattgcctgacaaaaggattactttgatagagtaaattatataatattaactattatatctattagctcaaatttatatttaatagaattaaactatctctaaaagtatcaaaaacttttgtgcttcatacactaaaatataattatttttattaaaaaagataagctaattaagctaataggttcataccctatttataaaggttttaatccttttctttttaattattaaaaattcctataaatttttatttcttatttcattaatatcaggtacattaattgctgtgtcatctacttcttgatttagaatttgaataggattggaaattaatttattgtcttttattcccttaataataagatcaaaaaatttattttcttcagaatcctcattgaagtatttcttaacacaagccttagcatcctcggtattattattctctattattttaatatatttatttattaattttaagattaattttatagtttataatataatattaatttcttcaactataatactaaaaagagggacagctcctttccatttttgattcccaagtgtgatagaaggtttaagatgaaattctaattttttattaataacatgacaaaaattagccccattaataattttatcttatagactatctttaaatttattaatttttattatttttttttcaataatttttggtagtcttggaggtattaatcaaacttctttacgaaaattaatagctttttcttctattaatcacttaggttgaatattaagtggaatattaaacaatgaaataatttgatttagatattttttattttatagttttttaaatttttctattgtattcatatttaatagatttaaaatttttaatattaatcaaacttttaaaatatttaattctaataaatttataataatttcaatatttttacttcttttatctttaggaggcttacccccatttttaggatttttaccaaaatgactgatgatgattaatattttttattattttttctaataaaactactttataataaactttatcaattttatagactagctaattactaagaaagctttaagttaatctaaactaatagccttcaaagttataaataaaaatatatttttaagctttaataaatagtaatttattcctttagaattgcagtctaatatcatttatatgaatataaagcctaaaaaattaataattttttattttattttaataaaaaaaaattactttataatagtataacttaaatttaaagtcataaaattaatttttaaaattataagattatgaaataaatttaattttaaaatgtgttttttcaaacccagcaataacttaattaaagaaaaataattttcataaatagatttacaatctaacgcctaaacttcagccatttaatttattgagttttgcgacaatggttattttctacaaatcacaaagatattggaacattatattttattttcggagcttgatcaggaatagtaggtacttctctaagaatcttaattcgagctgaattaggtcatgcgggttcattaattggtgatgaccaaatttataatgttattgttacagctcatgcttttgtaataatttttttcatggttatacctattttaattggaggatttgggaactgattagttcctttaatactaggagctcctgacatagctttccctcgaataaataatataagtttttgattattacctccttctcttaccttacttctttcaagttcaattgttgaaaacggagctgggacaggatgaactgtttatcctcctctttcttcaggaattgctcac')

a[0:119] = [random.choice(['c', 'a'])for _ in range(120)]   #数组前120位，随机生成120个a和c组成的数组
a[120:199] = [random.choice(['t', 'g'])for _ in range(80)]  #数字前121——200位，随机生成80个由t和g组成的数组
random.shuffle(a[0:199])   #将前200个字母打乱

a[-200:-81] = [random.choice(['a', 'c'])for _ in range(120)]
a[-80:] = [random.choice(['t', 'g'])for _ in range(80)]
random.shuffle(a[-200:])     #将倒数200个字母打乱

print(a)
print(a)





# random.shuffle(a)
# print(random.choice('abf'))

# print(''.join(random.sample(['a', 'c'], 200)))
# print(a)

# print(''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)))
#
# print(random.sample('abcd', 5))

# print(a)

#b = [random.choice(['y', 'h'])for _ in range(120)]

