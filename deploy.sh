#!/bin/bash
# Test de seguridad - No ejecuta acciones maliciosas
echo "Simulando actividad de malware para pruebas"
echo "Intentando acceder a /etc/passwd (solo lectura simulada)"
ls -la /etc/passwd 2>/dev/null || echo "Acceso simulado fallido"
echo "Creando archivo de prueba .locked (vacío)"
touch .locked
echo "Archivo .locked creado (no contiene datos reales)"
rm -f .locked
echo "Prueba completada - todo inofensivo"
