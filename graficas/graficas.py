import matplotlib.pyplot as plt

def generar_pie_grafico():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]
    figura, coordenadas = plt.subplots()
    coordenadas.pie(values, labels=labels)
    plt.savefig('pie2.png')
    plt.close()
