import schemdraw
import schemdraw.elements as elm
p =schemdraw.Drawing()
V =p.add(elm.SourceV().label('V', loc='left'))
R =p.add(elm.Resistor().label('R').right())
C=p.add(elm.Capacitor().label('C').right())
L= p.add(elm.Inductor().label('L').right())

p.add(elm.Ground().at(V.start))
p.add(elm.Ground().at(L.end))

p.draw()

