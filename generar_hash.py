from werkzeug.security import generate_password_hash, check_password_hash
 
contrasena = input("Escribe la contraseña que quieres proteger: ")
hash_generado = generate_password_hash(contrasena)
 
print("\nCopia este hash completo (sin espacios):")
print(hash_generado)
 
# Comprobamos que el hash funciona
prueba_buena = check_password_hash(hash_generado, contrasena)
prueba_mala = check_password_hash(hash_generado, "otra123")
print("\n¿La contraseña correcta coincide?", prueba_buena)   # True
print("¿Una contraseña falsa coincide?  ", prueba_mala)      # False
