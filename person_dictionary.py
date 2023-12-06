persona = {"nombre":"angel uriel", "primer_apellido":"velasco", "segundo_apellido":"mejia", "edad":23, "ciudad":"mexico",}
print(f"""
Registro...
Nombre:{persona["nombre"].title()}
Apellidos: {persona["primer_apellido"].title()} {persona["segundo_apellido"].title()}
Edad: {persona["edad"]}
Ciudad: {persona["ciudad"].title()}
""")
