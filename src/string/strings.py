class Strings:
    def es_palindromo(self, texto):
        texto_limpio = ''.join(c.lower() for c in texto if c.isalnum())  # Elimina espacios y signos
        return texto_limpio == texto_limpio[::-1]
    def invertir_cadena(self, texto):
        invertida = ""
        for char in texto:
            invertida = char + invertida
        return invertida
    def contar_vocales(self, texto):
        vocales = "aeiouAEIOU"
        return sum(1 for c in texto if c in vocales)
    def contar_consonantes(self, texto):
        texto_limpio = ''.join(c.lower() for c in texto if c.isalpha())
        vocales = "aeiou"
        return sum(1 for c in texto_limpio if c not in vocales)
    def es_anagrama(self, texto1, texto2):
        return sorted(texto1.replace(" ", "").lower()) == sorted(texto2.replace(" ", "").lower())
    def contar_palabras(self, texto):
        return len(texto.split())
    def palabras_mayus(self, texto):
        return ' '.join(p.capitalize() for p in texto.split())
    def eliminar_espacios_duplicados(self, texto):
        return ' '.join(texto.split())
    def es_numero_entero(self, texto):
        if not texto:
            return False
        if texto[0] in ('-', '+'):
            texto = texto[1:]
        return all(c in '0123456789' for c in texto) and bool(texto)
    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for char in texto:
            if char.isalpha():
                inicio = ord('A') if char.isupper() else ord('a')
                resultado += chr(inicio + (ord(char) - inicio + desplazamiento) % 26)
            else:
                resultado += char
        return resultado
    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)
    def encontrar_subcadena(self, texto, subcadena):
        posiciones = []
        len_sub = len(subcadena)
        for i in range(len(texto) - len_sub + 1):
            if texto[i:i + len_sub] == subcadena:
                posiciones.append(i)
        return posiciones
        pass