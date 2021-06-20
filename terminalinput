from PIL import Image
from matplotlib import pyplot as plt
from matplotlib_venn import venn3
import sys, os

print('*Venn diagrams*')
print("just use words, separated by a comma without spaces. example:")
print("bee,ant,wasp,spider")
#input("Press Enter to continue...")
  #to works better with pyinstaller the onefile .exe
imputname_a = input('Name SET A > ')
imputa = input('List SET A > ')
a = set(imputa.split(","))
print(a)
imputname_b = input('Name SET B > ')
imputb = input('List SET B > ')
b = set(imputb.split(","))
print(b)
imputname_c = input('Name SET C > ')
imputc = input('List SET C > ')
c = set(imputc.split(","))
print(c)
set1 = a
set2 = b
set3 = c
namea = imputname_a
nameb = imputname_b
namec = imputname_c
venn = venn3([set1, set2, set3], (namea, nameb, namec))
venn.get_label_by_id('100').set_text('\n'.join(set1-set2-set3))
venn.get_label_by_id('110').set_text('\n'.join(set1&set2-set3))
venn.get_label_by_id('010').set_text('\n'.join(set2-set3-set1))
venn.get_label_by_id('101').set_text('\n'.join(set1&set3-set2))
venn.get_label_by_id('111').set_text('\n'.join(set1&set2&set3))
venn.get_label_by_id('011').set_text('\n'.join(set2&set3-set1))
venn.get_label_by_id('001').set_text('\n'.join(set3-set2-set1))
plt.title("Diagram")
plt.savefig('1.png')

#img = Image.open('1.png')
#img.show()
  #to show img maybe
  
plt.show()
sys.exit(0)
