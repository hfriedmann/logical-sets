import matplotlib.pyplot as plt
from matplotlib_venn import venn3

set1 = {1, 2, 4, 6, 8}
set2 = {1, 2, 3, 5, 7, 9}
set3 = {1, 3, 5, 7}

venn3([set1, set2, set3], ('Group1', 'Group2', 'Group3'))

venn = venn3([set1, set2, set3], ('Set1', 'Set2', 'Set3'))
  
  #this make the groups have the values right in them, not only the amount
venn.get_label_by_id('100').set_text('\n'.join(set1-set2-set3))
venn.get_label_by_id('110').set_text('\n'.join(set1&set2-set3))
venn.get_label_by_id('010').set_text('\n'.join(set2-set3-set1))
venn.get_label_by_id('101').set_text('\n'.join(set1&set3-set2))
venn.get_label_by_id('111').set_text('\n'.join(set1&set2&set3))
venn.get_label_by_id('011').set_text('\n'.join(set2&set3-set1))
venn.get_label_by_id('001').set_text('\n'.join(set3-set2-set1))

plt.show()
