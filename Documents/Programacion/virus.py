import pyautogui
import time

def invert_mouse(duration=60):
    end_time = time.time() + duration  # Duración en segundos (por defecto 60 segundos)
    
    # Obtiene la posición inicial del ratón
    last_x, last_y = pyautogui.position()
    
    while time.time() < end_time:
        # Obtiene la posición actual del ratón
        current_x, current_y = pyautogui.position()
        
        # Calcula el movimiento invertido
        move_x = last_x - (current_x - last_x)
        move_y = last_y - (current_y - last_y)
        
        # Mueve el ratón a la posición invertida
        pyautogui.moveTo(move_x, move_y)
        
        # Actualiza la última posición conocida
        last_x, last_y = move_x, move_y
        
        # Pequeña pausa para evitar un uso intensivo del procesador
        time.sleep(0.01)

# Ejecuta la función para invertir el ratón durante 1 minuto
if __name__ == "__main__":
    invert_mouse(60)
