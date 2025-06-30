import json
from jose import jwe
# Se necesita la librería 'cryptography' para generar las claves RSA.
# Generalmente se instala como una dependencia de python-jose.
# Si no, ejecute: pip install cryptography
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# --- NUEVA SECCIÓN: GENERACIÓN DE CLAVES PÚBLICA/PRIVADA RSA ---
# En una aplicación real, cargarías estas claves desde archivos seguros, no las generarías cada vez.
# 1. Generar la clave privada
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
# 2. Obtener la clave pública correspondiente
public_key = private_key.public_key()


# 1. DATOS A PROTEGER (PAYLOAD)
# Este es el contenido que queremos que sea secreto.
claims = {
    "sub": "johndoe",
    "email": "johndoe@example.com",
    "role": "admin",
    "iat": 1677696000
}
# Convertimos el diccionario a una cadena de bytes, que es lo que espera la función de cifrado.
plaintext = json.dumps(claims).encode('utf-8')


# 2. ALGORITMOS DE JWE
# Para JWE, necesitas especificar DOS algoritmos:
# 'alg': El algoritmo de gestión de claves. Usaremos RSA.
# 'enc': El algoritmo de cifrado de contenido. Sigue siendo una opción segura.
JWE_ALG = "RSA-OAEP-256"  # CAMBIO: Usando un algoritmo RSA estándar
JWE_ENC = "A256GCM"


# 3. CIFRADO (ENCRIPTACIÓN) DEL TOKEN USANDO LA CLAVE PÚBLICA
# Usamos jwe.encrypt() pero ahora con la clave PÚBLICA.
# Cualquiera con la clave pública puede crear mensajes, pero solo el poseedor de la clave privada puede leerlos.
encrypted_token = jwe.encrypt(
    plaintext=plaintext,
    key=public_key,
    encryption=JWE_ENC,
    algorithm=JWE_ALG
)

print("--- Token Cifrado (JWE) ---")
print(encrypted_token)
print("\nSi pegas este token en jwt.io, verás que el payload es ilegible.")


# 4. DESCIFRADO (DESENCRIPTACIÓN) DEL TOKEN USANDO LA CLAVE PRIVADA
# Para leer el contenido, el receptor debe tener la CLAVE PRIVADA correspondiente.
# Usamos jwe.decrypt()
try:
    decrypted_payload_bytes = jwe.decrypt(
        jwe_str=encrypted_token,
        key=private_key
    )
    # Convertimos los bytes de vuelta a un diccionario de Python
    decrypted_claims = json.loads(decrypted_payload_bytes)

    print("\n--- Contenido Descifrado ---")
    print("Payload original recuperado exitosamente:")
    print(decrypted_claims)
    print(f"El rol del usuario es: {decrypted_claims.get('role')}")

except Exception as e:
    print(f"\nNo se pudo descifrar el token: {e}")
