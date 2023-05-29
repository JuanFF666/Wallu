import tkinter as tk
from tkinter import scrolledtext
import time

class RobotGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Robot GUI")

        # Frame principal
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Frame de control
        self.control_frame = tk.Frame(self.main_frame)
        self.control_frame.pack(padx=10, pady=10)

        # Label de estado
        self.state_label = tk.Label(self.control_frame, text="Estado actual: ")
        self.state_label.pack()

        # Frame de eventos
        self.events_frame = tk.Frame(self.main_frame)
        self.events_frame.pack(padx=10, pady=10)

        # Label de eventos
        self.events_label = tk.Label(self.events_frame, text="Eventos:")
        self.events_label.pack()

        # Lista de eventos
        self.events_listbox = tk.Listbox(self.events_frame, width=90, height=18)
        self.events_listbox.pack()

        # Botones de control
        self.start_button = tk.Button(self.control_frame, text="Iniciar", command=self.start_robot)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(self.control_frame, text="Detener", command=self.stop_robot)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        self.play_button = tk.Button(self.control_frame, text="Reproducir eventos", command=self.play_events)
        self.play_button.pack(side=tk.LEFT, padx=5)

        # Widget de texto para mostrar el mensaje de resultado
        self.result_text = scrolledtext.ScrolledText(self.main_frame, width=60, height=10)
        self.result_text.pack(padx=10, pady=10)

        # Eventos disponibles
        self.events = [
            "1. Se suelta un objeto de la garra del robot.",
            "2. Se mueve y/o cambia la posición u orientación de un objeto mientras se intenta agarrar.",
            "3. El robot no consigue llegar a la posición del objeto después de que se le entrega la posición final.",
            "4. Se oprime el botón de parada de emergencia.",
            "5. Se oprime el botón de continuar.",
            "6. Se oprime el botón de start.",
            "7. El robot llega a la posición del contenedor.",
            "8. Se cambia la categoría de los objetos que se quieren recoger.",
            "9. La garra del robot llega a su posición más extendida pero aún no está cerca del objeto.",
            "10. Ya no hay más objetos reciclables para recoger.",
            "11. La cámara se desconectó y no hay imágenes.",
            "12. El robot no logra agarrar el objeto después de varios minutos.",
            "13. La AI cambia la categoría a botella mientras la garra se acerca a un objeto de la categoría lata."
        ]

        for event in self.events:
            self.events_listbox.insert(tk.END, event)

    def start_robot(self):
        # Acción a realizar al presionar el botón "Iniciar"
        self.state_label.config(text="Estado actual: Iniciado")
        selected_event = self.events_listbox.get(tk.ACTIVE)
        result_message = self.get_result_message(selected_event)
        self.result_text.delete(1.0, tk.END)  # Limpiar el contenido del widget de texto
        self.result_text.insert(tk.END, result_message)

    def stop_robot(self):
        # Acción a realizar al presionar el botón "Detener"
        self.state_label.config(text="Estado actual: Detenido")

    def play_events(self):
        for event in self.events:
            self.events_listbox.selection_clear(0, tk.END)  # Desmarcar cualquier evento previamente seleccionado
            self.events_listbox.selection_set(self.events.index(event))  # Seleccionar el evento actual
            self.events_listbox.event_generate("<<ListboxSelect>>")  # Generar evento de selección en la lista
            result_message = self.get_result_message(event)
            self.result_text.insert(tk.END, result_message)
            self.window.update()  # Actualizar la ventana para que se muestre el mensaje
            time.sleep(2)  # Esperar 2 segundos antes de pasar al siguiente evento
            if event == self.events[-1]:
                break        
    def get_result_message(self, event):
        # Retorna el mensaje de resultado según el evento seleccionado
        if event == "1. Se suelta un objeto de la garra del robot.":
            return "1. Objeto soltado correctamente.\n"
        elif event == "2. Se mueve y/o cambia la posición u orientación de un objeto mientras se intenta agarrar.":
            return "2. Error: Objeto en movimiento.\n"
        elif event == "3. El robot no consigue llegar a la posición del objeto después de que se le entrega la posición final.":
            return "3. Error: No se puede llegar a la posición del objeto.\n"
        elif event == "4. Se oprime el botón de parada de emergencia.":
            return "4. Deteniendo el robot por parada de emergencia.\n"
        elif event == "5. Se oprime el botón de continuar.":
            return "5. Continuando la operación del robot.\n"
        elif event == "6. Se oprime el botón de start.":
            return "6. Iniciando el robot.\n"
        elif event == "7. El robot llega a la posición del contenedor.":
            return "7. Llegada a la posición del contenedor.\n"
        elif event == "8. Se cambia la categoría de los objetos que se quieren recoger.":
            return "8. Cambio de categoría de objetos.\n"
        elif event == "9. La garra del robot llega a su posición más extendida pero aún no está cerca del objeto.":
            return "9. Garra extendida pero objeto lejano.\n"
        elif event == "10. Ya no hay más objetos reciclables para recoger.":
            return "10. No hay más objetos reciclables disponibles.\n"
        elif event == "11. La cámara se desconectó y no hay imágenes.":
            return "11. Error: Cámara desconectada.\n"
        elif event == "12. El robot no logra agarrar el objeto después de varios minutos.":
            return "12. Error: No se pudo agarrar el objeto.\n"
        elif event == "13. La AI cambia la categoría a botella mientras la garra se acerca a un objeto de la categoría lata.":
            return "13. Cambio de categoría a botella durante aproximación a objeto de categoría lata.\n"

    def run(self):
        self.window.mainloop()


robot_gui = RobotGUI()


robot_gui.run()