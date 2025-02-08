from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QRadioButton, QComboBox, QCheckBox, QProgressBar, QPushButton
import sys

class Formulario(QWidget):
    def __init__(self):
        super().__init__()

        # Configurar la ventana
        self.setWindowTitle("Formulario con PyQt")
        self.setGeometry(200, 200, 400, 500)

        # Layout principal
        layout = QVBoxLayout()


        # Etiquetas y campos de texto
        labels = ["Edad", "Edad", "Domicilio", "Tipo", "Entrenador", "Nivel", "Región", "Altura", "Peso", "Habilidad"]

        for label_text in labels:
            h_layout = QHBoxLayout()
            label = QLabel(label_text)
            entry = QLineEdit()
            h_layout.addWidget(label)
            h_layout.addWidget(entry)
            layout.addLayout(h_layout)


        # Radio Buttons (Sexo)
        sexo_label = QLabel("Sexo:")
        layout.addWidget(sexo_label)
        sexo_layout = QHBoxLayout()
        self.radio_masculino = QRadioButton("Masculino")
        self.radio_femenino = QRadioButton("Femenino")
        self.radio_masculino.setChecked(False)
        sexo_layout.addWidget(self.radio_masculino)
        sexo_layout.addWidget(self.radio_femenino)
        layout.addLayout(sexo_layout)

        # Combobox (Escolaridad)
        escolaridad_label = QLabel("Escolaridad:")
        layout.addWidget(escolaridad_label)
        self.combo_escolaridad = QComboBox()
        self.combo_escolaridad.addItems(["Primaria", "Secundaria", "Preparatoria", "Universidad"])
        layout.addWidget(self.combo_escolaridad)

        # Checkbox (Disponible para batallas)
        self.checkbox_batallas = QCheckBox("Disponible para batallas")
        layout.addWidget(self.checkbox_batallas)

        # Barra de progreso
        progreso_label = QLabel("Progreso de entrenamiento:")
        layout.addWidget(progreso_label)
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(90)
        layout.addWidget(self.progress_bar)

        # Botón de cierre
        self.boton_cerrar = QPushButton("Cerrar")
        self.boton_cerrar.clicked.connect(self.close)
        layout.addWidget(self.boton_cerrar)

        # Establecer el layout principal
        self.setLayout(layout)

# Ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    formulario = Formulario()
    formulario.show()
    sys.exit(app.exec_())

    print('nada dsds')