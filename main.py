print("¡Hola desde Railway!")

def saludo_personalizado(nombre="Mundo"):
  """Saluda a la persona con un mensaje personalizado."""
  return f"¡Hola, {nombre}! Tu aplicación Python en Railway está funcionando."

if __name__ == "__main__":
  nombre_usuario = "Usuario de Railway"
  mensaje = saludo_personalizado(nombre_usuario)
  print(mensaje)

  print("\nEste script no tiene dependencias externas.")
