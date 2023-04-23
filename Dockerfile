# Uporabi osnovno sliko nginx
FROM nginx

# Kopiraj mapo projekta v mapo '/usr/share/nginx/html'
COPY ./ /usr/share/nginx/html/
