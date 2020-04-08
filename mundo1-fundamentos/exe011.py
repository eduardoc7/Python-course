lp = float(input('Largura da parede: '))
ap = float(input('Altura da parede: '))
area = lp*ap
tinta = area/2
print('Sua parede tem a dimensão de {}x{} e sua area é de {}m²'.format(lp,ap,area))
print('Para pintar essa parede, será necessário {}L de tinta'.format(tinta))
