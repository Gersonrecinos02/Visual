import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Definir los conjuntos
A = set(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'])
C = set(['a', '2', 'c', '3', 'e', '4', 'g', '5', 'i', '6', 'k', '7', 'm'])
E = set(['g', 'e', 'r', 's', 'o', 'n'])  # Letras del nombre "Gerson"

# Calcular las regiones del diagrama
only_A = A - C - E
only_C = C - A - E
only_E = E - A - C
A_and_C = (A & C) - E
A_and_E = (A & E) - C
C_and_E = (C & E) - A
A_C_E = A & C & E

# Crear el diagrama
plt.figure(figsize=(10, 8))
venn = venn3([A, C, E], set_labels=('A (Hexadecimal)', 'C', 'E (Gerson)'))

# Etiquetar cada región con sus elementos correspondientes
if venn.get_label_by_id('100'):
    venn.get_label_by_id('100').set_text(', '.join(sorted(only_A)))
if venn.get_label_by_id('010'):
    venn.get_label_by_id('010').set_text(', '.join(sorted(only_C)))
if venn.get_label_by_id('001'):
    venn.get_label_by_id('001').set_text(', '.join(sorted(only_E)))
if venn.get_label_by_id('110'):
    venn.get_label_by_id('110').set_text(', '.join(sorted(A_and_C)))
if venn.get_label_by_id('101'):
    venn.get_label_by_id('101').set_text(', '.join(sorted(A_and_E)))
if venn.get_label_by_id('011'):
    venn.get_label_by_id('011').set_text(', '.join(sorted(C_and_E)))
if venn.get_label_by_id('111'):
    venn.get_label_by_id('111').set_text(', '.join(sorted(A_C_E)))

plt.title("Diagrama de Venn completo: A ∩ C ∩ E")
plt.show()
