#!/bin/sh

# Duck DNS Token y Dominio (Se esperan como variables de entorno en el contenedor)
# Si no están presentes, se pueden hardcodear aquí si se prefiere.
TOKEN="${DUCKDNS_TOKEN}"
DOMAIN="${DUCKDNS_DOMAIN}"

# URL de actualización de Duck DNS para el reto TXT
# El valor de $CERTBOT_VALIDATION es proporcionado automáticamente por Certbot
curl -s "https://www.duckdns.org/update?domains=$DOMAIN&token=$TOKEN&txt=$CERTBOT_VALIDATION"

# Esperar para la propagación DNS
echo "Esperando 30 segundos para la propagación DNS..."
sleep 30
