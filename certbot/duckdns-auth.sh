#!/bin/sh

# Duck DNS Token y Dominio
TOKEN="${DUCKDNS_TOKEN}"
DOMAIN="${DUCKDNS_DOMAIN}"

# Usamos wget en lugar de curl porque la imagen de Certbot no tiene curl
wget -qO- "https://www.duckdns.org/update?domains=$DOMAIN&token=$TOKEN&txt=$CERTBOT_VALIDATION"

# Esperar para la propagación DNS
echo "Esperando 30 segundos para la propagación DNS..."
sleep 30